from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit import BasicAer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from qiskit.visualization import plot_state_city
import numpy as np

APItoken = "token here"
url = "url here"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

#Creating a Quantum Register with 2 qubit and a Classical Register with 2 bits 
q_reg = QuantumRegister(2)
c_reg = ClassicalRegister(2)
qc = QuantumCircuit(q_reg, c_reg)

#Preparation phase. Entanglement of 2 qubits (as explained in other entanglement.py file) long before the communication starts.
qc.h(q_reg[0])
qc.cx(q_reg[0],q_reg[1])

#Barrier necessary to prevent noise
#qc.barrier()

# If Alice wants to send '00', do not apply any gate
# if Alice wants to send '01' apply a PauliX gate
# if Alice wants to send '10' apply a PauliZ gate
# if Alice wants to send '11' apply a PauliX gate followed by a PauliZ gate

#Alice gets her qubit from the couple entangled and prepares it applying the X gate to send the message '01'
qc.x(q_reg[0])

#Bob has already received his qubit and has just received a qubit from Alice.
#Applies the CNOT and Hadamard Gate to reverse the entanglement preparing to read the message
qc.cx(q_reg[0],q_reg[1])
qc.h(q_reg[0])

#Bob reads the message by measuring the 2 qubits.
qc.measure(q_reg,c_reg)

#Setting the simulator
backends = BasicAer.get_backend('qasm_simulator')

#Use this to run on a real machine
#backend_sim = IBMQ.get_backend(backends)

result = execute(qc, backends, shots=1024).result()
#the result printed would be '01'

#Shows a drawing of the actual circuit
#qc.draw()

print(result.get_counts(qc))

#plot_state_city(result.get_counts(qc))

#Plots an istogram with the results
plot_histogram(result.get_counts(qc))
