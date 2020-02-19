def a():
    x = 2

    def show():
        return x

    def add():
        nonlocal x
        x += 1

    return show, add


show1, add1 = a()

print(show1())
add1()

print(show1())
