def power_of_two():
    for exponent in range(11):
        yield 2 ** exponent


p = power_of_two()

print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

print('----')

p2 = power_of_two()

for item in p2:
    print(item)
