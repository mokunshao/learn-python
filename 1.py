class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('hello, my name is ' + self.name)


jack = Human('jack', 'male')

jack.speak()
