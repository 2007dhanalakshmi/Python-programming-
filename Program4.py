# Program 4 - Area of Various Shapes using Functions

def square():
    s = int(input("Enter side of the square: "))
    a = s * s
    print("Area of Square =", a)

def rectangle():
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    a = l * b
    print("Area of Rectangle =", a)

def circle():
    r = float(input("Enter radius: "))
    a = 3.14 * r * r
    print("Area of Circle =", a)

def triangle():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    a = 0.5 * b * h
    print("Area of Triangle =", a)

while True:
    print("\n1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        square()
    elif ch == 2:
        rectangle()
    elif ch == 3:
        circle()
    elif ch == 4:
        triangle()
    elif ch == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")

  
