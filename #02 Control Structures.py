# encoding: utf-8
import sys


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
print()

# List Comprehensions
fives = [x for x in range(50) if x % 5 == 0]  # Erzeugt eine Liste
print(type(fives))
# ist identisch zu
# fives = []
# for x in range(50):
#     if x % 5 == 0:
#         fives.append(x)
# # fives = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
fives = (x for x in range(50) if x % 5 == 0)  # Erzeugt einen Generator
print(type(fives))
print()


def frange(arg0, arg1=None, arg2=None):
    start = 0.0
    inc = 1.0
    if arg2 is not None:  # 3 Argumente
        start = arg0
        stop = arg1
        inc = arg2
    elif arg1 is not None:  # 2 Argumente
        start = arg0
        inc = arg1
    else:  # 1 Argument
        stop = arg0
    result = []
    # Generator-Functions (Speichereffizient!)
    while start < (stop - (inc / 2)):
        yield start
        start += inc
    # ist identisch zu
    # while start < (stop - (inc/2)):
    #     result.append(round(start, 2))
    #     start += inc
    else:
        if start == stop:
            yield stop
    return result


print(list(frange(0, 5, 0.25)))


def simplify(text, delete=''):
    result = []
    word = []
    for char in text:
        if char in delete:
            continue
        elif char.isspace():
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    if word:
        result.append(word)
    return ' '.join(result)


cube = lambda x: pow(x, 3)
print(cube(16))
print()


def action(arg0):
    print('You pressed Button {}'.format(arg0))


# Abwärtskompatibilität sichern
if sys.version_info[:2] < (2, 5):
    def partial(func, arg):
        def callme():
            return func(arg)

        return callme
else:
    from functools import partial

buttonOneFunc = partial(action, 'One')
buttonTwoFunc = partial(action, 'Two')

buttonOneFunc()

# # Exceptions
# Testing for errors
# result = ''
# i = text.find('<')
# if i > -1:
#     j = text.find('>', i + 1)
#     if j > -1:
#         result = text[i:j +1]
# print(result)
# # Proper Exception Handling
# try:
#     i = text.index('<')
#     j = text.index('>', i+1)
#     result = text[i:j + 1]
# except ValueError:
#     result = ''
# print(result)

# Exceptions um aus verschachtelten Schleifen auszubrechen
# Manuelle Fehlerbehandlung
grid = [[[1], [2]], [[2], [3]], [[4], [1]]]


def search(grid, target):
    # print(repr(grid))
    # found = False
    # for x in range(len(grid)):
    #     for y in range(len(grid[x])):
    #         for z in range(len(grid[x][y])):
    #             if grid[x][y][z] == target:
    #                 found = True
    #                 break
    #         if found:
    #             break
    #     if found:
    #         break
    # if found:
    #     print('Found at ({}, {}, {})'.format(x, y, z))
    # else:
    #     print('Not found')
    # Elegante Fehlerbehandlung
    class FoundException(Exception):
        pass

    try:
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                for z in range(len(grid[x][y])):
                    if grid[x][y][z] == target:
                        raise (FoundException)
    except FoundException:
        print('Found at ({}, {}, {})'.format(x, y, z))
    else:
        print('Not found')


search(grid, 4)


# # EXERCISES
#   1. valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    result = ''
    for char in text:
        if char in chars:
            result += char
    return result


print(valid("Barking!"))
print(valid("KL754", "0123456789"))
print(valid('BEAN', "abcdefghijklmnopqrstuvwxyz"))


#   2. charcount(text)
def charcount(text):
    dict = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        dict[char] = 0
    dict['whitespace'] = 0
    dict['others'] = 0
    for char in text.lower():
        if char.isalpha():
            dict[char] += 1
        elif char.isspace():
            dict['whitespace'] += 1
        else:
            dict['others'] += 1
    return dict


print(charcount('Exceedingly Edible'))


#   3. integer(number)
def integer(number):
    try:
        return int(round(float(number), 0))
    except ValueError:
        return 0


print(integer("23"))
print(integer(4.5))
print(integer(32))
print(integer(-15.1))
print(integer("tonsils"))


#   4. incrementString(text="AAAA")
def incrementString(text="AAAA"):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = list(text)
    result = []
    carry = 0

    def add(char, carry):
        index = alphabet.find(char)
        print(index)
        if index < 0:
            raise (ValueError)
        elif index + carry < 25:
            return (alphabet[index + carry + 1], 0)
        elif index + carry == 25:
            return (alphabet[0], 1)

    for i in chars:
        try:
            letter, carry = add(i, carry)
            result.append(letter)
            if carry == 1:
                chars.append('A')
        except ValueError:
            print("False Input!")
    return str(result)


print(incrementString('A'))
print(incrementString('Z'))


#   5. leapyears(yearlist)
def leapyear(yearlist):
    for y in yearlist:
        if y % 4 == 0:
            if y % 100 == 0 and not y % 400 == 0:
                continue
            yield y


print()
l = leapyear([1600, 1601, 1602, 1603, 1604, 1800])
for y in l: print(y)
