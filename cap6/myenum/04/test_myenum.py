import unittest
from myenum import *
        
class TestPasta(unittest.TestCase):
    def setUp(self):
        class Pasta(MyEnum):
            spaghetti = 1
            lasagne = 2
            tagliatelle = 3
        self.Pasta = Pasta
    def test_membersOrder(self):
        """Verifica che i membri siano ordinati secondo l'ordine di definizione."""
        self.assertListEqual(['spaghetti', 'lasagne', 'tagliatelle'], list(self.Pasta.__members__))
    def test_isInstance(self):
        """Verifica che i membri siano istanze della classe Pasta."""
        for member in self.Pasta.__members__.values():
            self.assertIsInstance(member, self.Pasta)
    def test_memberAttributes(self):
        """Verifica che gli attributi name e value dei membri siano corretti."""
        self.assertEqual(self.Pasta.spaghetti.name, 'spaghetti')
        self.assertEqual(self.Pasta.spaghetti.value, 1)
    def test_noHomonym(self):
        """Verifica che non vi siano membri con lo stesso nome."""
        namespace = Namespace({'spaghetti': 1})
        self.assertRaises(KeyError, namespace.update, {'spaghetti': 1})
    def test_doNotChange(self):
        """Verifica che i membri non possano essere ne' riassegnati ne' cancellati."""
        self.assertRaises(AttributeError, setattr, self.Pasta, 'spaghetti', 2)
        self.assertRaises(AttributeError, delattr, self.Pasta, 'spaghetti')
    def test_aliases(self):
        """Verifica che un membro con stesso valore di uno esistente sia un alias."""
        class Pasta(MyEnum):
            spaghetti = 1
            lasagne = 2
            tagliatelle = 1
        self.assertIs(Pasta.spaghetti, Pasta.tagliatelle) 

if __name__ == '__main__':
    unittest.main()

