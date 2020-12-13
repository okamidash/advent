def grab_log(filename):
    return [(ord(line[0]), int(line[1:])) for line in open(filename)]
# North = 0                 0
# East = 1                 3X1
# South = 2                 2
# West = 3
## ORDINALS
# N = 78
# S = 83
# E = 69
# W = 87
# L = 76
# R = 82
# F = 70


def det_rotation(bearing, rotation, one_turn=(1, 2, 3, 0), two_turn=(2, 3, 0, 1), three_turn=(3, 0, 1, 2)):
    new_bearing = 0
    if rotation == 90:
        new_bearing = one_turn[bearing]
    elif rotation == 180 or rotation == -180:
        new_bearing = two_turn[bearing]
    elif rotation == 270:
        new_bearing = three_turn[bearing]
    elif rotation == 360 or rotation == -360 or rotation == 0:
        new_bearing = bearing
    elif rotation == -90:
        new_bearing = three_turn[bearing]
    elif rotation == -270:
        new_bearing = one_turn[bearing]
    return new_bearing


def wp_det_rotation(rotation, wp_north_south, wp_east_west):
    if rotation == 90:
        return wp_east_west, wp_north_south
    if rotation == 180:
        return -wp_north_south, -wp_east_west
    else:
        return wp_north_south, wp_east_west


def det_move(north_south, east_west, bearing, value):
    if bearing == 0:
        return north_south + value, east_west
    elif bearing == 1:
        return north_south, east_west + value
    elif bearing == 2:
        return north_south - value, east_west
    elif bearing == 3:
        return north_south, east_west - value


def part_2(log, log_length, position=(10, 1), waypoint=(1, 10)):
    ship_north_south, ship_east_west = position
    wp_north_south, wp_east_west = waypoint
    if log_length == 0:
        return abs(ship_north_south) + abs(ship_east_west)
    command, value = log[0]
    if command == 78:
        # COMMAND: Go North
        wp_north_south += value
    elif command == 83:
        # COMMAND: Go South
        wp_north_south -= value
    elif command == 69:
        # COMMAND: Go East
        wp_east_west += value
    elif command == 87:
        # COMMAND: Go West
        wp_east_west -= value
    elif command == 76:
        # COMMAND: Rotate Left
        wp_north_south, wp_east_west = wp_det_rotation(-value, wp_north_south, wp_east_west)
    elif command == 82:
        # COMMAND: Rotate Right
        wp_north_south, wp_east_west = wp_det_rotation(value, wp_north_south, wp_east_west)
    elif command == 70:
        ship_north_south += value * wp_north_south
        ship_east_west += value * wp_east_west
    print(ship_north_south, ship_east_west)
    #north_south, east_west = det_move(north_south, east_west, bearing, value)
    return part_1(log[1:], log_length - 1, (ship_north_south, ship_east_west), (wp_north_south, wp_east_west))


def part_1(log, log_length, position=(0, 0, 1)):
    north_south, east_west, bearing = position
    if log_length == 0:
        return abs(north_south) + abs(east_west)
    command, value = log[0]
    if command == 78:
        # COMMAND: Go North
        north_south += value
    elif command == 83:
        # COMMAND: Go South
        north_south -= value
    elif command == 69:
        # COMMAND: Go East
        east_west += value
    elif command == 87:
        # COMMAND: Go West
        east_west -= value
    elif command == 76:
        # COMMAND: Rotate Left
        bearing = det_rotation(bearing, -value)
    elif command == 82:
        # COMMAND: Rotate Right
        bearing = det_rotation(bearing, value)
    elif command == 70:
        # COMMAND: GO FORWARD
        north_south, east_west = det_move(north_south, east_west, bearing, value)
    return part_1(log[1:], log_length - 1, (north_south, east_west, bearing))


if __name__ == '__main__':
    log = grab_log('input.txt')
    print(f"Part 1: {part_1(log, len(log))}")
    #print(part_2(log, len(log)))
