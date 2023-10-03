import json
from exeptions import AccessError, LevelError, NameAccessError, IDAccessError

class User:
    def __init__(self, name: str, u_id:str, lvl:int):
        self.name = name
        self.u_id = str(u_id).zfill(6)
        self.lvl = int(lvl)
    
    def __str__(self):
        return f'Имя: {self.name} ({self.u_id}) | Уровень доступа: {self.lvl}'  
    
    def __repr__(self):
        return f'User ({self.name}, {self.u_id}, {self.lvl})' 
    
    def __hash__(self):
        return hash((self.name + self.u_id) * self.lvl)
    
    def __eq__(self, other):
        if not isinstance(other, User):
            raise TypeError
        return self.name == other.name and self.u_id == other.u_id
    
class Terminal:
    def __init__(self) -> None:
        self.user_base = Terminal.users_db()
    
    @staticmethod
    def users_db():
        users_list = set()
        with open('Lesson13/users.json', 'r', encoding='utf-8') as file:
            data_users = json.load(file)
        for lvl, users in data_users.items():
            for user in users:
                name, u_id = user
                users_list.add(User(name, u_id, lvl))
        return users_list

    def login(self, name: str, u_id: str):
        log_user = User(name, u_id, 0)
        users_name = [u_name.name for u_name in self.user_base]        
        if name in users_name:
            for cur_user in self.user_base:
                if cur_user == log_user:
                    return cur_user
                raise IDAccessError(name, u_id)
        raise NameAccessError(name)
    
    def create_new_user(self, log_user: User, new_user: User):
        if new_user.lvl < log_user.lvl:
            raise LevelError(log_user.lvl, new_user.lvl)
        user_dict = {}
        self.user_base.add(new_user)
        for user in self.user_base:
            if user.lvl in user_dict:
                user_dict[user.lvl].append([user.name, user.u_id])
            else:
                user_dict[user.lvl] = [[user.name, user.u_id]]
        with open('Lesson13/users.json', 'w', encoding='utf-8') as file:
            json.dump(user_dict, file, indent=4, ensure_ascii=False)
            return True
            
    def users(self):
        for user in self.user_base:
            print(user)

if __name__ == '__main__':
    
    user_base = Terminal()

    user_base.login('Владимир', '1')
#     print(login_user)
    login_user = User('Владимир', '1', 3)
    new_user = User('Новый12', '61', 1)
    print((login_user, new_user))
    user_base.create_new_user(login_user, new_user)
    # print(user_base.users_db())