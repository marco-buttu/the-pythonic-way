import unittest
from orderedtypemeta import OrderedTypeMeta
from typedesc import TypeDesc
        
class TestBook(unittest.TestCase):
    def setUp(self):
        class Book(metaclass=OrderedTypeMeta):
            title = TypeDesc(str)
            author = TypeDesc(str)
            year = TypeDesc(int)
            def __init__(self, title, author, year):
                self.title, self.author, self.year = title, author, year
        self.Book = Book
        self.b = Book('Programmare con Python', 'Marco Buttu', 2014)
    def test_order(self):
        """Verifica che l'attributo Book._order sia una lista ordinata come da attese."""
        self.assertListEqual(self.Book._order, ['title', 'author', 'year'])
    def test_exceptmessage(self):
        """Verifica che il nome dell'attributo sia corretto."""
        self.assertRaisesRegex(TypeError, 'year', setattr, self.b, 'year', str(self.b.year))

if __name__ == '__main__':
    unittest.main()

