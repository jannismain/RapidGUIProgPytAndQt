# encoding: utf-8

count = 10
while count != 0:
    print(count, end=', ')
    count -= 1
print('Ende\n')

for char in 'aeiou':
    print("{}={}".format(char, ord(char)))
else:
    print()

for i in range(0, 90, 3):
    print(i, end=', ')
else:
    print('Ende')
