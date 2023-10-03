class UserException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
class LevelError(UserException):
    def __init__(self, log_level, new_level):
        super().__init__(f'Ошибка уровня доступа! Ваш уровень {log_level} меньше требуемого '
                         f'для создания пользователя уровня {new_level}')
        
class AccessError(UserException):
    def __init__(self, msg: str = ''):
        self.msg = 'Ошибка доступа!' + ' ' + msg
        super().__init__(self.msg)

class NameAccessError(AccessError):
    def __init__(self, name: str):
        self.msg = f'Пользователя с именем {name} нет в базе'
        super().__init__(self.msg)

class IDAccessError(AccessError):
    def __init__(self, name: str, u_id: str):
        self.msg = f'Имя {name} не совпадает с ID: {u_id}'
        super().__init__(self.msg)
