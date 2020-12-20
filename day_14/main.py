

def read_program(filename):
    unparsed = [line.rstrip() for line in open(filename)]
    instructions = []
    for line in unparsed:
        # If MASK
        if line[1] == 'a':
            mask = line.split('mask = ')[1]
        else:
            instruction = line.split('mem[')[1].split('] = ')
            address = int(instruction[0])
            value = "{0:036b}".format(int(instruction[1]))
            instructions.append((mask, address, value))
    return instructions


def part_1(instructions):
    register = {}
    bitrange = range(35, -1, -1)
    for mask, address, value in instructions:
        for bit in bitrange:
            if mask[bit] != 'X':
                value = value[:bit] + mask[bit] + value[bit + 1:]
        register[address] = int(value, 2)
    return (sum(i for i in register.values()))


def part_2(instructions):
    register = {}
    bitrange = range(35, -1, -1)
    for mask, address, value in instructions:
        x_count = 0
        address = "{0:036b}".format(address)
        for bit in bitrange:
            if mask[bit] != '0':
                address = address[:bit] + mask[bit] + address[bit + 1:]
            if mask[bit] == 'X':
                x_count += 1

        if x_count != 0:
            address_list = [int(address_bin, 2) for address_bin in flatten(recurse(address, x_count, 35))]
            for address in address_list:
                register[address] = int(value, 2)
    return (sum(i for i in register.values()))


def recurse(address, x_count, index):
    address_list = []
    if x_count == 0:
        return address
    else:
        if address[index] == 'X':
            x_count -= 1
            address_one = address[:index] + '1' + address[index + 1:]
            address_zero = address[:index] + '0' + address[index + 1:]
            address_list.append(recurse(address_one, x_count, index - 1))
            address_list.append(recurse(address_zero, x_count, index - 1))
        else:
            address_list.append(recurse(address, x_count, index - 1))

    return address_list


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


if __name__ == '__main__':
    #print("{0:036b}".format(11))
    instructions = read_program('input.txt')
    print(part_1(instructions))
    print(part_2(instructions))
    # Mine
    # 000000000000000000000000000000001011
    # Example:
    # 000000000000000000000000000000001011
