# Superdense coding

### Superdense coding is a quantum communication protocol that uses a preparaed quantum entangled couple of qubits to increase the rate of information sent through a quantum channel.
### With this protocol it is possible to send 2 classical bits of information sending one qubit.

<img width="880" alt="Schermata 2019-06-03 alle 14 37 25" src="https://user-images.githubusercontent.com/37590676/58802769-4530c900-860e-11e9-845b-1806f939834a.png">

Let's say Alice wants to send two classical bits of information (00, 01, 10 or 11) to Bob using qubits.

First, an entangled Bell state is prepared. Then, long before the communication is established one of these qubits is sent to Alice and the other to Bob.

Now Alice has to decide what two-bit message send to Bob (00, 01, 10, 11).
Each combination represents one of the four Bell states.

So Alice has to apply one of the operations associated with the two-bit code (Bell state) she wants to send.

<img width="807" alt="Schermata 2019-06-03 alle 14 37 13" src="https://user-images.githubusercontent.com/37590676/58802319-2b42b680-860d-11e9-9043-cf4172f76c80.png">

Alice chooses to send the message '01' (applying the X gate).

She now sends the qubit to Bob and he decodes the message by applying a CNOT followed by an H gate to both qubits he has (reverse operation of entanglement).

This is the result Bob will get measuring the two qubits he has now:

<img width="695" alt="superdense_prob" src="https://user-images.githubusercontent.com/37590676/58802544-c0de4600-860d-11e9-928d-a1c97a12d183.png">

End of protocol.

This is an image of what this specific circuit looks like:


<img width="606" alt="superdense_circuit" src="https://user-images.githubusercontent.com/37590676/58802621-f08d4e00-860d-11e9-9069-d17b4fabcfa5.png">
