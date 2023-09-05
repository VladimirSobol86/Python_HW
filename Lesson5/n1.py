import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

print(parse_path('C:/Users/vsobol2/Desktop/Погружение в Python/HW/Lesson5/n2.py'))