SOLITAIRE = 16.18
SINGLE_PARENT = 17.80
COHABIT = 13.76
CHILD_10_17 = 11.33
CHILD_UNDER_10 = 10.20

while True:
    new_data = input("New data (y/n): ")
    if new_data != "y":
        break

    adults = int(input("Adults in household (1/2): "))
    children = input("Any underage children (y/n): ")

    small_kids = 0
    big_kids = 0
    if children == "y":
        small_kids = int(input("Children less than 10 years: "))
        big_kids = int(input("Children 10-17 years: "))

    days = int(input("Days: "))

    if adults == 1:
        if children == "y":
            base = SINGLE_PARENT
        else:
            base = SOLITAIRE
    else:
        base = 2 * COHABIT

    daily = base + small_kids * CHILD_UNDER_10 + big_kids * CHILD_10_17
    total = daily * days

    print(f"Amount of the benefit is {total:.2f} euro")