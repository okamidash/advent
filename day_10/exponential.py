#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def grab_input(filename):
    return set([int(line.rstrip()) for line in open(filename)])


if __name__ == '__main__':
    lines = sorted(grab_input('test_input.txt'))
    sol = {0: 1}
    for line in lines:
        sol[line] = 0
        if line - 1 in lines:
            sol[line] += sol[line - 1]
        if line - 2 in lines:
            sol[line] += sol[line - 2]
        if line - 3 in lines:
            sol[line] += sol[line - 3]

    print(sol)
