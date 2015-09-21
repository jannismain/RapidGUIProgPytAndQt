#!/usr/bin/env python3
#coding: utf-8

import decimal
from PyQt4.QtGui import *
from PyQt4.QtCore import *

print("Hello World")

x = 71 # Java: Integer x = new Integer(71)
# x = object reference
x += 9
y = 'Dove'

d = decimal.Decimal('5.1')
f = float(d)
c = 5.5+0.8j
print(repr(d), repr(f))
print(type(c))

euro = chr(8364)
print(euro + ' Ord:' + repr(ord(euro)))

author = 'the lazy fox'
print(author[1])
print(author[-1])
print('His Name is "{}, {}"'.format(author[4:], author[:3])) # 'lazy fox, the'
title = author.replace('lazy', 'awesome').title()
print('{} - {}'.format(title.upper(), author.upper()))
a, b, c = title.split()
print(c, a, b)

pets = ('tiger', 'mathilda', 'non-scary shower-spider', 'else')
print(pets[:], len(pets))
my_pets = list(pets)

my_pets.reverse()
my_pets.sort()
my_pets[3:] = []
print(my_pets)

"""
Shallow Copying (commonly '=')
a = ['1', '2']
b = a
Deep Copying (commony '.copy()', 'deepcopy()')
a = ['1', '2']
b = a[:]
"""

"""
==  Value Comparison
is  Identity Comparison (object.id())
"""

"""
Python Keywords:
and    as   assert  break   class   continue    def     del
elif   else except  exec    finally for         from    global
if  import  in  is  lambda  not or  pass    print   raise   return
try while   with    yield
"""

"""
Built-in Collection types
tuple       immutable
list          mutable
dict          mutable
set           mutable
frozenset   immutable
"""