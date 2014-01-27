import unittest
from typedesc import TypeDesc
        
class TestBook(unittest.TestCase):
    def setUp(self):
        class Book:
            title = TypeDesc(str, 'title')
            author = TypeDesc(str, 'author')
            year = TypeDesc(int, 'year')
            def __init__(self, title, author, year):
                self.title, self.author, self.year = title, author, year
        self.Book = Book
        self.b = Book('Programmare con Python', 'Marco Buttu', 2014)
    def test_creation(self):
        """Verifica che durante la creazione venga sollevata una eccezione di tipo TypeError."""
        self.assertRaises(TypeError, self.Book, self.b.title, self.b.author, str(self.b.year))
    def test_setting(self):
        """Verifica che dopo la creazione gli assegnamenti avvengano in modo corretto."""
        title = 'I principi della matematica'
        author = 'Bertrand Russell'
        year = 1903
        self.b.title = title
        self.b.author = author
        self.b.year = year
        self.assertEqual(self.b.title, title)
        self.assertEqual(self.b.author, author)
        self.assertEqual(self.b.year, year)
    def test_wrongsetting(self):
        """Verifica che dopo la creazione un assegnamento errato sollevati una TypeError."""
        self.assertRaises(TypeError, setattr, self.b, 'title', [self.b.title])
        self.assertRaises(TypeError, setattr, self.b, 'author', [self.b.author])
        self.assertRaises(TypeError, setattr, self.b, 'year', str(self.b.year))
    def test_exceptmessage(self):
        """Verifica che il nome dell'attributo sia corretto."""
        self.assertRaisesRegex(TypeError, 'year', setattr, self.b, 'year', str(self.b.year))

if __name__ == '__main__':
    unittest.main()

