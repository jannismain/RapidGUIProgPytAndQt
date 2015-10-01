# encoding: utf-8

import random
import bisect


class Chair(object):
    """This class represents chairs"""

    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs


class Reichtangle(object):
    """This class resembles Reichtangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def _get_area(self):
        return round(self.width * self.height, 2)

    def _set_area(self, area):
        self.set_width(random.random() * area)
        self.set_height(area / self.get_width())

    area = property(fget=_get_area, fset=_set_area)


class OrderedDict(object):
    def __init__(self, dictionary=None):
        self.__keys = []
        self.dict = {}
        if dictionary is not None:
            if isinstance(dictionary, OrderedDict):
                self.__dict = dictionary.__dict.copy()
                self.__keys = dictionary.__keys[:]
            else:
                self.__dict = dict(dictionary).copy()
                self.__keys = sorted(self.__dict.keys())

    def get(self, key, value=None):
        """Returns the value associated with key or value if key isn't
        in the dictionary
        >>> d = OrderedDict(dict(s=1, a=2, n=3, i=4, t=5, y=6))
        >>> d.get("X", 21)
        21
        >>> d.get("i")
        4
        """
        return self.__dict.get(key, value)

    def get_at(self, index):
        return self.__dict[self.__keys[index]]

    def set_at(self, index, value):
        self.__dict[self.__keys[index]] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        if key not in self.__dict:
            bisect.insort_left(self.__keys, key)
        self.__dict[key] = value

    def __delitem__(self, key):
        i = bisect.bisect_left(self.__keys, key)
        del self.__keys[i]
        del self.__dict[key]


class Tribool(object):
    def __init__(self, value=None):
        self.__value = None
        if value is not None:
            self.__value = bool(value)

    def __str__(self):
        return str(self.__value)

    def __hash__(self):
        return super(Tribool, self).__hash__()

    def __eq__(self, other):
        """
        >>> a = Tribool()
        >>> b = Tribool(True)
        >>> c = Tribool(False)
        >>> a < b
        True
        >>> a < c
        True
        >>> b = Tribool(True)
        True
        >>> a < c < b
        True
        >>> b > c
        :param other:
        :return:
        """
        return self.__value == other.__value

    def __repr__(self):
        return "Tribool({})".format(self.__value)

    def __cmp__(self, other):
        pass


def main():
    my_chair = Chair("Hvalla", 5)
    print(my_chair, my_chair.name, str(my_chair.legs))
    print()
    my_reichtangle = Reichtangle(20, 5)
    print('Fläche: ' + str(my_reichtangle.area))
    my_reichtangle.area = 100
    print('Höhe: {}, Breite {}'.format(my_reichtangle.height, my_reichtangle.width))
    print('Neue Fläche: ' + str(my_reichtangle.area))


main()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
