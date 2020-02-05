letters = (item for item in 'abc')

for item in letters:
    print(item)

print('---')

letters2 = (item*2 for item in [1, 3, 4])

for item in letters2:
    print(item)

print('---')

letters3 = (item*2 for item in range(0, 10))

print(next(letters3))
print(next(letters3))
print(next(letters3))
print(next(letters3))
print(next(letters3))
print(next(letters3))
print(next(letters3))
print(next(letters3))

