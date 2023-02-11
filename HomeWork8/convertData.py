myDataBasePath = 'database.csv'
myProfBasePath = 'profBase.csv'


def exportToJSON(dataBase):
    myDataBasePathJson = 'database.json'
    myList = []
    for i in dataBase.keys():
        line = [i]
        for j in dataBase[i]:
            line.append(j)
        myList.append(line)
    with open(myDataBasePathJson, 'w+', encoding='utf-8') as jsonFile:
        jsonFile.write('[')
        myCount = 0
        for item in myList:
            jsonFile.write('\n')
            jsonFile.write('    {' + '\n')
            jsonFile.write(f'        "id": {item[0]},\n')
            jsonFile.write(f'        "surname": {item[2]},\n')
            jsonFile.write(f'        "name": {item[1]},\n')
            jsonFile.write(f'        "patronymic": {item[3]},\n')
            jsonFile.write(f'        "position": {item[4]},\n')
            jsonFile.write(f'        "salary": {item[5]}\n')
            myCount += 1
            if myCount != len(myList):
                jsonFile.write('    },')
            else:
                jsonFile.write('    }')
        jsonFile.write('\n]')


def exportToTXT(dataBase):
    myDataBasePathTxt = 'database.txt'
    myList = []
    for i in dataBase.keys():
        line = f'{i}. '
        for j in dataBase[i]:
            line += f'{j} '
        line += '\n'
        myList.append(line)
    with open(myDataBasePathTxt, 'w+', encoding='utf-8') as txtFile:
        for item in myList:
            txtFile.write(item)


def exportToCSV(myDict):
    with open(myDataBasePath, 'w+', encoding='utf-8') as dataBase:
        dataBase.write(f'id;name;surname;patronymic;position;salary;\n')
        myCount = 0
        for key in myDict:
            myString = str(key) + ';'
            for item in myDict[key]:
                myString += str(item) + ';'
            myCount += 1
            if myCount != len(myDict):
                myString += '\n'
            dataBase.write(myString)

def importCSV():
    myDict = {}
    with open(myDataBasePath, 'r', encoding='utf-8') as dataBase:
        for line in dataBase:
            if line.strip()[0] != 'i':
                oneLine = line.strip()
                count = 1
                while oneLine[count] != ';':
                    count += 1
                memberID = int(oneLine[:count])
                myList = line.strip().split(';')
                myList.remove('')
                myList.pop(0)
                myDict[memberID] = myList

    return myDict


def importProf():
    dictProf = {}
    with open(myProfBasePath, 'r', encoding='utf-8') as ProfBase:
        text = ProfBase.read()
        if len(text):
            lines = text.split('\n')
            # инкрементируем счетчик
            for i in range(len(lines)):
                if len(lines[i]):
                    dictProf[i] = lines[i]
        else:
            dictProf[0] = ''

    return dictProf


def exportProf(newPosition):

    with open(myProfBasePath, 'a', encoding='utf-8') as profBase:
        newPosition = newPosition + '\n'
        profBase.write(newPosition)