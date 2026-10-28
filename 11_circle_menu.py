import math

radius = 0

while True:
    print()
    print()
    print("0 = Exit")
    print("1 = Give radius")
    print("2 = Compute circumference of the circle")
    print("3 = Compute area of the circle")

    select = int(input("Select: "))

    if select == 1:
        radius = float(input("Give radius: "))
    elif select == 2:
        circumference = 2 * math.pi * radius
        print(f"Circumference is {circumference:.2f}")
    elif select == 3:
        area = math.pi * radius ** 2
        print(f"Area is {area:.2f}")
    else:
        break