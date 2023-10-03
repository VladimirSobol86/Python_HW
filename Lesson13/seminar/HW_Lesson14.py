from classes import User, Terminal
from exeptions import NameAccessError, LevelError
import unittest

class TestSample(unittest.TestCase):
    
    def setUp(self):
        self.login_user = User('Владимир', '000001', 3)
    
    def test_level_error(self):
        new_user = User('Новый12', '000061', 1)
        self.assertRaises(LevelError, Terminal().create_new_user, self.login_user, new_user)
        
    def test_name_access_error(self):
        self.assertRaises(NameAccessError, Terminal().login, 'Антон', '8')
        print('done')
        
    def test_success_login(self):
        self.assertTrue(Terminal().login('Владимир', '000001'))
        
    def test_success_creation_user(self):
        new_user = User('Новый25', '000022', 4)
        self.assertTrue(Terminal().create_new_user(self.login_user, new_user))      
        
if __name__ == '__main__':
    unittest.main()