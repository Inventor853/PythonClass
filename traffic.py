signal = input("Is the signal green? ")
road = input("Rate traffic 1-10: ")

road = int(road)

if signal == "yes":
    signal = 1
elif signal == "no":
    signal = 0

probability = signal/road

print(str(int(probability * 100)) + "% Chance to go outside")