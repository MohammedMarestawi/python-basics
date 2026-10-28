temperature = float(input("Give temparature: "))
if  temperature > 39:
    print("Too hot")
elif  10 < temperature <= 39  :
    print("Warm")
elif 0 <= temperature <= 10 :
    print("Moderate")
elif -30 <= temperature <0 :
    print("Freezing")
else:
    print("Too cold")