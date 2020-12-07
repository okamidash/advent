

def part_1():
    bag_rules = {}
    direct_bags = set([])
    for line in open("input.txt"):
        # Using :-1 instead of rstrip as it is faster
        line = line[:-1]
        splitln = line.split(' bags contain ')
        bag_type = splitln[0]
        rules = {}
        for bag_rule in splitln[1].split(', '):
            quantity = bag_rule[0]
            split_bag_rule = bag_rule.split(' ')
            if split_bag_rule[0] != "no":
                rule_name = split_bag_rule[1] + " " + split_bag_rule[2]
                if rule_name == "shiny gold":
                    direct_bags.add(bag_type)
                rules[rule_name] = quantity
        bag_rules[bag_type] = rules
    # Now perform a search
    while True:
        current_direct_set = len(direct_bags)
        for search_bag in bag_rules:
            for bag_rule in bag_rules[search_bag]:
                if bag_rule in direct_bags:
                    direct_bags.add(search_bag)
        if current_direct_set == len(direct_bags):
            return len(direct_bags)
    print(direct_bags)


def part_2():
    bag_rules = {}
    finalizers = []
    for line in open("input.txt"):
        # Using :-1 instead of rstrip as it is faster
        line = line[:-1]
        splitln = line.split(' bags contain ')
        bag_type = splitln[0]
        rules = {}
        # Seprate the bag conditions out into a list
        for bag_rule in splitln[1].split(', '):
            quantity = bag_rule[0]
            split_bag_rule = bag_rule.split(' ')
            if bag_rule == "no other bags.":
                finalizers.append(bag_type)
            else:
                rule_name = split_bag_rule[1] + " " + split_bag_rule[2]
                rules[rule_name] = int(quantity)
        if rules != {}:
            bag_rules[bag_type] = rules

    # No, I don't know why I need to subtract 1.
    return (recurse(finalizers, bag_rules, "shiny gold") - 1)


def recurse(finalizers, bag_rules, search_bag, prepared_totals={}):
    # If the bag cannot recurse any further, just return
    if search_bag in finalizers:
        # Return None if a finalizer is met
        return None
    # If not, commit an atrocity
    else:
        # Create a running total to add to
        total = 1
        # Iterate over the bag rules for each bag
        for next_bag in bag_rules[search_bag]:
            # Set the multiplier
            next_bag_total = bag_rules[search_bag][next_bag]
            # Recurse into the bag rules
            if next_bag in prepared_totals:
                recurse_answer = prepared_totals[next_bag]
            else:
                recurse_answer = recurse(finalizers, bag_rules, next_bag, prepared_totals)
                prepared_totals[next_bag] = recurse_answer
            # So that we don't multiply by None
            if recurse_answer is None:
                total += next_bag_total
            else:
                total += next_bag_total * recurse_answer

    return total

# timecheck code lovingly submitted by Vess
"""
'####:'########::'######:::::'###::::'########:::'#######:::'######:::'######::'##::::'##:'##::::'##:
. ##::... ##..::'##... ##:::'## ##::: ##.... ##:'##.... ##:'##... ##:'##... ##: ##:::: ##: ###::'###:
: ##::::: ##:::: ##:::..:::'##:. ##:: ##:::: ##: ##:::: ##: ##:::..:: ##:::..:: ##:::: ##: ####'####:
: ##::::: ##::::. ######::'##:::. ##: ########:: ##:::: ##:. ######::. ######:: ##:::: ##: ## ### ##:
: ##::::: ##:::::..... ##: #########: ##.....::: ##:::: ##::..... ##::..... ##: ##:::: ##: ##. #: ##:
: ##::::: ##::::'##::: ##: ##.... ##: ##:::::::: ##:::: ##:'##::: ##:'##::: ##: ##:::: ##: ##:.:: ##:
'####:::: ##::::. ######:: ##:::: ##: ##::::::::. #######::. ######::. ######::. #######:: ##:::: ##:
....:::::..::::::......:::..:::::..::..::::::::::.......::::......::::......::::.......:::..:::::..::
"""
def timecheck():
    import time
    time_total = 0
    test_count = 100
    for temp_step in range(test_count):
        time_before = time.time()
        part_2()
        time_total += time.time() - time_before
        print(test_count, "trials took", time_total / test_count)
#


if __name__ == '__main__':
    #part_1()
    part_2()
