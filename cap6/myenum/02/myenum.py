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
                attr = cls(name, value)
                setattr(cls, name, attr) 
                members[name] = attr
        setattr(cls, '__members__', types.MappingProxyType(members))
        return cls

class MyEnum(metaclass=MyEnumMeta):
    def __init__(self, name, value):
        self.name = name
        self.value = value

