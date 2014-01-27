"""Questo modulo definisce la metaclasse `OrderedTypeMeta`.

Se una generica classe `Foo` ha come metaclasse `OrderedTypeMeta`, allora `Foo` 
ha un attributo `_order` che fa riferimento ad una lista contenente gli attributi 
di `Foo` di tipo `TypeDesc`, ordinati secondo l'ordine con cui sono definiti nella
istruzione class:

    >>> class Foo(metaclass=OrderedTypeMeta):
    ...     c = TypeDesc(int)
    ...     x = TypeDesc(str)
    ...     a = TypeDesc(int)
    ...     m = TypeDesc(list)
    ... 
    >>> Foo._order
    ['c', 'x', 'a', 'm']

Inoltre, il descriptor `TypeDesc` fa si che agli attributi di istanza possano essere
assegnati solamente istanze del tipo passato a `TypeDesc`:

    >>> f = Foo()
    >>> f.c = 'python' # Errore: posso assegnare solamente degli interi
    Traceback (most recent call last):
        ...
    TypeError: L'attributo `c` deve essere di tipo `int`
"""
from collections import OrderedDict
from typedesc import TypeDesc

class OrderedTypeMeta(type):
    def __prepare__(clsname, bases):
        return OrderedDict(_order=[])
    def __new__(metacls, clsname, bases, namespace):
        for key, value in ((k, v) for k, v in namespace.items()):
            if isinstance(value, TypeDesc):
                value._name = key
                namespace['_order'].append(value._name)
        return super().__new__(metacls, clsname, bases, namespace)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
