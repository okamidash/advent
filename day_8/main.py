import time


def part_1():
    instructions = []
    for line in open('input.txt'):
        split_ins = line.rstrip().split(' ')
        opp, ins = split_ins[0], int(split_ins[1])
        instructions.append((opp, ins, False))
    accumulator = 0
    ins_iter = 0
    while True:
        # Evaluate the instruction
        opp, ins, chk = instructions[ins_iter]

        # Check if we have traversed this path before
        if chk is False:
            instructions[ins_iter] = (opp, ins, True)
        else:
            return accumulator
        # Evaluate the action
        if opp == 'nop':
            ins_iter += 1
        elif opp == 'jmp':
            ins_iter += ins
        elif opp == 'acc':
            ins_iter += 1
            accumulator += ins


def part_2():
    instructions = []
    for line in open('input.txt'):
        split_ins = line.rstrip().split(' ')
        opp, ins = split_ins[0], int(split_ins[1])
        instructions.append((opp, ins))
    instructions_length = len(instructions)
    looping_stack = discover(instructions, instructions_length)
    for index in range(len(looping_stack) - 1, -1, -1):
        position = looping_stack[index]
        operation, value = instructions[position]
        ret = 0
        if operation == 'acc':
            pass
            #print("nothing to be done here")
        elif operation == 'jmp':
            operator = 'nop'
            ret = iterate(instructions, instructions_length, position, operator, looping_stack[0:index + 1])
        elif operation == 'nop':
            operator = 'jmp'
            ret = iterate(instructions, instructions_length, position, operator, looping_stack[0:index + 1])
        if ret is True:
            operation, value = instructions[position]
            instructions[position] = (operator, value)
            break
    #print("Found that to break the loop you must exit at position", position)
    construct(instructions, instructions_length)


def construct(instructions, instructions_length):
    ins_iter = 0
    accumulator = 0
    while True:
        if ins_iter == instructions_length:
            return accumulator
        # Evaluate the instruction
        opp, ins = instructions[ins_iter]

        # Evaluate the action
        if opp == 'nop':
            ins_iter += 1
        elif opp == 'jmp':
            ins_iter += ins
        elif opp == 'acc':
            ins_iter += 1
            accumulator += ins


def discover(instructions, instructions_length):
    stack_trace = []
    position = 0
    while True:

        # Evaluate the instruction
        operation, value = instructions[position]
        # Check if we have traversed this path before
        if position in stack_trace:
            return stack_trace
        else:
            stack_trace.append(position)
        # Evaluate the action
        position, dispose = eval_nx(operation, position, value)


def iterate(instructions, instructions_length, position, operator, stack_trace):
    stack_trace = []
    while True:
        if position == instructions_length:
            return True

        # Evaluate the instruction
        operation, value = instructions[position]
        if operator != 0:
            operation = operator
            operator = 0

        # Check if we have traversed this path before
        if position in stack_trace:
            return False
        else:
            stack_trace.append(position)
        # Evaluate the action
        position, dispose = eval_nx(operation, position, value)


def printy(instructions, position):
    for idx, line in enumerate(instructions):
        if idx == position:
            print(f"|X| {line[0]} {line[1]}")
        else:
            print(f"| | {line[0]} {line[1]}")
    print('-----------------')
# def recurse(instructions, instructions_length: int, position=0, accumulator=0, stack_trace=[], changed=0):
#     print(position)
#     # Evaluate if the position is at the end of the loop
#     if position - 1 == instructions_length:
#         print("Reached end of list")
#         return changed
#     if position in stack_trace:
#         return False
#     else:
#         stack_trace.append(position)
#
#     # Pull the value for the instruction at the CURRENT position
#     operation, value = instructions[position]
#     next_position, next_accumulator = eval_nx(operation, position, value, accumulator)
#
#     recursion_result = recurse(instructions, instructions_length, next_position, next_accumulator, stack_trace, changed)
#     # Attempt to pop
#     if recursion_result is False:
#         print("Loop found somewhere")
#         if operation == 'jmp':


def eval_nx(operation, position, value, accumulator=0):
    if operation == 'jmp':
        return position + value, accumulator
    elif operation == 'nop':
        return position + 1, accumulator
    elif operation == 'acc':
        return position + 1, accumulator + value


if __name__ == '__main__':
    part_1()
    part_2()
