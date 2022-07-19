from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(4, 4) # Number of qubits, number of measure outcomes

qc.h(0)
qc.cx(0, 1)
qc.barrier()

qc.x(2)
qc.h(3)
qc.barrier()

qc.toffoli(1, 2, 3)

qc.measure(1, 3)
qc.measure(0, 1)
qc.measure([2, 3], [0, 2])
# qc.measure_all()

# Draw the circuit diagram
qc.draw(output='mpl')
plt.show() # add when using command line
# print(qc) # text one for command line

# Simulate the circuit.
# Remember to mesure the results!
sim = Aer.get_backend('aer_simulator') # other simulator can also be used
qobj = assemble(qc)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts) # set the finename attribute to save to a new file
plt.show() # add when using command line

