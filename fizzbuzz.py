#!/bin/python
# -*- coding: UTF-8 -*-
import sys


def fizzbuzz(n):
    try:
        num = int(n)
    except ValueError:
        print("%s is not a number, please input a positive interger!" % n)
        return
    if num <= 0:
        print("%s is not  a positive interger!" % num)
        return
    result = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizz buzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result


def main():
    n = raw_input('Please input a positive integer: ')
    result = fizzbuzz(n)
    if result:
        print(result)


if __name__ == '__main__':
    main()
