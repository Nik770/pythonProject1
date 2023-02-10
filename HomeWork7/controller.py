import view as v
import module as m

def create_contact():
    return m.create(v.add_new())

def find_contact():
    return m.find(v.find_phone())

def export_contact(swith):
    function = [m.export_txt, m.export_xml]
    return function[int(swith)-3]()

def menu(answer):
    if answer == '0':
        show_res('Выход')
    else:
        if answer == '1':
            show_res(create_contact())
        elif answer == '2':
            show_res(find_contact())
        elif answer == '3' or '4':
            show_res(export_contact(answer))
        else:
            show_res('Ошибка')
        menu(v.show_nemu())

def show_res(res):
    v.view_res(res)