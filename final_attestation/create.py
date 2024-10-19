from datetime import datetime


def create_note():
    print("--------------------------------------------------")
    id_note = 1
    title = input("Введите заголовок заметки:")
    note_body = input("Напишите вашу заметку:")
    date_time_create = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M")
    with open("notes.csv", "a", encoding="utf-8") as f:
        f.write(f"{id_note};{title};{note_body};{date_time_create}\n")
