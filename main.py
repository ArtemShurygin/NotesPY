import datetime
import os.path
from noteDef import *


command = input("Введите комманду: \n 1 - Создать замметку \n 2 - Открыть список заметок \n 3 - Редактировать заметку "
                "\n 4 - Удалить заметку \n 5 - Выход \n\nВаша комманда: ")
print(f"Введенная команда: {command}")

if command == "1":
    print("Введенна  комманда 1.")
    fileCreate()


elif command == "2":
    print("Введенна  комманда 2.")




elif command == "3":
    print("Введенна  комманда 3.")
    noteId = input("Введите id заметки, которую Вы хотите изменить:")
    if os.path.exists(f"Notes/{noteId}.csv"):
        print(f"Файл {noteId}.csv найден.")
        notePrint(noteId)
        commandChange = input("Введите комманду: \n 1 - Дополнить заметку \n 2 - Изменить заметку \nВаша комманда: ")
        if commandChange == "1":
            with open(f"Notes/{noteId}.csv", "a") as f:
                noteAppend = input("Введите текст, который вы хотите добавить: ")
                date = datetime.datetime.now()
                dateFormat = datetime.datetime.strftime(date, '%d-%m-%Y %H:%M:%S')
                f.write(f"\n\n{noteAppend}")
                f.write(f"\n{dateFormat}")
                f.close()
                print("Заметка дополнена.")

        if commandChange == "2":
            with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
                for num, line in enumerate(f):
                    print(textwrap.fill(("Line № " + str(num) + ": " + line.strip()), break_long_words=False, replace_whitespace=False))
                f.close()
            with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
                noteData = f.readlines()
                f.close()
            noteLineChange = int(input("Введите строчку, которую Вы хотите заменить: "))
            noteLineNew = input("Введите текст, на который вы хотите замент данную строчку: ")
            noteData[noteLineChange] = noteLineNew
            with open(f"Notes/{noteId}.csv", "w", encoding="utf-8") as f:
                f.writelines(noteData)
                f.close()


            # with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
            #     for num, line in enumerate(f):
            #         if num == noteLineChange:



    else:
        print(f"Файла {noteId}.csv не существует.")












elif command == "4":
    print("Введенна  комманда 4.")
elif command == "5":
    print("Введенна  комманда 5.")
else:
    print("Введенной комманды нет в списке.")


