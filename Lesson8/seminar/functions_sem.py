import os
import json
import csv
import pickle
#1 
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
def create_new_json(list_, file_path):
    with open('Lesson8/seminar/results.txt', 'r', encoding='utf-8') as f:
        dict_ = dict()
        names = f.readlines()
        for name in names:
            name = name.strip().split(' -> ')
            dict_[name[0]] = float(name[1])
        print(dict_)
    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(dict_, f, indent=4, ensure_ascii=False)

# if __name__ == '__main__':
#     list_to_write = None
#     create_json(list_to_write, os.path.join(os.getcwd(), 'first_json.json'))

#2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
def create_json(path: str = 'users.json'):
    users_data = {}
    id_list = []
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
        if users_data:
            for users in users_data.values():
                for user in users:
                    id_list.append(user[1])
        name = input('Введите имя пользователя: ')
        if not name:
            break
        while True:
            u_id = input('Введите личный ID: ')
            if u_id.isdigit():
                if int(u_id) not in id_list:
                    u_id = int(u_id)
                    break
                else:
                    print(f'ID {u_id} уже занят. Введите другой ID')
            else:
                print('ID должен быть целым числом')
        while True:
            u_lvl = input('Введите уровень доступа: ')
            if u_lvl.isdigit() and 0 < int(u_lvl) < 8:
                break
            else:
                print(f'Уровень доступа должен быть от 1 до 7')
        if u_lvl in users_data:
            users_data[u_lvl].append(name, u_id)
        else:
            users_data[u_lvl] = [(name, u_id)]
        with open (path, 'w', encoding='utf-8') as file:
            json.dump(users_data, file, indent=4, ensure_ascii=False)

# if __name__ == '__main__':
#     create_json()

#3
#Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
def json_to_csv(json_path, csv_path):
    with (open(json_path, 'r', encoding='utf-8') as json_file,
          open(csv_path, 'w', encoding='utf-8') as csv_file):
        data: dict[str, list[list[str,int]]] = json.load(json_file)
        users_list = []
        for u_lvl, users in data.items():
            for user in users:
                users_list.append((user[0], user[1], u_lvl))
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=' ', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(('Имя', 'User ID', 'Level access'))
        csv_writer
        csv_writer.writerows(users_list)

# if __name__ == '__main__':
#     json_to_csv('users.json', 'users.csv')

#4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. 
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
def csv_to_json(csv_path: str = 'users.csv', json_path: str = 'hash_users.json'):
    with (open (csv_path, 'r', encoding='utf-8') as csv_file,
          open (json_path, 'w', encoding='utf-8') as json_file):
        data = csv_file.readlines()
        users_data = {}
        for i in range(len(data)):
            if i and data[i] != '\n':
             user = data[i].strip().replace('"', '').split()
             user[1] = f'{user[1]:0>10}'
             u_hash = str(hash(user[0]+user[1]))
             users_data[u_hash] = user
        json.dump(users_data, json_file, indent=4, ensure_ascii=False)
    print(users_data)

# if __name__ == '__main__':
#     csv_to_json()

#5
#Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith('.json'):
                file_list.append(os.path.join(files[0], file))
    for file in file_list:
        with (open(file.rsplit('.', 1)[0] + '.pickle', 'wb') as data,
              open(file, 'r', encoding='utf-8') as json_file):
            users_file = json.load(json_file)
            pickle.dump(users_file, data)

# if __name__ == '__main__':
#     json_to_pickle()