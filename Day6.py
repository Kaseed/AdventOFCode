def check_anyone_answer_yes(list_of_answers):
    answer = []
    for i in list_of_answers:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer


def check_everyone_answer_yes(list_of_answers):
    to_remove = []
    if len(list_of_answers) == 1:
        return check_anyone_answer_yes(list_of_answers)
    else:
        list_of_unique_answer = check_anyone_answer_yes(list_of_answers[0])
        for i in list_of_answers[1:]:
            for j in list_of_unique_answer:
                if j not in i:
                    to_remove.append(j)
                    # list_of_unique_answer.remove(j)
    to_remove = ''.join(set(to_remove))

    for i in to_remove:
        list_of_unique_answer.remove(i)

    return list_of_unique_answer


listOfData = []
temporaryList = []

with open('data6.txt') as f:
    for i in f:
        if i == '\n':
            listOfData.append(temporaryList)
            temporaryList = []
        elif i.endswith('\n'):
            temporaryList.append(i[:-1])
    temporaryList.append(i)
    listOfData.append(temporaryList)

print(len(listOfData))

sumOfCounts = 0
sumOfUniqueCounts = 0

for i in listOfData:
    # sumOfCounts += len(''.join(set(i)))
    sumOfCounts += len(check_anyone_answer_yes(i))
    sumOfUniqueCounts += len(check_everyone_answer_yes(i))

print(sumOfCounts)
print(sumOfUniqueCounts)
