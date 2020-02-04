letters = (item for item in 'abc')

for item in letters:
    print(item)

letters2 = (item*2 for item in [1, 3, 4])

for item in letters2:
    print(item)

letters3 = (item*2 for item in [11, 33, 44])

print(next(letters3))
print(next(letters3))
print(next(letters3))

