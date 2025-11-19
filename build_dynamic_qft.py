import math
from typing import List

from matplotlib import pyplot as plt
from qiskit.circuit import ClassicalRegister, QuantumCircuit


NUM_QUBITS = 10
OUTPUT_FILE = f"dynamic_qft_{NUM_QUBITS}.qasm"


def build_dynamic_qft(num_qubits: int) -> QuantumCircuit:
    if num_qubits <= 0:
        raise ValueError("Number of qubits must be positive")

    circuit = QuantumCircuit(num_qubits)
    classical_registers: List[ClassicalRegister] = []
    for index in range(num_qubits):
        register = ClassicalRegister(1, f"c{index}")
        circuit.add_register(register)
        classical_registers.append(register)

    for target in reversed(range(num_qubits)):
        circuit.h(target)
        circuit.measure(target, classical_registers[target][0])
        for control in range(target):
            angle = math.pi / (2 ** (target - control))
            circuit.p(angle, control).c_if(classical_registers[target], 1)

    return circuit


def main() -> None:
    circuit = build_dynamic_qft(NUM_QUBITS)
    fig = circuit.draw(output="mpl")
    fig.tight_layout()
    plt.show()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as stream:
        stream.write(circuit.qasm())


if __name__ == "__main__":
    main()
