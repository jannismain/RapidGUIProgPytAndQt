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
    print('Ende\n')

presidents = dict(Washington=(1789, 1797), Adams=(1797, 1801), Jefferson=(1801, 1809), Madison=(1809, 1817))

for key in sorted(presidents):
    print('{}: {}-{}'.format(key, presidents[key][0], presidents[key][1]))
else:
    print()

def invert_bits_recursive(b):
    if b=='0':
        return '1'
    elif b=='1':
        return '0'
    else:
        mid = len(b)//2
        return invert_bits_recursive(b[:mid]) + invert_bits_recursive(b[mid:])

def swap_bits(b):
    res = ''
    for n in range(len(b)):
        res += b[-n-1]
    return res


byte = '1000000000'
byte_inv = invert_bits_recursive(byte)
byte_swa = swap_bits(byte)
print(byte_inv)
print(byte_swa)