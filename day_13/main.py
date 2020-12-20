def read_file(filename):
    unparsed = [line.rstrip() for line in open(filename)]
    return int(unparsed[0]), [int(bus_id) for bus_id in unparsed[1].split(',') if bus_id != 'x']


def part_1(departure_time, bus_ids):
    mylist = [(bus_id - departure_time % bus_id, bus_id) for bus_id in bus_ids]
    lowest = 100000
    lowest_bus = 0
    for item in mylist:
        if item[0] <= lowest:
            lowest = item[0]
            lowest_bus = item[1]
    return lowest * lowest_bus


if __name__ == '__main__':
    departure_time, bus_ids = read_file('input.txt')
    print(part_1(departure_time, bus_ids))
