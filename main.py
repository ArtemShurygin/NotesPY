import datetime
import os.path


def fileCreate(fileName):
    file = open(f"Notes/{fileName}.csv", "w")
    noteTitle = input("Введите заголовок заметки:\n")
    noteBody = input("Введите тело заметки:\n")
    id = Id()
    file.write(f"id: {id} \n")
    file.write(f"{noteTitle} \n\n")
    file.write(f"{noteBody} \n\n")
    date = datetime.datetime.now()
    dateFormat = datetime.datetime.strftime(date, '%d-%m-%Y %H:%M:%S')
    file.write(dateFormat)
    file.close()

def Id ():
    with open("currentId.txt", "r") as f:
        currentIdStr = f.readline().strip('\n')
        currentIdInt = int(currentIdStr)
        newIdInt = currentIdInt + 1
        newIdStr = str(newIdInt)
        print(f"Старый id: {currentIdStr}")
        print(f"Новый id для текущего файла: {newIdStr}")
        f.close()
    with open("currentId.txt", "w") as f:
        f.write(newIdStr)
        f.close()
    return newIdStr


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
            fileCreate(fileName)
            print("Заметка перезаписана.")
        elif owerwrite == "n":
            print("Заметка не создана.")
        else:
            print("Введенной комманды нет в списке, заметка не создана.")
    else:
        fileCreate(fileName)
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


