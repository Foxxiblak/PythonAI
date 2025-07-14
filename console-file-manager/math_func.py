import math
import random

def generate_num_list():
    '''
    :return: последовательность целых чисел от 1 до 100, состаящая из 10 элементов
    '''
    return [random.randint(1, 100) for i in range(1, 10)]

def sorted_num():
    '''
    :return: список чисел отсортированный по убыванию
    '''
    return sorted(generate_num_list(), reverse=True)

def filter_num():
    '''
    :return: список четных чисел
    '''
    return list(filter(lambda x: x % 2 == 0, generate_num_list()))

def map_num():
    '''
    :return: список строк формата N+N
    '''
    return list(map(lambda x: str(x) + '+' + str(x), generate_num_list()))

def s_circle(r):
    '''
    :param r: радиус круга
    :return: площадь круга
    '''
    return math.pi * r ** 2

def th_Pythagorean(a, b):
    '''
    :param a: 1 катет
    :param b: 2 катет
    :return: гипотенуза
    '''
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

def th_Pythagorean_automatically(a, b):
    '''
    :param a: 1 катет
    :param b: 2 катет
    :return: гипотенуза
    '''
    return math.hypot(a, b)

if __name__ == '__main__':
    sorted_num()
    filter_num()
    map_num()
    s_circle(10)
    th_Pythagorean(2, 5)
    th_Pythagorean_automatically(2, 5)