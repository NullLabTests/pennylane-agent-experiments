import pennylane as qml
import numpy as np

np.random.seed(42)
qml.numpy.random.seed(42)

N_QUBITS = 4
N_REUPLOAD = 3

dev = qml.device('lightning.qubit', wires=N_QUBITS, shots=None)


def reupload_ansatz(x, params):
    idx = 0
    for r in range(N_REUPLOAD):
        for i in range(N_QUBITS):
            qml.RX(x[i % len(x)], wires=i)
        for i in range(N_QUBITS):
            qml.RY(params[idx], wires=i); idx += 1
        for i in range(N_QUBITS - 1):
            qml.CNOT(wires=[i, i + 1])
        for i in range(N_QUBITS):
            qml.RZ(params[idx], wires=i); idx += 1


@qml.qnode(dev)
def reupload_circuit(x, params):
    reupload_ansatz(x, params)
    return [qml.expval(qml.PauliZ(i)) for i in range(N_QUBITS)]


n_params = N_REUPLOAD * (2 * N_QUBITS)
x = np.array([0.5, -0.3, 0.1, -0.7])
params = np.random.default_rng(42).uniform(-0.1, 0.1, size=n_params)

result = reupload_circuit(x, params)

assert isinstance(result, list), f"Expected list, got {type(result)}"
assert len(result) == N_QUBITS, f"Expected {N_QUBITS} outputs, got {len(result)}"
for i, val in enumerate(result):
    assert -1.0 <= val <= 1.0, f"Output[{i}]={val} outside [-1, 1]"
print(f"H2 smoke test passed. Output shape: ({N_QUBITS},), values={[f'{v:.6f}' for v in result]}")
