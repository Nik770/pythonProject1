import workingWithData as wwd
import convertData as cd
import userView as uv

dataBase = cd.importCSV()  # Подгрузили БД
myWindow = uv.mainWindow()  # Загружаем меню
useData = dataBase # Временные данные


def start():
    uv.upMenu(myWindow) # Верхнее меню
    myWindow.mainloop() # Мотор


def showInformation(data = dataBase):
    global dataBase
    uv.viewList(data, myWindow)


def addMember():
    uv.changeField(myWindow, 0)
def saveAddMembers(dataBase, newPers):
    dataBase = wwd.newPersonal(dataBase, newPers)
    cd.exportToCSV(dataBase)
    # uv.infoWindow('Сотрудник добавлен')
    return dataBase

def findMember():
    uv.findRequest(myWindow)

def position():
    uv.profRequest(myWindow)
def checkPosition(position):
    professionsList = cd.importProf()
    return wwd.checkValidPosition(professionsList, position)
def newPos(pos):
    cd.exportProf(pos)

def salary():
    uv.salRequest(myWindow)


def delMember():
    checkList = uv.watchCheckList(True) # Список выбранных позиций (со сбросом выбранных элементов)
    keysList = wwd.createKeysList(useData, checkList) # Ключи
    for delID in keysList:
        wwd.deletionOnID(dataBase, delID)
        if useData != dataBase:
            wwd.deletionOnID(useData, delID)
    cd.exportToCSV(dataBase)
    showInformation(useData) if len(useData) else uv.clear(myWindow)
    # uv.infoWindow('Удалено')


def update():
    checkList = uv.watchCheckList() # Список выбранных позиций (без сброса флажков)
    if not checkList:
        uv.infoWindow('Выберите сотрудника')
    elif len(checkList) > 1:
        uv.infoWindow('Выбрано несколько сотрудников')
    else:
        uv.changeField(myWindow, 1)
def saveChangeMember(dataBase, personal):
    global useData
    checkList = uv.watchCheckList(True) # Обнуляем флаги
    keysList = wwd.createKeysList(useData, checkList)
    dataBase = wwd.reloading(dataBase, personal, keysList[0])
    cd.exportToCSV(dataBase)
    # useData = wwd.reloading(useData, personal, keysList[0])
    # uv.infoWindow('Данные изменены')
    return dataBase


def exportJSON():
    cd.exportToJSON(dataBase)


def exportTXT():
    cd.exportToTXT(dataBase) # Сохраняем БД


def transit(index, data):
    function = [saveAddMembers, wwd.findPersonal, wwd.sortOfPosition, wwd.sortOfSalary, saveChangeMember]
    global useData
    useData = function[index](dataBase, data)
    if 0 in useData.keys():
        uv.infoWindow(*useData[0])
    else:
        showInformation(useData)

def changesTransit(index, data):
    global dataBase
    function = [saveAddMembers, saveChangeMember]
    dataBase = function[index](dataBase, data)
    # print(dataBase)
    if len(dataBase):
        showInformation(dataBase)