listOfData = []

with open('data8.txt') as f:
    for i in f:
        temporaryList = [i[:3], i[4], int(i[5:]), 0]
        listOfData.append(temporaryList)

accumulator = 0
counter = 0

while listOfData[counter][3] == 0:
    tmp = listOfData[counter]
    listOfData[counter][3] = 1
    tmpCount = counter
    if listOfData[tmpCount][0] == 'acc':
        if listOfData[tmpCount][1] == '+':
            accumulator += listOfData[tmpCount][2]
        elif listOfData[tmpCount][1] == '-':
            accumulator -= listOfData[tmpCount][2]
        counter += 1
    elif listOfData[tmpCount][0] == 'jmp':
        if listOfData[tmpCount][1] == '+':
            counter += listOfData[counter][2]
        else:
            counter -= listOfData[counter][2]
    else:
        counter += 1

print(accumulator)

accumulator = 0
counter = 0

for i in range(0, len(listOfData)):
    if listOfData[i][0] == 'jmp':
        listOfData[i][0] = 'nop'
    elif listOfData[i][0] == 'nop':
        listOfData[i][0] = 'jmp'

    for j in range(0, len(listOfData)):
        listOfData[j][3] = 0

    accumulator = 0
    counter = 0

    while counter < len(listOfData) and listOfData[counter][3] == 0:
        tmp = listOfData[counter]
        listOfData[counter][3] = 1
        tmpCount = counter
        if listOfData[tmpCount][0] == 'acc':
            if listOfData[tmpCount][1] == '+':
                accumulator += listOfData[tmpCount][2]
            elif listOfData[tmpCount][1] == '-':
                accumulator -= listOfData[tmpCount][2]
            counter += 1
        elif listOfData[tmpCount][0] == 'jmp':
            if listOfData[tmpCount][1] == '+':
                counter += listOfData[counter][2]
            else:
                counter -= listOfData[counter][2]
        else:
            counter += 1

    if listOfData[i][0] == 'jmp':
        listOfData[i][0] = 'nop'
    elif listOfData[i][0] == 'nop':
        listOfData[i][0] = 'jmp'

    if counter >= len(listOfData):
        print(accumulator)
        break
