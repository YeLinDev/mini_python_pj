import math
square = float(input("Type in the length of your square: "))
print(f"The area of the square is {square ** 2}.")
rectangle_w = float(input("Type in the length of your rectangle: "))
rectangle_l = float(input("Type in the width of your rectangle: "))
print(f"The area of the rectangle is {rectangle_w * rectangle_l}.")
radius = float(input("Type in the radius of your circle: "))
print(f"The area of the circle is { math.pi*radius**2 :.1f }.")