import unittest
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quantum_layer import QuantumLayer

class TestQuantumLayer(unittest.TestCase):
    def setUp(self):
        self.quantum_layer = QuantumLayer()
        self.test_data = [1, 2, 3, 4]

    def test_initialize_qubits(self):
        n_qubits = 3
        self.quantum_layer.initialize_qubits(n_qubits)
        self.assertEqual(self.quantum_layer.n_qubits, n_qubits)
        self.assertEqual(len(self.quantum_layer.state), 2**n_qubits)
        self.assertEqual(self.quantum_layer.state[0], 1.0)

    def test_simulate_superposition(self):
        result = self.quantum_layer.simulate_superposition(self.test_data)
        self.assertEqual(len(result), len(self.test_data))
        self.assertTrue(all(isinstance(x, (int, float)) for x in result))

    def test_simulate_entanglement(self):
        data2 = [5, 6, 7, 8]
        result = self.quantum_layer.simulate_entanglement(self.test_data, data2)
        self.assertEqual(len(result), len(self.test_data))
        expected = [a * b for a, b in zip(self.test_data, data2)]
        self.assertEqual(result, expected)

    def test_invalid_input_superposition(self):
        with self.assertRaises(TypeError):
            self.quantum_layer.simulate_superposition("invalid input")

    def test_invalid_input_entanglement(self):
        with self.assertRaises(ValueError):
            self.quantum_layer.simulate_entanglement([1, 2], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
