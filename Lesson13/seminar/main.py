import os
import json
from classes import User

MIN_LVL = 1
MAX_LVL = 7

def create_json(path: str = 'Lesson13/users.json'):
    user_data = {}
    id_list =[]
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as file:
                user_data = json.load(file)
        if user_data:
            for users in user_data.values():
                for user in users:
                    id_list.append(user[1])
        name = input("Введите имя пользователя: ")
        if not name:
            break
        while True:
            u_id = input("Введите личный ID: ")
            if u_id.isdigit():
                if int(u_id) not in id_list:
                    u_id = int(u_id)
                    break
                else:
                    print(f'ID {u_id} уже занят. Введите другой ID.')
            else:
                print('ID должен быть целым числом')
        while True:
            u_lvl = input("Введите уровень доступа: ")
            if u_lvl.isdigit() and MIN_LVL <= int(u_lvl) <= MAX_LVL:
                break
            else:
                print(f'Уровень доступа должен быть от {MIN_LVL} до {MAX_LVL}')

        if u_lvl in user_data:
            user_data[u_lvl].append((name, u_id))
        else:
            user_data[u_lvl] = [(name, u_id)]

        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(user_data, file, indent=6, ensure_ascii=False)

def load_users():
    users_list = set()
    with open('Lesson13/users.json', 'r', encoding='utf-8') as file:
        data_users = json.load(file)
    for lvl, users in data_users.items():
        for user in users:
            name, u_id = user
            users_list.add(User(name, u_id, lvl))
    return users_list

if __name__ == '__main__':
    create_json()
    # data = load_users()
    # print(data)