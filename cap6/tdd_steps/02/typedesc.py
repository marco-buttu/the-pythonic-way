class TypeDesc:
    def __init__(self, expected_type, value=None):
        self._type, self.value = expected_type, value
    def __set__(self, instance, value):
        if isinstance(value, self._type):
            self.value = value
        else:
            raise TypeError("L'attributo deve essere di tipo `%s`" %self._type.__name__)
