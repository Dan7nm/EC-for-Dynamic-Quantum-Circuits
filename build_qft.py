import math
from matplotlib import pyplot as plt
from qiskit.circuit import QuantumCircuit


NUM_QUBITS = 10
OUTPUT_FILE = f"qft_{NUM_QUBITS}.qasm"


def build_qft(num_qubits: int) -> QuantumCircuit:
	if num_qubits <= 0:
		raise ValueError("Number of qubits must be positive")

	circuit = QuantumCircuit(num_qubits)

	for target in reversed(range(num_qubits)):
		circuit.h(target)
		for control in range(target):
			angle = math.pi / (2 ** (target - control))
			circuit.cp(angle, control, target)

	# for i in range(num_qubits // 2):
	# 	circuit.swap(i, num_qubits - i - 1)
	return circuit


def main() -> None:
	circuit = build_qft(NUM_QUBITS)
	fig = circuit.draw(output="mpl")
	fig.tight_layout()
	plt.show()
	
	# Export to OpenQASM 2.0
	with open(OUTPUT_FILE, 'w') as f:
		f.write(circuit.qasm())

if __name__ == "__main__":
	main()
