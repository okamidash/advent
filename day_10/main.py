import sys


def grab_input(filename):
    return set([int(line.rstrip()) for line in open(filename)])


def part_1(adapters, voltage=0, diff_1=0, diff_2=0, diff_3=0):
    if voltage + 1 in adapters:
        return part_1(adapters[1:], voltage+1, diff_1+1, diff_2, diff_3)
    elif voltage + 2 in adapters:
        return part_1(adapters[1:], voltage+2, diff_1, diff_2+1, diff_3)
    elif voltage + 3 in adapters:
        return part_1(adapters[1:], voltage+3, diff_1, diff_2, diff_3+1)
    else:
        return diff_1 * (diff_3 + 1)


# Stack is a list of possible permeatations
def part_2(adapters, final_adapter, voltage=0, stack={}, total=0):
    if voltage == final_adapter:
        return 1
    for voltage_n in range(1, 4):
        if voltage_n + voltage in adapters:
            total += part_2(adapters, final_adapter, voltage_n + voltage)
    return total


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    adapters = sorted(grab_input('test_input.txt'))
    # part_1(adapters)
    final_adapter = adapters[-1] + 3
    print(final_adapter)
    print(part_2(adapters, final_adapter))
