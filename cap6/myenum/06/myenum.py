import types
from collections import OrderedDict

class Iterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.index += 1
            return self.wrapped[self.index]
        except IndexError:
            raise StopIteration('Iterazione conclusa')

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
        return Iterator(unique_members)
    def __getitem__(self, name):
        for member in self:
            if member.name == name:
                return member
        raise KeyError('Un membro con questo nome non esiste')


class MyEnum(metaclass=MyEnumMeta):
    def __init__(self, name, value):
        self.name = name
        self.value = value

