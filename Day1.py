listOfDate = []

with open("data1.txt") as f:
    for i in f:
        listOfDate.append(int(i))

print(listOfDate)

for i in listOfDate:
    for j in listOfDate:
        if i+j == 2020:
            print(f"Numbers {i}+{j}=2020\n{i}*{j}={i*j}")

print()

for i in listOfDate:
    for j in listOfDate:
        for k in listOfDate:
            if i+j+k == 2020:
                print(f"Numbers {i}+{j}+{k}=2020\n{i}*{j}*{k}={i * j * k}")
