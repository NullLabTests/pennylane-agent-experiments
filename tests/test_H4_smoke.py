import pennylane as qml
from pennylane import numpy as np

np.random.seed(42)
qml.numpy.random.seed(42)

N_QUBITS = 3
N_SAMPLES = 10

def global_circuit(params, n_qubits):
    for i in range(n_qubits):
        qml.RY(np.pi / 4, wires=i)
    for i in range(n_qubits):
        qml.RX(params[i], wires=i)
    for i in range(n_qubits - 1):
        qml.CZ(wires=[i, i + 1])
    H = np.zeros((2 ** n_qubits, 2 ** n_qubits))
    H[0, 0] = 1
    return qml.expval(qml.Hermitian(H, list(range(n_qubits))))

def local_circuit(params, n_qubits):
    for i in range(n_qubits):
        qml.RY(np.pi / 4, wires=i)
    for i in range(n_qubits):
        qml.RX(params[i], wires=i)
    for i in range(n_qubits - 1):
        qml.CZ(wires=[i, i + 1])
    return qml.expval(qml.PauliZ(0))

def compute_grad_var(circuit_fn, n_qubits):
    dev = qml.device("default.qubit", wires=n_qubits)
    qnode = qml.QNode(circuit_fn, dev, diff_method="parameter-shift")
    grad_fn = qml.grad(qnode)
    grads = []
    for _ in range(N_SAMPLES):
        p = np.random.uniform(-np.pi, np.pi, size=n_qubits)
        g = grad_fn(p, n_qubits=n_qubits)
        grads.append(g[-1])
    return float(np.var(np.array(grads)))

var_global = compute_grad_var(global_circuit, N_QUBITS)
var_local = compute_grad_var(local_circuit, N_QUBITS)

assert isinstance(var_global, float), f"Expected float, got {type(var_global)}"
assert var_global >= 0, f"Variance should be non-negative, got {var_global}"
assert var_local >= 0, f"Variance should be non-negative, got {var_local}"
print(f"H4 smoke test passed. Global var={var_global:.6e}, Local var={var_local:.6e}")
