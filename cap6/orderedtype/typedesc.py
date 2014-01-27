"""Questo modulo definisce il descriptor `TypeDesc`.

La classe `TypeDesc` e' un descriptor che consente di indicare di che tipo deve 
essere un attributo di istanza. Ad esempio, consideriamo la seguente classe `Book`:

    >>> class Book:
    ...     title = TypeDesc(str, 'title')
    ...     author = TypeDesc(str, 'author')
    ...     year = TypeDesc(int, 'year')
    ...     def __init__(self, title, author, year):
    ...         self.title, self.author, self.year = title, author, year

L'attributo di istanza `title` deve essere di tipo `str`, cosi' come `author`, 
mentre `year` deve essere di tipo `int`. Quindi se chiamiamo la classe passandole 
una stringa sia come primo sia come secondo argomento, e un intero come terzo 
argomento, l'istanza viene creata correttamente:

    >>> b = Book('Programmare con Python', 'Marco Buttu', 2014)
    >>> b.year
    2014

Se invece proviamo a istanziare la classe passandole dei tipi diversi da quelli 
attesi, allora viene sollevata una eccezione di tipo `TypeError`:

    >>> b = Book('Programmare con Python', 'Marco Buttu', '2014')
    Traceback (most recent call last):
        ....
    TypeError: L'attributo `year` deve essere di tipo `int`
"""
class TypeDesc:
    def __init__(self, expected_type, name='', value=None):
        self._type, self._name, self.value = expected_type, name, value
    def __set__(self, instance, value):
        if isinstance(value, self._type):
            self.value = value
        else:
            raise TypeError("L'attributo `%s` deve essere di tipo `%s`" %(self._name, self._type.__name__))
    def __get__(self, instance, instance_type):
        return self.value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
