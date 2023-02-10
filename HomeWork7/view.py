
def add_new():
    name = input('Имя: ')
    phone = input('Номер: ')
    return (name, phone)


def find_phone():
    return input('Имя: ')


def show_nemu():
    return input('1 - Создать контакт\n' \
                   '2 - Поиск контакта\n' \
                   '3 - экспортировать в txt\n' \
                   '4 - экспортировать в xml\n' \
                   '0 - выход\n'\
                 'Введите число: ')



def view_res(res):
    print(f"{res}\n")