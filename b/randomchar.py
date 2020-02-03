import random


class RandomChar:
    def __init__(self):
        self.all_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.all_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self.all_digits = '0123456789'
        self.all_specials = '~!@#$%^&*'

    @staticmethod
    def pick_random_item(sequence):
        random_int = random.randint(0, len(sequence) - 1)
        # 调用 random.randint() 生成一个随机数字作为索引去字符串中取值，因为随机生成的数字不可超过字符串长度，所以取值范围为 0, len(sequence) - 1。
        return sequence[random_int]

    def uppercase(self):
        return self.pick_random_item(self.all_uppercase)  # 调用 pick_random_item 随机从 all_uppercase 字符串中取出一个大写字母

    def lowercase(self):
        return self.pick_random_item(self.all_lowercase)  # 调用 pick_random_item 随机从 all_lowercase 字符串中取出一个小写字母

    def digit(self):
        return self.pick_random_item(self.all_digits)     # 调用 pick_random_item 随机从 all_digits 字符串中取出一个数字

    def special(self):
        return self.pick_random_item(self.all_specials)   # 调用 pick_random_item 随机从 all_specials 字符串中取出一个特殊字符

    def anyone(self):
        # 将四种字符拼接在一起，形成一个大字符串 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*'，
        # 然后调用 pick_random_item 方法从中随机取出一个字符。
        return self.pick_random_item(self.all_uppercase + self.all_lowercase + self.all_digits + self.all_specials)
