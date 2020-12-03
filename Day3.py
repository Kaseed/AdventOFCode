def count_of_trees(list, right, down):
    positionX = 0
    positionY = 0
    amountOfTrees = 0

    for line in list:
        if positionY % down == 0:
            if (positionX > 30):
                positionX = (positionX % 30) - 1
            if (line[positionX] == '#'):
                amountOfTrees += 1
            positionX += right
        positionY += 1

    return amountOfTrees


listOfData = []

# Pobranie danych
with open("data3.txt") as f:
    for i in f:
        listOfData.append(i)

print(listOfData)

# positionX = 0
# amountOfTrees = 0
#
# for line in listOfData:
#     if(positionX > 30):
#         positionX = (positionX % 30) - 1
#     if(line[positionX] == '#'):
#         amountOfTrees += 1
#     positionX += 3
# print(amountOfTrees)

print(count_of_trees(listOfData, 3, 1))

print(count_of_trees(listOfData, 1, 1))
print(count_of_trees(listOfData, 5, 1))
print(count_of_trees(listOfData, 7, 1))
print(count_of_trees(listOfData, 1, 2))

x = count_of_trees(listOfData, 3, 1) * count_of_trees(listOfData, 1, 1) \
    * count_of_trees(listOfData, 5, 1) * count_of_trees(listOfData, 7, 1) \
    * count_of_trees(listOfData, 1, 2)

print(x)
