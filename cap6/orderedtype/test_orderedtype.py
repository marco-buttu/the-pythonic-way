import unittest
from orderedtypemeta import OrderedTypeMeta
from typedesc import TypeDesc
        
class TestBook(unittest.TestCase):
    def setUp(self):
        class Book(metaclass=OrderedTypeMeta):
            title = TypeDesc(str)
            author = TypeDesc(str)
            year = TypeDesc(int)
        self.Book = Book
    def test_order(self):
        """Verifica che l'attributo Book._order sia una lista ordinata come da attese."""
        self.assertListEqual(self.Book._order, ['title', 'author', 'year'])

if __name__ == '__main__':
    unittest.main()

