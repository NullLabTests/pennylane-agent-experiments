import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

np.random.seed(42)
qml.numpy.random.seed(42)

N_WIRES = 4

def feature_map(features, n_wires=N_WIRES):
    for i in range(n_wires):
        qml.Hadamard(i)
    for i in range(len(features)):
        if i % 2:
            qml.AngleEmbedding(features=features[i], wires=range(n_wires), rotation="Z")
        else:
            qml.AngleEmbedding(features=features[i], wires=range(n_wires), rotation="X")

def ansatz(params, n_wires=N_WIRES):
    for i in range(n_wires):
        qml.RY(params[i], wires=i)
    for i in range(n_wires):
        qml.CNOT(wires=[(i - 1) % n_wires, i % n_wires])
    for i in range(n_wires):
        qml.RY(params[i + n_wires], wires=i)

dev = qml.device("default.qubit", wires=N_WIRES)

@qml.qnode(dev)
def circuit(params, features):
    feature_map(features)
    ansatz(params)
    return qml.expval(qml.PauliZ(0))

X, y = make_moons(n_samples=20, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
y_train = (y_train - 0.5) * 2
y_test = (y_test - 0.5) * 2

weights = 0.01 * np.random.randn(2 * N_WIRES)
pred = circuit(weights, X_train[0]) + 0.0

assert isinstance(pred, (float, np.floating)), f"Expected float, got {type(pred)}"
assert -1.0 <= pred <= 1.0, f"Output {pred} outside [-1, 1]"
print(f"H3 smoke test passed. Single prediction value={pred:.6f}")
