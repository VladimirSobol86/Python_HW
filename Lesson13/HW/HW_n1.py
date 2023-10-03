

class NegativeValueError(Exception):
    def __init__(self, text):
        self.txt = text

class Rectangle:
        __slots__ = ('_width', '_height')

        def __init__(self, width: float, height: float = None):
            # if side_a <= 0 | side_b <= 0:
            #     raise ValueError
            self.width = width
            self.height = height
            if height is None:
                self._height = width

        @property
        def width(self):
            return self._width
        
        @property
        def height(self):
            return self._height
        
        @width.setter
        def width(self, value):
            if value > 0:
                self._width = value                              
            else:
                raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")

          

        @height.setter
        def height(self, value):
            if value > 0:
                self._height = value                              
            else:
                raise NegativeValueError(f"Высота должна быть положительной, а не {value}")       

        def __str__(self):
            return f'Прямоугольник со сторонами {self.width} и {self.height}'