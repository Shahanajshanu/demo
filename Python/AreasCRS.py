def circle():
    print("You are choose circle......")
    radius = int(input("Enter the circle radius: "))
    print("Area of the circle with the radius", radius, "Unit is", 3.14 * (radius ** 2), "Square units.")


def square():
    print("You are choose square.....")
    side = int(input("Enter the side and size of the square: "))
    print("Area of the side of the square", side, "Unit is", side ** 2, "Square units: ")


def rectangle():
    print("You are choose rectangle....")
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the of the rectangle: "))
    print("Area of the rectangle is", length * breadth, "Square units")


print("Menu\n"
      "1. Circle\n"
      "2. Square\n"
      "3. Rectangle\n")


x = int(input("Enter the corresponding ares given in menu, whose areas you want be calculate: "))
if x == 1:
    circle()
elif x == 2:
    square()
elif x == 3:
    rectangle()
else:
    print("Invalid option you are selected: ")