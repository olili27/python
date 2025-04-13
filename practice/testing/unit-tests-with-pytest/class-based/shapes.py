class Shape:
    def area(self):
        ...
    

    def perimeter(self):
        ...

    
    def number_of_sides(self):
        ...


class Rectangle(Shape):
    def __init__(self, length: int | float, width: int | float) -> None:
        if length == width:
            raise ValueError("Rectangle cannot have length equal to width")
        
        self.__length = length
        self.__width = width
        self.__number_of_sides = 4

    def get_length(self) -> int | float:
        return self.__length

    def get_width(self) -> int | float:
        return self.__width

    def set_length(self, length: int | float) -> None:
        self.__length = length

    def set_width(self, width: int | float) -> None:
        self.__width = width

    def area(self) -> int | float:
        return self.__length * self.__width

    def perimeter(self) -> int | float:
        return (self.__length * 2) + (self.__width * 2)
    

    def number_of_sides(self) -> int:
        return self.__number_of_sides
    
    def has_equal_sides(self) -> bool:
        return self.__length == self.__width


class Square(Rectangle):
    def __init__(self, side_length: int | float):
        super().__init__(side_length, side_length)

    def set_length(self, length: int | float) -> None:
        self.__length = length
        self.__width = length

    def set_width(self, width: int | float) -> None:
        self.__width = width
        self.__length = width


