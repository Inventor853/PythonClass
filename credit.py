import sys

def add_digits(sum, group):
    for number in group:
        number = str(number)
        for digit in number:
            digit = int(digit)
            sum += digit
    return sum

credit = input("Credit Card Number: ")

try:
    credit = int(credit)
except:
    print("This number is invalid")
    sys.exit(1)

credit = str(credit)

group1 = []
group2 = []

group = True

for digit in credit:
    digit = int(digit)
    if group:
        group1.append(digit)
        group = False
    else:
        group2.append(digit)
        group = True

for i in range(len(group1)): 
    group1[i] *= 2

sum = 0

sum = add_digits(sum, group1)
sum = add_digits(sum, group2)

if sum%10 == 0:
    print("This credit card is valid!")
else:
    print("This number is invalid")