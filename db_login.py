import os
from app import db, Product, app

app.app_context().push()


def save_to_db(record):
    login = record[0]
    mail = record[1]
    password = record[2]

    product = Product(login=login, mail=mail, password=password)

    # try:
    db.session.add(product)
    db.session.commit()
    # except:
    # print("При добавлении статьи прозошла ошибка")
    # print() #::::


folder = r"C:\Users\sebab\PycharmProjects\Webb\static\pic"
paths = os.listdir(folder)


def fill(file):
    """
    функция извлекает из файла в массив по разделителю enter

    """
    f = open(file)
    str1 = f.read()
    res = str1.split("\n")
    f.close()
    return res


list_folders = []

for i in range(len(paths)):
    if os.path.isdir(folder + "\\" + paths[i]):
        list_folders.append(folder + "\\" + paths[i])

for i in range(len(list_folders)):
    f = list_folders[i]
    lst_f = os.listdir(f)

    if "description" in lst_f:
        descr = os.listdir(f + "\\description")
        arr_desr_brand = []
        for j in range(len(descr)):
            file = f + "\\description\\" + descr[j]
            arr_desr_brand.append(fill(file))

            # print(file)
        # print(arr_desr_brand) #тут будем записывать базу данных

        for elem in range(len(arr_desr_brand)):
            save_to_db(arr_desr_brand[elem])

        print()
