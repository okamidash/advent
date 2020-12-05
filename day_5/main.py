def search(search_set: str, min: int, max: int) -> int:
    row_range = abs(max - min)
    differential = round(row_range / 2)

    search_char = search_set[0]

    # Take the lower half
    if search_char == 'F' or search_char == 'L':
        if len(search_set) == 1:
            return min
        return search(search_set[1:], min, max - differential)
    # Take the upper half
    elif search_char == 'B' or search_char == 'R':
        if len(search_set) == 1:
            return max
        return search(search_set[1:], min + differential, max)


def part_2(seat_id_list):
    for idx, seat_id in enumerate(seat_id_list):
        if seat_id_list[idx + 1] != seat_id + 1:
            return seat_id + 1


def main():
    highest_seat_id = 0
    seat_id_list = []
    for boarding_pass in open('input.txt'):
        boarding_pass = boarding_pass.rstrip()
        # The determiner of which row to sit in
        row_search = boarding_pass[:7]
        row = search(row_search, 0, 127)
        # The determiner of which aisle to sit in
        aisle_search = boarding_pass[7:]
        aisle = search(aisle_search, 0, 7)

        seat_id = row * 8 + aisle
        seat_id_list.append(seat_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print(f"Part 1: {highest_seat_id}")
    print(f"Part 2: {part_2(sorted(seat_id_list))}")


if __name__ == '__main__':
    main()
