from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

title = contacts_list.pop(0)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def parser(row):
    regex = r'\D*(7|8)?\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)(\s)?[\s\(]*(доб.)?\D*(\d+)?[\s\)]*'
    subst = r'+7(\2\3\4)\5\6\7-\8\9-\10\11\12\13\14'

    full_name = ' '.join(row[:3])
    lastname, firstname, surname = full_name.split(' ')[:3]
    organization, position = row[3:5]
    phone = re.sub(regex, subst, row[5])
    email = row[6]

    return [lastname, firstname, surname, organization, position, phone, email]

def merge(source, receiver):
    for i in range(2, len(receiver)):
        if receiver[i] == '':
            receiver[i] = source[i]

new_contacts_list = list()
new_contacts_list.append(title)
for contact in map(parser, contacts_list):
    contact_in_list = False
    for new_contact in new_contacts_list:
        if contact[0] == new_contact[0] and contact[1] == new_contact[1]:
            if contact[2] == '' or new_contact[2] == '':
                contact_in_list = True
                merge(contact, new_contact)
                break
            elif contact[2] == new_contact[2]:
                contact_in_list = True
                merge(contact, new_contact)
                break
    if not contact_in_list:
        new_contacts_list.append(contact)
        
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)