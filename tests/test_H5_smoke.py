import pennylane as qml
from pennylane import numpy as np

np.random.seed(42)
qml.numpy.random.seed(42)

N_LAYERS = 2
N_EPOCHS = 3

dev = qml.device("lightning.qubit", wires=1)

@qml.qnode(dev)
def reupload_circuit(params, x, dm_label):
    for p in params:
        qml.Rot(*x, wires=0)
        qml.Rot(*p, wires=0)
    return qml.expval(qml.Hermitian(dm_label, wires=[0]))

label_0 = np.array([[1], [0]])
label_1 = np.array([[0], [1]])
dm_labels = [l @ l.conj().T for l in [label_0, label_1]]

x = np.array([0.5, -0.3, 0.1])
params = np.random.uniform(size=(N_LAYERS, 3))

result = reupload_circuit(params, x, dm_labels[0])

assert isinstance(result, (float, np.floating)), f"Expected float, got {type(result)}"
assert -1.0 <= result <= 1.0, f"Output {result} outside [-1, 1]"

# Quick training smoke test
from pennylane.optimize import AdamOptimizer
train_params = np.random.uniform(size=(N_LAYERS, 3), requires_grad=True)
opt = AdamOptimizer(0.1)
dm = dm_labels[0]
train_params, _, _ = opt.step(
    lambda p, x, dm: (1 - reupload_circuit(p, x, dm)) ** 2,
    train_params, x, dm
)

final_val = reupload_circuit(train_params, x, dm)
print(f"H5 smoke test passed. Initial fidelity={result:.6f}, after 1 step={final_val:.6f}")
