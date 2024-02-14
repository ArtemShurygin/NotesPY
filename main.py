def fileCreate(fileName):
    file = open(f"Notes/{fileName}.csv", "w")
    file.write(f"Создана заметка с названием '{fileName}'")
    file.close()



import os.path

command = input("Введите комманду: \n 1 - Создать замметку \n 2 - Открыть список заметок \n 3 - Редактировать заметку "
                "\n 4 - Удалить заметку \n 5 - Выход \n\nВаша комманда:")
print(f"Введенная команда: {command}")

if command == "1":
    print("Введенна  комманда 1.")
    fileName = input("Введите название заметки: ")
    if os.path.exists(f"Notes/{fileName}.csv"):
        owerwrite = input("Заметка с таким названием уже существует, вы хотитете перезаписать заметку? "
              "Введите \"y\" (перезаписать заметку) или \"n\" (отменить действие): ")
        if owerwrite == "y":
            fileCreate("fileName")
            print("Заметка перезаписана.")
        elif owerwrite == "n":
            print("Заметка не создана.")
        else:
            print("Введенной комманды нет в списке, заметка не создана.")
    else:
        fileCreate("fileName")
        print("Заметка создана.")
elif command == "2":
    print("Введенна  комманда 2.")
elif command == "3":
    print("Введенна  комманда 3.")
elif command == "4":
    print("Введенна  комманда 4.")
elif command == "5":
    print("Введенна  комманда 5.")
else:
    print("Введенной комманды нет в списке.")


