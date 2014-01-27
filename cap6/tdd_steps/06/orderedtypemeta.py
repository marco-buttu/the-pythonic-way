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
