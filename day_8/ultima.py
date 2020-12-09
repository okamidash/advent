# Hashmap
# acc = 97
# jmp = 106
# nop = 110
import time


def prepare(filename):
    instructions = []
    for line in open(filename):
        split_ins = line.rstrip().split(' ')
        opp, ins = int(ord(split_ins[0][0])), int(split_ins[1])
        instructions.append((opp, ins))
    instructions_length = len(instructions)

    return instructions, instructions_length


def part_2():
    for looping_stack_index in range(len(looping_stack)-1, -1, -1):
        # Set the position to continue the search from
        position = looping_stack[looping_stack_index]
        # Set the accumulator
        accumulator = accumulator_stack[looping_stack_index]
        # Pull the stack trace up to this point
        stack_trace = looping_stack[0:looping_stack_index]
        # Pull the accumulator trace up to this point
        accumulator_trace = accumulator_stack[0:looping_stack_index]
        # Find the fix
        if instructions[position][0] != 97:
            attempted_fix = recurse(instructions, instructions_length, stack_trace, position, accumulator, accumulator_trace, True)
            if attempted_fix[3] == instructions_length:
                return attempted_fix[2]


def recurse(instructions, instructions_length, stack=[], position=0, accumulator=0, accumulator_stack=[], force_operation=False):
    if position == instructions_length:
        return stack, accumulator_stack, accumulator, position
    if position in stack:
        return stack, accumulator_stack, accumulator, position
    # Lets discover the loop first
    operation, value = instructions[position]
    if force_operation:
        if operation == 106:
            operation = 110
        elif operation == 110:
            operation = 106

    stack.append(position)
    accumulator_stack.append(accumulator)
    # Handle operations
    if operation == 97:
        # Handle increasing the Accumulator
        accumulator += value
        position += 1
    elif operation == 106:
        # Handle jumping to the next instruction
        position += value
    elif operation == 110:
        position += 1

    return recurse(instructions, instructions_length, stack, position, accumulator, accumulator_stack)


if __name__ == '__main__':
    time_total = 0
    test_count = 1000
    instructions, instructions_length = prepare('vessInput.txt')
    for temp_step in range(test_count):
        time_before = time.time()
        looping_stack, accumulator_stack, final_accumulator, position = recurse(instructions, instructions_length)
        part_2()
        time_total += time.time() - time_before
    print(test_count, "trials took", time_total / test_count)

    # Part 1
    print(final_accumulator)
    print(part_2())
