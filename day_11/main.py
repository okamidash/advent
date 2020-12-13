# 76 = L EMPTY
# 46 = . FLOOR
# 35 = # OCCUPIED


import time


def grab_seats(filename):
    seat_map = []
    for line in open(filename):
        line = line.rstrip()
        seat_map.append([ord(char) for char in line])
    return seat_map


def show_seating(seats):
    for idx, line in enumerate(seats):
        print(f"\t{idx} | {''.join([chr(char) for char in line])} |")
    print(f"\t  | {''.join([str(x) for x in range(0,len(seats))])} |")
    print("\n")
    time.sleep(1)


def get_adjacent_one(x_pos, y_pos, x_max, y_max, seats):
    adjacent = []
    if x_pos != 0:
        adjacent.append(seats[y_pos][x_pos - 1])            # x - 1, y
        if y_pos != 0:
            adjacent.append(seats[y_pos - 1][x_pos - 1])    # x - 1, y - 1
        if y_pos != y_max:
            adjacent.append(seats[y_pos + 1][x_pos - 1])    # x - 1, y + 1

    #   x + 1,  y
    if y_pos != 0:
        adjacent.append(seats[y_pos - 1][x_pos])            # x,    y - 1
    if y_pos != y_max:
        adjacent.append(seats[y_pos + 1][x_pos])            # x,    y + 1

    if x_pos != x_max:
        adjacent.append(seats[y_pos][x_pos + 1])            # x + 1,    y
        if y_pos != 0:
            adjacent.append(seats[y_pos - 1][x_pos + 1])    # x + 1, y - 1
        if y_pos != y_max:
            adjacent.append(seats[y_pos + 1][x_pos + 1])    # x + 1, y + 1
    return adjacent


def mover(x_pos, y_pos, x_mov, y_mov, x_brk, y_brk):
    while True:
        if y_pos == y_brk or x_pos == x_brk:
            break
        else:
            y_pos += y_mov
            x_pos += x_mov
        seat = seats[y_pos][x_pos]
        if seat == 35 or seat == 76:
            return seat
    return None


def get_visible(x_pos, y_pos, x_max, y_max, seats):
    adjacent = []
    series = [
        (0, -1, None, 0),
        (0, 1, None, y_max),
        (1, 0, x_max, None),
        (1, -1, x_max, 0),
        (1, 1, x_max, y_max),
        (-1, 0, 0, None),
        (-1, 1, 0, y_max),
        (-1, -1, 0, 0)
    ]
    return [mover(x_pos, y_pos, x_mov, y_mov, x_brk, y_brk) for x_mov, y_mov, x_brk, y_brk in series]


def part_1(seats):
    changed = True
    max_y = len(seats) - 1
    max_x = len(seats[0]) - 1
    x_range = range(0, max_x + 1)
    y_range = range(0, max_y + 1)
    while changed:
        queue = []
        changed = False
        for y in y_range:
            for x in x_range:
                seat = seats[y][x]
                if seat != 46:  # Check if it's a floor space
                    adjacent_seats = get_adjacent_one(x, y, max_x, max_y, seats)
                    if seat == 76:  # Handle empty
                        if 35 not in adjacent_seats:
                            queue.append((y, x, 35))
                            changed = True
                    elif seat == 35:
                        if adjacent_seats.count(35) >= 4:
                            queue.append((y, x, 76))
                            changed = True
        for y, x, num in queue:
            seats[y][x] = num

    total = 0
    for line in seats:
        total += line.count(35)
    return total


def part_2(seats):
    changed = True
    max_y = len(seats) - 1
    max_x = len(seats[0]) - 1
    x_range = range(0, max_x + 1)
    y_range = range(0, max_y + 1)
    while changed:
        queue = set()
        changed = False
        for y in y_range:
            for x in x_range:
                seat = seats[y][x]
                if seat != 46:  # Check if it's a floor space
                    adjacent_seats = get_visible(x, y, max_x, max_y, seats)
                    if seat == 76:  # Handle empty
                        if 35 not in adjacent_seats:
                            queue.add((y, x, 35))
                            changed = True
                    elif seat == 35:
                        if adjacent_seats.count(35) >= 5:
                            queue.add((y, x, 76))
                            changed = True
        for y, x, num in queue:
            seats[y][x] = num
    total = 0
    for line in seats:
        total += line.count(35)
    return total


if __name__ == '__main__':
    seats = grab_seats('input.txt')
    #print(part_1(seats))
    print(part_2(seats))
