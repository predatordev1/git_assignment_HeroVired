import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()

# TODO: Implement the feature to calculate the area of a circle
radius = 5
print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
