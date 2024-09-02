import json
phonebook : dict = {}

def add():
    name = input("Введите имя контакта: ")
    number = input("Ведите номер: ")
    phonebook[name] = number
    save()
    print("\nКонтакт успешно добавлен")
    


def edit():
        edit_contact = input("Введите имя изменяемого контакта: ")
        if edit_contact in phonebook:
            print("Что вы хотите изменить?")
            while True:
                change = int(input("1. имя, 2. номер телефона: "))
                if change == 1:
                    change_name = input("Введите имя контакта: ")
                    phonebook[change_name] = phonebook[edit_contact]  
                    phonebook.pop(edit_contact) 
                    save()
                    print("\nИмя успешно изменено")
                    break
                elif change == 2:
                    change_phone = input ("Введите номер телефона: ")
                    phonebook[edit_contact] = change_phone 
                    save()
                    print("\nНомер успешно изменен")
                    break    
                print("Ведите существующую опцию: ") 
        else:
            print("\nНекорректный ввод")



def delete():
    deleteContacts = input("выберите имя, которое хотите удалить: ")
    del phonebook[deleteContacts]
    save()
    print("\nКонатакт успешно удален")
   


def list():
    for number, name in phonebook.items():
        print(number, name)



def save():
    with open('data.json', 'w') as file:
        file.write(json.dumps(phonebook))



def load():
    global phonebook
    with open('data.json', 'r') as file:
        phonebook = json.load(file)
        


load()
while True:
    option = input(
"""
    Выберите действие:
    add - Добавить контакт
    delete - Удалить контакт
    list - Вывести список контактов
    edit - Отредактировать контакт
    exit - Выйти из приложения
"""
)


    if option == "add":
        add()
    elif option == "delete":
        delete()
    elif option == "list":
        list()     
    elif option == "edit":
        edit()     
    elif option == "exit":
        print("\nКонец программы.")
        break   
    else:
        print("\nНекорректный ввод.")