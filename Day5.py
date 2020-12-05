def changeToDec(number):
    row = number[:7]
    column = number[7:11]

    rowSeat = 0
    columnSeat = 0

    for i in range(0, 7):
        if row[i] == 'B':
            rowSeat += 2 ** (6 - i)

    for i in range(0, 3):
        if column[i] == 'R':
            columnSeat += 2 ** (2 - i)

    return rowSeat * 8 + columnSeat


def searchSeat(list):
    list.sort()
    for i in range(0, len(list)):
        if i != len(list) - 1 and list[i + 1] - list[i] == 2:
            return list[i] + 1

    return -1


listOfData = []
listOfSeat = []

with open('data5.txt') as f:
    for i in f:
        listOfData.append(i)

maxSeat = changeToDec(listOfData[0])
listOfSeat.append(changeToDec(listOfData[0]))
for i in listOfData[1:]:
    listOfSeat.append(changeToDec(i))
    if changeToDec(i) > maxSeat:
        maxSeat = changeToDec(i)
# print(changeToDec('FFFBBBFRRR'))
print(maxSeat)

print(searchSeat(listOfSeat))
