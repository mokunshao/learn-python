def say_hello(name: str):
    print(name, ', hello!')


say_hello('mike')


def say_hello2(name: str) -> str:
    word = 'hello, ' + name
    return word


print(say_hello2('mike'))
