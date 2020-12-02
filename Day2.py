listOfData = []

# Pobranie danych
with open("data2.txt") as f:
    for i in f:
        listOfData.append(i)

rightPasswords = 0

# print(listOfData)

for i in listOfData:
    list = i.split(' ', 2)
    minLetter, maxLetter = list[0].split('-')
    countOfLetter = list[2].count(list[1][0])
    if int(minLetter) <= countOfLetter <= int(maxLetter):
        rightPasswords += 1

print(rightPasswords)

rightPasswords2 = 0

for i in listOfData:
    list = i.split(' ', 2)
    firstLetter, secondLetter = list[0].split('-')
    if (list[2][int(firstLetter)-1] == list[1][0]) ^ (list[2][int(secondLetter)-1] == list[1][0]):
        rightPasswords2 += 1

print(rightPasswords2)
