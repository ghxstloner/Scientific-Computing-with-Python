class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, x):
        self.width = x

    def set_height(self, x):
        self.height = x

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height **2 ) ** .5
    
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture.'
        width = self.width
        height = self.height
        return ('*' * width + '\n') * height
    
    def get_amount_inside(self, other):
        if not isinstance(other, (Rectangle, Square)):
            raise TypeError("Argument must be an instance of Rectangle or Square class.")
        
        return self.get_area() // other.get_area()


    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __str__(self):
        return f"Square(side={self.width})"
