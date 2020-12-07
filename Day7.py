def find_the_outer_bag(list_of_rules, inner_bag):
    list_of_outer_bag = []
    for rule in list_of_rules:
        if rule.rfind(inner_bag) != -1 and rule.rfind(inner_bag) != 0:
            x = get_outer_bag(rule)
            list_of_outer_bag.append(x)

    return list_of_outer_bag


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def get_outer_bag(rule):
    x = find_nth(rule, ' ', 2)
    return rule[:x]


def get_inners_amount(list_of_rules, outer_bag):
    for rule in list_of_rules:
        if rule.find(outer_bag) != -1 and rule.find(outer_bag) == 0:
            x = rule.find('contain ')
            list_of_bags = rule[x + 8: -1].split(', ')
            break

    amount_of_bags = 0

    if list_of_bags[0][0].isdecimal():
        for bag in list_of_bags:
            amount = int(bag[0])
            type_bag = get_outer_bag(bag[2:])
            amount_of_bags += amount * get_inners_amount(list_of_rules, type_bag)
        return amount_of_bags + 1
    else:
        return 1


listOfData = []

with open('data7.txt') as f:
    for i in f:
        listOfData.append(i)

listofBags = find_the_outer_bag(listOfData, 'shiny gold')

change = True
while change:
    change = False
    temporaryList = []
    for i in listofBags:
        temporaryList += find_the_outer_bag(listOfData, i)

    for i in temporaryList:
        if i not in listofBags:
            listofBags.append(i)
            change = True

print(len(listofBags))

AmountOfInnerBags = get_inners_amount(listOfData, 'shiny gold')

print(AmountOfInnerBags - 1)
