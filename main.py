from noteDef import *

while True:
    command = input("Введите комманду: \n 1 - Создать замметку \n 2 - Открыть список заметок "
                    "\n 3 - Редактировать заметку \n 4 - Удалить заметку \n 5 - Выход \n\nВаша комманда: ")

    if command == "1":
        fileCreate()

    elif command == "2":
        commandPrintNotes = input("Введите комманду: \n 1 - Вывести все заметки.  "
                                  "\n 2 - Вывести только id, дату и заголовок всех заметок. "
                                  "\n 3 - Вывести заметку по id \nВаша комманда: ")
        if commandPrintNotes == "1":
            printNotes()
        elif commandPrintNotes == "2":
            printNotesIdDateTitle()
        elif commandPrintNotes == "3":
            printNoteById()
        else:
            print("Введенной комманды нет в списке.")

    elif command == "3":
        noteId = input("Введите id заметки, которую Вы хотите изменить: ")
        if os.path.exists(f"Notes/{noteId}.csv"):
            numLines = notePrintEnumerate(noteId)
            commandChange = input("Введите комманду: \n 1 - Дополнить заметку \n 2 - Изменить заметку \nВаша комманда: ")
            if commandChange == "1":
                noteAppend(noteId)
            if commandChange == "2":
                noteLineChange(noteId, numLines)
        else:
            print(f"Заметки с id:{noteId} не существует.")

    elif command == "4":
        noteDel()

    elif command == "5":
        print("Программа завершена.")
        break
    else:
        print("Введенной комманды нет в списке.")
