import math


class Point:
    global x
    global y


    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def print_attributes(self):
        print("Point x =", self.x)
        print("Point y =", self.y)


def distance(point_one: Point, point_two: Point):
    x_coordinate_difference = point_two.x - point_one.x
    y_coordinate_difference = point_two.y - point_one.y

    # Calculate difference between points using the formula - sqrt((x1 - x2)^2 + (y1 - y2)^2)
    result = math.sqrt(x_coordinate_difference ** 2 + y_coordinate_difference ** 2)
    return result


print("Enter values for 1st point")
x_coordinate_one = int(input("Enter the value of x coordinate: "))
y_coordinate_one = int(input("Enter the value of y coordinate: "))

point_initial = Point(x_coordinate_one, y_coordinate_one)

print("Enter values for 2nd point")
x_coordinate_two = int(input("Enter the value of x coordinate: "))
y_coordinate_two = int(input("Enter the value of y coordinate: "))

point_final = Point(x_coordinate_two, y_coordinate_two)

print("Your entered points are: ")
print("Point 1: ")
point_initial.print_attributes()
print("Point 2: ")
point_final.print_attributes()

print("Distance between the two points: ", distance(point_initial, point_final))
