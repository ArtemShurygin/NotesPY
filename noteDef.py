import datetime
import textwrap

def fileCreate():
    id = Id()
    file = open(f"Notes/{id}.csv", "w")
    noteTitle = input("Введите заголовок заметки:\n")
    noteBody = input("Введите тело заметки:\n")
    file.write(f"id: {id} \n")
    file.write(f"{dateNow()}\n\n")
    file.write(f"{noteTitle} \n\n")
    file.write(f"{noteBody}")
    file.close()
    print("Заметка создана.")

def dateNow():
    date = datetime.datetime.now()
    dateFormat = datetime.datetime.strftime(date, '%d-%m-%Y %H:%M:%S')
    return dateFormat

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


# Распечатывает заметку с переносом строки при достижении лимита символов в строке
def notePrint(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        noteRead = f.read()
        print(textwrap.fill(noteRead, break_long_words=False, replace_whitespace=False))
        f.close()

def notePrintEnumerate(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        for num, line in enumerate(f):
            print(textwrap.fill((str(num) + ": " + line.strip()), break_long_words=False,
                                replace_whitespace=False))
        f.close()
    return num

def noteInBuffer(noteId):
    with open(f"Notes/{noteId}.csv", "r", encoding="utf-8") as f:
        noteData = f.readlines()
        f.close()
    return noteData


