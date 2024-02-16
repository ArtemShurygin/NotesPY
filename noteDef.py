import datetime
import textwrap
import os.path

# Создает заметку
def fileCreate():
    id = Id()
    file = open(f"Notes/{id}.csv", "w")
    noteTitle = input("Введите заголовок заметки:\n")
    noteBody = input("Введите тело заметки:\n")
    file.write(f"id: {id} \n")
    file.write(f"{dateNow()}\n")
    file.write(f"{noteTitle} \n\n")
    file.write(f"{noteBody}")
    # Запись на диск (а не в буффер) во время работы программы
    file.flush()
    file.close()

    print("Заметка создана.")

# Выдает текущую дату в заданном формате
def dateNow():
    date = datetime.datetime.now()
    dateFormat = datetime.datetime.strftime(date, '%d-%m-%Y %H:%M:%S')
    return dateFormat

# Открывает файл с последним сохраненным id, и создает новый id увеличенный на 1
def Id ():
    with open("currentId.txt", "r") as f:
        currentIdStr = f.readline().strip('\n')
        currentIdInt = int(currentIdStr)
        newIdInt = currentIdInt + 1
        newIdStr = str(newIdInt)
        #print(f"Старый id: {currentIdStr}")
        #print(f"Новый id для текущего файла: {newIdStr}")
        f.close()
    with open("currentId.txt", "w") as f:
        f.write(newIdStr)
        f.close()
    return newIdStr


# Распечатывает заметку с переносом строки при достижении лимита символов в строке
def notePrint(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        noteRead = f.read()
        print(textwrap.fill(noteRead, break_long_words=False, replace_whitespace=False))
        f.close()

# Распечатывает заметку с переносом строки при достижении лимита символов в строке, номерует строки заметки
def notePrintEnumerate(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        for num, line in enumerate(f):
            print(textwrap.fill((str(num) + ": " + line.strip()), break_long_words=False,
                                replace_whitespace=False))
        f.close()
    return num

# Сохраняет содержимое файла в переменную
def noteInBuffer(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        noteData = f.readlines()
        f.close()
    return noteData

# Добавляет введенный текст в конец заметки
def noteAppend(noteId):
    noteAppend = input("Введите текст, который вы хотите добавить: ")
    noteData = noteInBuffer(noteId)
    noteData[1] = f"{dateNow()}\n"
    with open(f"Notes/{noteId}.csv", "w", encoding="utf-8") as f:
        f.writelines(noteData)
        f.write(f"\n\n{noteAppend}")
        f.flush()
        f.close()
        print("Заметка дополнена.")

# Заменяет текст выбранной строчки на введенный текст
def noteLineChange(noteId, numLines):
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
                f.flush()
                f.close()
            print("Заметка изменена.")
        elif noteLineChangeInt <= 1:
            print("Невозможно изменить id заметки и время её создания/изменения.")
        else:
            print("Такой строчки в заметке нет, смотрите нумерация строк заметки.")
    except ValueError:
        print("Ошибка! Номер строчки должен быть числом.")

#Удаляет заметку по введенному id
def noteDel():
    noteId = input("Введите id заметки, которую Вы хотите удалить: ")
    if os.path.exists(f"Notes/{noteId}.csv"):
        os.remove(f"Notes/{noteId}.csv")
        print(f"Заметка с id:{noteId} удалена.")
    else:
        print(f"Заметки с id:{noteId} не существует.")

# Сортирует файлы по дате изменения
def noteListSortDate():
    os.chdir("Notes/")
    notesList = sorted(filter(os.path.isfile, os.listdir(".")), key=os.path.getmtime)
    os.chdir("..")
    return notesList

# Выводит все заметки, отсортированные по дате изменения
def printNotes():
    notesList = noteListSortDate()
    for file in notesList:
        with open(f"Notes/{file}", "r", encoding="utf-8") as f:
            noteData = f.read()
            print(textwrap.fill(noteData, break_long_words=False, replace_whitespace=False))
            f.close()
        print("#####End of the note.#####")

# Выводит только id, дату измнения и заголовок заметок, отсортированных по дате изменения
def printNotesIdDateTitle():
    notesList = noteListSortDate()
    for file in notesList:
        with open(f"Notes/{file}", "r", encoding="utf-8") as f:
            noteData = f.readlines()
            f.close()
        numLines = len(noteData)
        print (numLines)
        if numLines >= 3:
            for i in range(3):
                print(noteData[i], end="")
        if numLines < 3:
            print(f"Файл {file} поврежден, отсутствуют ключевые строчки id, date, title.")
        print("#####End of the note.#####")

# Выводит заметку по введенному id
def printNoteById():
    noteId = input("Введите id заметки, которую вы хотитеты вывести: ")

    if os.path.exists(f"Notes/{noteId}.csv"):
        notePrint(noteId)
    else:
        print(f"Заметки с id:{noteId} не существует.")
