import unittest
from adder import adder

class AdderTest(unittest.TestCase):
    def test_addition(self):
        """Verifica che adder() esegua correttamente la somma."""
        self.assertEqual(['a', 'b'], adder(['a'], ['b']))
        self.assertEqual(3, adder(1, 2))
        self.assertEqual('python3', adder('python', '3'))
    def test_exception(self):
        """Verifica che adder() sollevi una eccezione quando la somma non è supportata."""
        self.assertRaises(TypeError, adder, 1, '2')

if __name__ == '__main__':
    unittest.main()
