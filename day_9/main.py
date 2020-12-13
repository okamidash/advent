import time
import sys


def read(filename):
    return [int(line.rstrip()) for line in open(filename)]


def iteration_search(current_number, current_range, preamble):
    iteration = 0
    while True:
        if iteration == len(current_range):
            return current_number

        if current_number - current_range[iteration] not in current_range:
            del current_range[iteration]
        else:
            return True
    return current_number


def part_1(stack, preamble):
    for index in range(preamble, len(stack)):
        current_number = stack[index]
        current_range = stack[index - preamble: index]
        search_result = iteration_search(current_number, current_range, preamble)
        if search_result is not True:
            return current_number


def part_2(stack, desired_number):
    return recurse(stack, 0, 1, desired_number)


def recurse(stack, window_start, window_end, desired_number):
    current_number = sum(stack[window_start:window_end])
    if current_number == desired_number:
        return stack[window_start:window_end]
    if current_number > desired_number:
        return recurse(stack, window_start + 1, window_end, desired_number)
    elif current_number < desired_number:
        return recurse(stack, window_start, window_end + 1, desired_number)


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    stack = read('input.txt')
    time_total = 0
    test_count = 1000
    for temp_step in range(test_count):
        time_before = time.time()
        # PART ONE SOLUITON
        desired_number = part_1(stack, 25)
        # PART TWO SOLUTION
        unsorted_stack = part_2(stack, 393911906)
        sorted_stack = sorted(unsorted_stack)
        part_2_ret = sorted_stack[0] + sorted_stack[-1]
        time_total += time.time() - time_before
    print(part_2_ret)
    print(test_count, "trials took", time_total / test_count)
