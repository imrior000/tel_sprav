#1. Открыть справочник
#2. Сохраниить справончик
#3. Показть все контакты
#4. Создать контакт
#5. Найти контакт
#6. Изменить контакт
#7. Удалить контакт
#8. Выход
def read_book():
    with open("phone_book.txt", "r+", encoding="utf-8") as book:
        return book.readlines()
def unpak_str(str):
    str1 = str.split("\n")
    return str1[0].split('#*#')
def print_book(book):
    #print(*book)
    #book = book.split("\n")
    print("|-id-|-----------------data------------------|")
    for i in range(len(book)):
        print(*unpak_str(book[i]))
def add_contact():
    fio = input("Введите имя : ")
    number = input("Введите номер : ")
    coment = input("Введите коментарий : ")
    try:
        f = open("index.txt", 'r', encoding='utf-8')
        f.close()
    except FileNotFoundError:
        f = open("index.txt", 'w', encoding='utf-8')
        f.write(f"1\n")
        f.close()
    ind1 = open("index.txt", 'r', encoding='utf-8')
    ind = int(ind1.readline())
    ind1.close()
    book = open("phone_book.txt", "a+", encoding="utf-8")
    book.write(f'{ind}#*#{fio}#*#{number}#*#{coment}\n')
    book.close()
    ind1 = open("index.txt", 'w', encoding='utf-8')
    ind1.write(str(ind+1))
    ind1.close()
def search_book():
    pole = int(input(f'Выберите поле, по которому будем ускать : \n 1. Имя \n 2. Номер \n 3. Коментарий \n : '))
    book = read_book()
    book1 = [unpak_str(book[i]) for i in range(len(book))]
    ret = [];
    q = input("Введите строку поиска : ")
    for i in range(len(book1)):
        if q == book1[i][pole]:
            ret.append(f"{book1[i][0]}#*#{book1[i][1]}#*#{book1[i][2]}#*#{book1[i][3]}\n")
    print_book(ret)
    return ret
def read_all():
    book = read_book()
    print_book(book)
    return book
def delete_contact(number):
    book = read_book()
    q = open("phone_book.txt", 'w', encoding='utf-8')
    for i in range(len(book)):
        str = unpak_str(book[i])
        if int(str[0]) == number:
            pass
        else:
            q.write(f"{str[0]}#*#{str[1]}#*#{str[2]}#*#{str[3]}\n")
    q.close()

def edit_book(number_i):
    book = read_book()
    for i in range(len(book)):
        str = unpak_str(book[i])
        if int(str[0]) == number_i:
            fio1 = str[1]
            number1 = str[2]
            coment1 = str[3]
    fio = input(f"Введите имя [{fio1}]: ")
    if fio == "":
        fio = fio1
    print(fio)
    number = input(f"Введите номер [{number1}]: ")
    if number == "":
        number = number1
    print(number)
    coment = input(f"Введите коментарий [{coment1}]: ")
    if coment == "":
        coment = coment1
    print(coment)
    book = read_book()
    q = open("phone_book.txt", 'w', encoding='utf-8')
    for i in range(len(book)):
        str = unpak_str(book[i])
        if int(str[0]) == number_i:
            q.write(f"{str[0]}#*#{fio}#*#{number}#*#{coment}\n")
        else:
            q.write(f"{str[0]}#*#{str[1]}#*#{str[2]}#*#{str[3]}\n")
    q.close()
def contakt_menu(number):
    vybor = 1
    while bool(vybor):
        print("---------Contakt Menu---------")
        print("1", "Изменить контакт")
        print("2", "Удалить контакт")
        print("0", "Назад")
        vybor = int(input("Введите номер : "))
        if vybor == 1:
            edit_book(number)
        elif vybor == 2:
            delete_contact(number)
def main_menu():
    vybor = 1
    while bool(vybor):
        print("Телефонный справочник v0.1a")
        print("---------Menu---------")
        print("1", "Показать все контакты")
        print("2", "Найти контакт")
        print("3", "Создать контакт")
        print("0", "Выход")
        vybor = int(input("Введите номер : "))
        if vybor == 1:
            otv = read_all()
            ooo = int(input("Введите id строки для выбора : "))
            contakt_menu(ooo)
        elif vybor == 2:
            search_book()
            ooo = int(input("Введите id строки для выбора : "))
            contakt_menu(ooo)
        elif vybor == 3:
            add_contact()
        else:
            if vybor != 0:
                print("Такого пункта не существует!")
            else:
                print("До новых встреч!")
main_menu()
    