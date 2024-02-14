import datetime
import os.path


def fileCreate(fileName, newId):
    file = open(f"Notes/{fileName}.csv", "w")
    file.write(f"Создана заметка с названием '{fileName}' \n")
    if newId == 1:
        id = Id()
        file.write(f"{id} \n")
    else:
        file.write(f"old id \n")
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
        print(currentIdStr)
        print(newIdStr)
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
            NewId = 0
            fileCreate(fileName, NewId)
            print("Заметка перезаписана.")
        elif owerwrite == "n":
            print("Заметка не создана.")
        else:
            print("Введенной комманды нет в списке, заметка не создана.")
    else:
        NewId = 1
        fileCreate(fileName, NewId)
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


