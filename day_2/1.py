
import time


def main():
    with open('input.txt', 'r') as f_input:
        str_array = f_input.read().splitlines()

    count_of_valid = 0
    count_of_invalid = 0
    for password_with_policy in str_array:
        split = password_with_policy.split(':')

        policy = split[0].split(' ')
        counts = policy[0].split('-')
        min_count = int(counts[0])
        max_count = int(counts[1])
        desired_letter = policy[1]
        password = split[1]
        count = 0
        for letter in password:
            if letter == desired_letter:
                count += 1
        if count >= min_count and count <= max_count:
            count_of_valid += 1
        else:
            count_of_invalid += 1

    #print(count_of_valid)


time_total = 0
test_count = 1000
if __name__ == '__main__':
    for temp_step in range(test_count):
        time_before = time.time()
        main()
        time_total += time.time() - time_before
    print(test_count, "trials took", time_total / test_count)
