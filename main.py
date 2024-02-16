import datetime
import os.path
from noteDef import *


command = input("Введите комманду: \n 1 - Создать замметку \n 2 - Открыть список заметок \n 3 - Редактировать заметку "
                "\n 4 - Удалить заметку \n 5 - Выход \n\nВаша комманда: ")
print(f"Введенная команда: {command}")
print()

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
        numLines = notePrintEnumerate(noteId)

        commandChange = input("Введите комманду: \n 1 - Дополнить заметку \n 2 - Изменить заметку \nВаша комманда: ")
        if commandChange == "1":
            noteAppend = input("Введите текст, который вы хотите добавить: ")
            noteData = noteInBuffer(noteId)
            noteData[1] = f"{dateNow()}\n"
            with open(f"Notes/{noteId}.csv", "w", encoding="utf-8") as f:
                f.writelines(noteData)
                f.write(f"\n\n{noteAppend}")
                f.close()
                print("Заметка дополнена.")

        if commandChange == "2":

            noteLineChange = input("Введите номер строчки, которую Вы хотите заменить: ")
            try:
                noteLineChangeInt = int(noteLineChange)
                if noteLineChangeInt <= numLines and noteLineChangeInt > 1:
                    noteLineNew = input("Введите текст, на который вы хотите замент данную строчку: ")
                    noteData = noteInBuffer(noteId)
                    noteData[noteLineChangeInt] = f"{noteLineNew}\n"
                    noteData[1] = f"{dateNow()}\n"
                    with open(f"Notes/{noteId}.csv", "w", encoding="utf-8") as f:
                        f.writelines(noteData)
                        f.close()
                elif noteLineChangeInt <= 1:
                    print("Невозможно изменить id заметки и время её создания/изменения.")
                else:
                    print("Такой строчки в заметке нет, смотрите нумерация строк заметки.")
            except ValueError:
                print("Ошибка! Номер строчки должен быть числом.")



    else:
        print(f"Файла {noteId}.csv не существует.")



elif command == "4":
    print("Введенна  комманда 4.")
    noteDel()


elif command == "5":
    print("Введенна  комманда 5.")
else:
    print("Введенной комманды нет в списке.")


