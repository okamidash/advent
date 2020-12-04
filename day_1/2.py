import sys
desired_number = 2020
with open('input.txt', 'r') as f_input:
    str_array = f_input.read().splitlines()
    number_array = sorted([int(string) for string in str_array])

# A + B + C = 2020
# Lazy as fuck but I don't care
for A in number_array:
    for B in number_array:
        for C in number_array:
            if (A + B + C) == desired_number:
                print(A * B * C)
                sys.exit(0)
