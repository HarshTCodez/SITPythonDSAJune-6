class Animal:
    def __init__(self, data):
        self.__data = data
        self._data = data


a = Animal(123)
# print(a.__data)
# print(a._data)
