class InvalidNumberError(Exception):
        def __init__(self, text):
            self.txt = text

class InvalidTextError(Exception):
        def __init__(self, text):
            self.txt = text
            
class Archive:
    def __init__(self, text: str, num):
        self.text = text
        self.num = num
               
        if isinstance(text, str) and len(text) != 0:
            self.text = text
        else:
            raise InvalidTextError('Invalid text: . Text should be a non-empty string.')    

        if (int(num) or float(num)) and num > 0:
            num = num
        else:
            raise InvalidNumberError(f'Invalid number: {num}. Number should be a positive integer or float.')                
        
    def __str__(self):
        return f'Text is {self.text} and number is {self.num}. Also [] and []'
# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)
# archive_instance = Archive("Sample text", 42.5)
# print(archive_instance)
invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)