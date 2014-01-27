"""Questo modulo consente di creare delle enumerazioni.

Una enumerazione e' una classe che eredita da `MyEnum`. Ad esempio, la seguente
classe `Pasta` e' una enumerazione:

    >>> class Pasta(MyEnum):
    ...     spaghetti = 1
    ...     lasagne = 2
    ...     tagliatelle = 3

Gli attributi di classe `Pasta.spaghetti`, `Pasta.lasagne` e `Pasta.tagliatelle`
sono detti membri. Questi  sono istanze di `Pasta`, ed hanno un nome e un valore:

    >>> isinstance(Pasta.spaghetti, Pasta)
    True
    >>> Pasta.lasagne.name
    'lasagne'
    >>> Pasta.lasagne.value
    2

I membri non possono essere riassegnati:

    >>> Pasta.tagliatelle = 1
    Traceback (most recent call last):
        ...
    AttributeError: Non si possono riassegnare i membri
"""
import types
from collections import OrderedDict


class Namespace(OrderedDict):
    def __setitem__(self, name, value):
        if name in self:
            raise KeyError("Un attributo di nome `%s` esiste gia'" %name)
        else:
            super().__setitem__(name, value)

class MyEnumMeta(type):
    def __prepare__(clsname, bases):
        return Namespace()
    def __new__(metacls, clsname, bases, namespace, *args, **kwargs):
        cls = super().__new__(metacls, clsname, bases, namespace)
        members = OrderedDict()
        for name, value in namespace.items():
            if not name.startswith('__') and not name.endswith('__'):
                for member in members.values():
                    if member.value == value:
                        attr = member
                        break
                else:
                    attr = cls(name, value)
                setattr(cls, name, attr) 
                members[name] = attr
        setattr(cls, '__members__', types.MappingProxyType(members))
        return cls
    def __setattr__(self, name, value):
        if hasattr(self, name) and isinstance(getattr(self, name), self):
            raise AttributeError('Non si possono riassegnare i membri')
        else:
            super().__setattr__(name, value)
    def __delattr__(self, name):
        if hasattr(self, name) and isinstance(getattr(self, name), self):
            raise AttributeError('Non si possono cancellare i membri')
        else:
            super().__delattr__(name)
    def __iter__(self):
        unique_members = []
        for member in self.__members__.values():
            if not member in unique_members:
                unique_members.append(member)
        return iter(unique_members)
    def __getitem__(self, name):
        for member in self:
            if member.name == name:
                return member
        raise KeyError('Un membro con questo nome non esiste')
    def __call__(self, *args, **kwargs):
        if len(args) == 1:
            for member in self:
                if member.value == args[0]:
                    return member
            raise ValueError('Un membro con questo valore non esiste')
        else:
            return super().__call__(*args, **kwargs)
    
class MyEnum(metaclass=MyEnumMeta):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return '%s.%s' %(type(self).__name__, self.name)
    def __repr__(self):
        return '<%s.%s: %s>' %(type(self).__name__, self.name, self.value)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
