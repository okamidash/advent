"""
____ ___  ____ ___  __   ____ _____  ____/ /  / /_  ____ __   _____
/ __ `__ \/ __ `/ / / /  / __ `/ __ \/ __  /  / __ \/ __ `/ | / / _ \
/ / / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /  / / / / /_/ /| |/ /  __/
/_/ /_/ /_/\__,_/\__, /   \__, /\____/\__,_/  /_/ /_/\__,_/ |___/\___/
             /____/   /____/

____ ___  ___  ____________  __   ____  ____     ____ ___  __  __
/ __ `__ \/ _ \/ ___/ ___/ / / /  / __ \/ __ \   / __ `__ \/ / / /
/ / / / / /  __/ /  / /__/ /_/ /  / /_/ / / / /  / / / / / / /_/ /
/_/ /_/ /_/\___/_/   \___/\__, /   \____/_/ /_/  /_/ /_/ /_/\__, /
                      /____/                            /____/
                  __
_________  __  __/ /
/ ___/ __ \/ / / / /
(__  ) /_/ / /_/ / /
/____/\____/\__,_/_/

"""


import math
import time
time_total = 0
test_count = 1000


def main():
    math.prod([sum([line[int((position / y_move * x_move) % len(line))] == '#' and (position) %
                    y_move == 0 for position, line in enumerate(open('input.txt').read().splitlines())]) for x_move, y_move in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])


#
if __name__ == '__main__':
    for temp_step in range(test_count):
        time_before = time.time()
        main()
        time_total += time.time() - time_before
    print(test_count, "trials took", time_total / test_count)
