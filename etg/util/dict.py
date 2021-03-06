"""
A set of utility functions for working with dictionaries
"""
import copy

def difference(first, other, epsilon=0.005):
    """
    Calculate the difference between two dictionaries. The difference is
    defined as all the values for the keys that are in both ``dict`` and
    ``other`` which differ. For floating point numbers, the value ``epsilon``
    is used to define difference, so two floating point values are seen as
    different if their difference is larger than ``epsilon``.

    :param dict first: The first dictionary to calculate the difference for.
    :param dict other: The other dictionary to calculate the difference for.
    :param float epsilon: The smallest difference between two floating point \
    numbers that we differentiate between
    :return: A dictionary where each key is a value where ``dict`` and ``other`` \
    differ and each value is the value from ``other``.
    :rtype: dict
    """
    ret = {}
    dict_keys = set(first.keys())
    other_keys = set(other.keys())
    for key in dict_keys.intersection(other_keys):
        try:
            if abs(first[key] - other[key]) >= epsilon:
                ret[key] = other[key]
        except TypeError:
            if first[key] != other[key]:
                ret[key] = other[key]
    return ret

def merge(one, two):
    """
    Merge two dictionaries with dictionaries in them. Keys that occur in both are taken from the
    second argument.
    """
    ret = copy.copy(one)
    for key in two:
        if key in one:
            if isinstance(one[key], dict) and isinstance(two[key], dict):
                ret[key] = merge(one[key], two[key])
            else:
                ret[key] = two[key]
        else:
            ret[key] = two[key]
    return ret
