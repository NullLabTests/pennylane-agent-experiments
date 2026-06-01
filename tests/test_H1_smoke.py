import pennylane as qml
import numpy as np

np.random.seed(42)
qml.numpy.random.seed(42)

N_QUBITS = 4
N_LAYERS = 2

dev = qml.device('lightning.qubit', wires=N_QUBITS, shots=None)


def global_ansatz(x, params):
    for i in range(N_QUBITS):
        qml.RX(x[i % len(x)], wires=i)
    for l in range(N_LAYERS):
        for i in range(N_QUBITS):
            qml.RY(params[l * 2 * N_QUBITS + i], wires=i)
        for i in range(N_QUBITS - 1):
            qml.CNOT(wires=[i, i + 1])
        for i in range(N_QUBITS):
            qml.RZ(params[l * 2 * N_QUBITS + N_QUBITS + i], wires=i)


@qml.qnode(dev)
def local_cost_circuit(x, params):
    global_ansatz(x, params)
    obs = [qml.PauliZ(i) for i in range(N_QUBITS)]
    return qml.expval(qml.sum(*obs) / N_QUBITS)


n_params = N_LAYERS * 2 * N_QUBITS
x = np.array([0.5, -0.3])
params = np.random.default_rng(42).uniform(-0.1, 0.1, size=n_params)

result = local_cost_circuit(x, params)

assert isinstance(result, (float, np.floating)), f"Expected float, got {type(result)}"
assert -1.0 <= result <= 1.0, f"Output {result} outside [-1, 1]"
print(f"H1 smoke test passed. Output shape: scalar, value={result:.6f}")
