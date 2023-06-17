contacts = {"Михайлов": "123-45-67", "Андреев": "214-46-78", "Якушев": "123-68-89"}
while True:
    print("1. Изменить контакт")
    print("2. Удалить контакт")
    print("3. Выход")
    choice = (input(" Выберите действие: "))
    if choice=="1":
        name = input("Введите имя: ")
        if name in contacts:
            contacts[name] = name
            changed=input("Введите изменения: ")
            name=changed
            print("Контакт успешно изменен!")
        else:
            print("Такого контакта нет в списке")
    elif choice == "2":
        name = input("Введите имя: ")
        if name in contacts:
            del contacts[name]
            print("Контакт успешно удален!")
        else:
            print("Такого контакта нет в списке")
    elif choice == "3":
        break
    else:
        print("Выберите действие из списка")
