from math_func import *
import collections
import math

def test_sorted_num():
    result = sorted_num()
    assert collections.Counter(result) == collections.Counter(sorted(result, reverse=True))

def test_th_Pythagorean():
    assert th_Pythagorean(2, 10) == th_Pythagorean_automatically(2, 10)
    assert th_Pythagorean(12.4, 3.6) == th_Pythagorean_automatically(12.4, 3.6)
    assert th_Pythagorean(0.1, 1) == th_Pythagorean_automatically(0.1, 1)

def test_filter_num():
    result = filter_num()
    for item in result:
        assert item % 2 == 0

def test_map_num():
    result = map_num()
    for item in result:
        parts = item.split('+')
        assert parts[0] == parts[1]

def test_s_circle():
    assert s_circle(10) == 314.1592653589793
    assert s_circle(0) == 0
    assert s_circle(1) == math.pi