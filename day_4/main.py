import re
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
passports = []

data = {}


class Validator:
    def __init__(self):
        self.hcl_reg = re.compile('#([a-f]|[0-9]){6}')

    def intcast(self, input):
        try:
            return int(input)
        except:
            return False

    def minmax(self, input, min, max):
        if input is not False and input >= min and input <= max:
            return True
        else:
            return False

    def lencheck(self, input, length):
        if len(input) != length:
            return False
        else:
            return input

    def validate_byr(self, byr):
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        return self.minmax(self.intcast(byr), 1920, 2002)

    def validate_iyr(self, iyr):
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return self.minmax(self.intcast(self.lencheck(iyr, 4)), 2010, 2020)

    def validate_eyr(self, eyr):
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return self.minmax(self.intcast(self.lencheck(eyr, 4)), 2020, 2030)

    def validate_hgt(self, hgt):
        # hgt (Height) - a number followed by either cm or in:
        #    If cm, the number must be at least 150 and at most 193.
        #    If in, the number must be at least 59 and at most 76.
        if hgt[-2:] == "in":
            return self.minmax(self.intcast(hgt[:-2]), 59, 76)
        elif hgt[-2:] == "cm":
            return self.minmax(self.intcast(hgt[:-2]), 150, 193)

    def validate_hcl(self, hcl):
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if hcl[0] != '#':
            return False
        else:
            if self.hcl_reg.match(hcl) is None:
                return False
            else:
                return True

    def validate_pid(self, pid):
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        return self.lencheck(pid, 9)

    def validate_ecl(self, ecl):
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        else:
            return True


validator = Validator()

for line in open("input.txt"):

    print(line)
    if line is "\n":
        passports.append(data)
        data = {}
    else:
        line_buffer = line.rstrip().split(" ")
        for piece in line_buffer:
            print(piece)
            data_buffer = piece.split(":")
            key = data_buffer[0]
            if key in required_fields:
                val = data_buffer[1]
                if getattr(validator, f'validate_{key}')(val):
                    data[key] = val


valid = 0
for passport in passports:
    print(passport)
    if len(passport.keys()) == len(required_fields):
        valid += 1
     invalid += 1

print(valid)
