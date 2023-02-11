import TestControl as control
def findPersonal(myDict, request):
    res = {}
    satisfyIndex = [0 for i in range(max(myDict.keys()) + 1)]
    for i in myDict:
        for j in myDict[i]:
            if request.lower().count(j.lower()):
                satisfyIndex[i] += 1
    if max(satisfyIndex):
        if satisfyIndex.count(max(satisfyIndex)) > 1:
            satisfyList = [i for i in range(len(satisfyIndex)) if satisfyIndex[i] == max(satisfyIndex)]
            for i in satisfyList:
                res[i] = myDict[i]
        else:
            maxIndex = satisfyIndex.index(max(satisfyIndex))
            res[maxIndex] = myDict[maxIndex]
    else:
        res[0] = ['Сотрудник не найден']
    return res

def sortOfPosition(myDict, position):
    res = {}
    if control.checkPosition(position):
        if str(myDict.items()).count(position) > 0:
            for i in myDict:
                if myDict[i][3] == position:
                    res[i] = myDict[i]
        else:
            res[0] = ['Нет сотрудников на данной должности']
    else:
        res[0] = ['Должность указана неверно']
    return res

def sortOfSalary(myDict, value):
    min, max = value
    res = {}
    if checkValue(min, max):
        for i in myDict:
            if int(min) <= int(myDict[i][4]) <= int(max):
                res[i] = myDict[i]
        if not len(res):
            res[0] = ['Сотрудники с подходящей зарплатой не найдены']
    else:
        res[0] = ['Значение указано неверно']
    return res

def newPersonal(myDict, newMember):
    position = newMember[3]
    if not control.checkPosition(position):
        control.newPos(position)
    lastKeys = int(list(myDict.keys())[-1])
    if lastKeys == len(myDict):
        newID = len(myDict) + 1
        myDict[newID] = list(newMember)
    else:
        for i, key in enumerate(myDict, 1):
            if int(key) != i:
                myDict[i] = list(newMember)
                myDict = dict(sorted(myDict.items()))
                break
    return myDict


def deletionOnPerson(myDict, delMember):
    for delID in delMember.keys():
        del myDict[delID]

def deletionOnID(myDict, delID):
    del myDict[delID]

def reloading(myDict, changedPersonal, PersID):
    deletionOnID(myDict, PersID)
    myDict[PersID] = list(changedPersonal)
    myDict = dict(sorted(myDict.items()))
    return myDict

def checkSort(myDict, PersID):
    sortList = {}
    for i in PersID:
        sortList[i] = myDict[i]
    return sortList

def takeProfile(myDict, id):
    return {id: myDict[id]}

def createKeysList(useList, numbers):
    keysList = []
    allKeys = [i for i in list(useList.keys())]
    for i in numbers:
        keysList.append(allKeys[i])
        return keysList

def checkValidPosition(professions, request):
    return bool(list(check.count(request) for check in professions.items()).count(1))

def checkValue(min, max):
    if alphaCheck(min) and alphaCheck(max):
        min = int(min)
        max = int(max)
        if max < 0 or min < 0 or max < min:
            return False
    else:
        return False
    return True

def alphaCheck(value):
    return bool((list(symbol.isalpha() for symbol in value)).count(1) == 0)

def checkCorrectInput(myDict, newMember):
    name, surname, patronymic, position, salary = newMember
    if not (alphaCheck(salary) and int(salary) > 0):
        return False
    if not checkValidPosition(position):
        print('Новая профессия')
    find = checkPersonal(myDict, 1, surname)
    if not (0 in find.keys()):
        find = checkPersonal(find, 0, name)
        if not (0 in find.keys()):
            find = checkPersonal(find, 2, patronymic)
            if not (0 in find.keys()):
                print('Человек с таким ФИО уже записан')
                find = checkPersonal(find, 3, position)
                if not (0 in find.keys()):
                    print(
                        'Полное совпадение с ранее записанным сотрудником')
    return True

def checkPersonal(myDict, searchKey, request):

    res = {}
    for i in myDict:
        if myDict[i][searchKey].lower() == request.lower(): # Ищем совпадения по объекту поиска
            res[i] = myDict[i]
    if not len(res):
        res[0] = ['Сотрудник не найден']
    return res