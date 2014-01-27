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
