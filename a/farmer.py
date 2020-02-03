import tree
import sys

print('种下一棵果树。')

tree.fruit_name = sys.argv[1]

print('等啊等，树长大了，可以收获了！')

fruits = tree.harvest()

print(fruits)
