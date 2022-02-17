def circle():
    print("You choose circle......")
    radius = int(input("Enter the radius: "))
    print("Area of the circle with the radius of", radius, "Units is", 3.14 * (radius ** 2), "Square Units")

def square():
    print("You choose square.....")
    side = int(input("Enter the size and side of a square: "))
    print("Area of square with the side of", side, "Unit is", side ** 2, "Square Units.")

def rectangle():
    print("You choose rectangle....")
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    print("Area of rectangle with length and breadth", length * breadth, "Square Units.")

print("Menu\n"
      "1. Circle\n"
      "2. Square\n"
      "3. Rectanglr\n"
      "")

x = int(input("Enter the corresponding no.of the shape given in the menu, whose area you wants to calculate: "))
if x == 1:
    circle()
elif x == 2:
    square()
elif x == 3:
    rectangle()
else:
    print("Wrong Input!")

