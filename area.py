import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()

radius = float(input("Enter the radius of circle: "))
print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
<<<<<<< HEAD

=======
>>>>>>> 9e69b1e (bug fixed)
 
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
<<<<<<< HEAD

=======
>>>>>>> 9e69b1e (bug fixed)
