
desired_number = 2020
number_array = []
with open('input.txt', 'r') as f_input:
    number_array = f_input.read().splitlines()

for each in number_array:
    number = int(each)
    if str(desired_number - number) in number_array:
        print(each, " and ", desired_number - number)
        print((desired_number - number) * number)
