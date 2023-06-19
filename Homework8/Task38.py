file_path = "file.txt"


def show_all_records():
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            phonebook = line.replace(";", " ")
            print(phonebook, end="")


def search_record():
    fam = input("Введите фамилию: ")
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if fam.lower() in line.split(";")[0].lower():
                print(line, end="")


def add_contact():
    print("Введите данные контакта: ")
    fam = input("Фамилия: ")
    name = input("Имя: ")
    sec_name = input("Отчество: ")
    tel = input("Номер телефона: ")
    with open(file_path, 'a', encoding="utf-8") as f:
        f.writelines(fam + ";" + name + ";" + sec_name + ";" + tel + "\n")


def delete_contact():
    print("Введите фамилию и имя контакта который нужно удалить: ")
    fam = input("Фамилия: ")
    name = input("Имя: ")
    data = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if not (fam.lower() in line.split(";")[0].lower() and name.lower() in line.split(";")[1].lower()):
                data.append(line.strip())
    with open(file_path, 'w', encoding="utf-8") as f:
        for i in data:
            f.writelines(i + "\n")


def edit_contact():
    print("Введите фамилию и имя контакта который нужно редактировать: ")
    fam = input("Фамилия: ")
    name = input("Имя: ")
    data = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if not (fam.lower() in line.split(";")[0].lower() and name.lower() in line.split(";")[1].lower()):
                data.append(line.strip())
            else:
                print("Введите новые данные редактируемого контакта: ")
                fam_edit = input("Фамилия: ")
                name_edit = input("Имя: ")
                sec_name_edit = input("Отчество: ")
                tel_edit = input("Номер телефона: ")
                data.append(fam_edit + ";" + name_edit + ";" + sec_name_edit + ";" + tel_edit + "\n")
    with open(file_path, 'w', encoding="utf-8") as f:
        for i in data:
            f.writelines(i + "\n")


def main():
    print("Выберите действие:\n"
          "1 - показать справочник;\n"
          "2 - найти контакт;\n"
          "3 - редактировать справочник\n")
    select1 = int(input())
    if select1 == 1:
        show_all_records()
    elif select1 == 2:
        search_record()
    elif select1 == 3:
        print("Выберите действие:\n"
              "1 - добавить контакт;\n"
              "2 - удилить контакт;\n"
              "3 - редактировать контакт\n")
        select2 = int(input())
        if select2 == 1:
            add_contact()
        elif select2 == 2:
            delete_contact()
        elif select2 == 3:
            edit_contact()


main()
