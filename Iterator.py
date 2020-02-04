class PowerOfTwo:
    def __init__(self):
        self.exponent = 0  					# 将每次的指数记录下来

    def __next__(self):
        if self.exponent > 10:
            raise StopIteration
        else:
            result = 2 ** self.exponent		# 以 2 为底数求指数幂
            self.exponent += 1
            return result

    def __iter__(self):
        return self


p = PowerOfTwo()

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

print('-----')

p2 = PowerOfTwo()

for item in p2:
    print(item)

