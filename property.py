class A:
    def __init__(self, name):
        self._apple = name

    @property
    def apple(self):
        return self._apple

    @apple.setter
    def apple(self, value):
        self._apple = value


a = A('ok')
print(a.apple)
a.apple = 'yes'
print(a.apple)
