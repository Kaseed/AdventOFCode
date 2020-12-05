def isRightHcl(hcl):
    # if hcl.startswith('#'):
    #     if len(hcl) == 7:
    #         return True
    # else:
    #     return False
    if not hcl.startswith('#') or len(hcl) != 7:
        return False

    good_characters = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in hcl[1:]:
        if not (i in good_characters or i.isdecimal()):
            return False
    return True


def changeListToDictonary(list):
    dict = {}
    for i in list.split():
        keyVal, value = i.split(':')
        dict[keyVal] = value
    return dict


def checkPassport(list):
    dict = changeListToDictonary(list)

    passportElements = [dict.get('byr', 0), dict.get('iyr', 0), dict.get('eyr', 0), dict.get('hgt', 0),
                        dict.get('hcl', 0), dict.get('ecl', 0), dict.get('pid', 0)]

    if all(passportElements):
        return 1
    else:
        return 0


def checkDataPassport(list):
    dict = changeListToDictonary(list)

    passportElements = []
    passportElements.append(1920 <= int(dict.get('byr')) <= 2002)
    passportElements.append(2010 <= int(dict.get('iyr')) <= 2020)
    passportElements.append(2020 <= int(dict.get('eyr')) <= 2030)
    if dict.get('hgt')[-2:] == 'cm':
        passportElements.append(150 <= int(dict.get('hgt')[:-2]) <= 193)
    elif dict.get('hgt')[-2:] == 'in':
        passportElements.append(59 <= int(dict.get('hgt')[:-2]) <= 76)
    else:
        passportElements.append(False)


    #if dict.get('hcl').startswith('#'):
    passportElements.append(isRightHcl(dict.get('hcl')))

    #     passportElements.append(True)
    # else:
    #     passportElements.append(False)

    eyeColourList = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if dict.get('ecl') in eyeColourList:
        passportElements.append(True)
    else:
        passportElements.append(False)

    if len(dict.get('pid')) == 9 and dict.get('pid').isdecimal():
        passportElements.append(True)
    else:
        passportElements.append(False)

    if all(passportElements):
        return True
    else:
        return False


listOfData = []
temporaryString = ''
amountOfRightPassport = 0
amountOfRightDataPassport = 0

# Pobranie danych
with open("data4.txt") as f:
    for i in f:
        if i == '\n':
            listOfData.append(temporaryString)
            temporaryString = ''
        elif i[-1] == '\n':
            temporaryString += i[:-1] + ' '
        else:
            temporaryString += i
    listOfData.append(temporaryString)

# print(len(listOfData))

for i in listOfData:
     if checkPassport(i):
        amountOfRightPassport += 1
        if checkDataPassport(i):
            amountOfRightDataPassport += 1
print(amountOfRightPassport)
print(amountOfRightDataPassport)
