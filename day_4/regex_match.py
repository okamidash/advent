import re
#from timeit import timeit
required_fields = [
    "byr",  # Birth Year
    "iyr",  # Issue Year
    "eyr",  # Expiration Year
    "hgt",  # Height
    "hcl",  # Hair Color
    "ecl",  # Eye Color
    "pid",  # Passport ID
    #"cid"  # Country ID
    ]


class Validator:
    def __init__(self):
        self.hcl = re.compile('#([a-f]|[0-9]){6}')
        self.byr = re.compile('(19[2-9][0-9])|(200[0-2])')
        self.iyr = re.compile('(201[0-9]|2020)')
        self.eyr = re.compile('(202[0-9]|2030)')
        self.hgt = re.compile('((1([5-8][0-9]|9[0-3]))cm)|((([5-6][0-9])|7[0-6])in)')
        self.pid = re.compile('^[0-9]{9}$')
        self.ecl = re.compile('(amb|blu|brn|gry|grn|hzl|oth)$')


def main():

    validator = Validator()
    passports = []

    data = {}
    for line in open("input.txt"):
        if line == "\n":
            passports.append(data)
            data = {}
        else:
            line_buffer = line.rstrip().split(" ")
            for piece in line_buffer:
                data_buffer = piece.split(":")
                key = data_buffer[0]
                if key in required_fields:
                    val = data_buffer[1]
                    if getattr(validator, f'{key}').match(val) is not None:
                        data[key] = val

    valid = 0
    for passport in passports:
        if len(passport.keys()) == len(required_fields):
            valid += 1


if __name__ == '__main__':
    #print(timeit(main, number=1))
    main()
