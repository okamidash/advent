
def part_1():
    answers = []
    answer = ""
    for line in open("input.txt"):
        # Using :-1 instead of rstrip as it is faster
        line = line[:-1]
        for char in line:
            if char not in answer:
                answer += char
        if line == "":
            answers.append(len(answer))
            answer = ""
    answers.append(len(answer))
    #print(sum(answers))


def part_2():
    answers = 0
    answer = 0
    answer_dict = {}
    count = 0
    for line in open("input.txt"):
        line = line[:-1]

        for idx, char in enumerate(line):
            answer_dict[char] = answer_dict.get(char, 0) + 1

        if line == "":
            for charcount in answer_dict:
                if answer_dict[charcount] == count:
                    answer += 1
            answers += answer
            answer_dict = {}
            answer = 0
            count = 0

        else:
            count += 1
    #print(answers)


if __name__ == '__main__':
    part_1()
    part_2()
