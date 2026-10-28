name=input("GIve your name: ")
height=float(input("GIve height in meters: "))
weight=float(input("GIve Weight in kgs: "))
bmi= weight / (height * height)

print(f"your name is {name}, and you are {height}m tall, and your weight is {weight}kg." )
print(f"your bim is {bmi:.2f} ")