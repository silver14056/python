import os


def get_id():
    filepath = "id.txt"
    if not os.path.exists(filepath):
        set_id(0)
        return get_id_note()
    else:
        empty = is_csv_empty(filepath)
        if empty:
            set_id(0)
            return get_id_note()
        else:
            return get_id_note()


def is_csv_empty(filepath):
    with open(filepath, 'r') as f:
        try:
            f.readline()
        except EOFError:
            return True

    return False


def get_id_note():
    with open("id.txt") as file:
        return int(file.read())


def set_id(id_note):
    with open("id.txt", 'w') as file:
        file.write(str(id_note))
