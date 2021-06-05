def main(input):
    if not input.isnumeric():
        return "This is not a number"
    number = int(input)
    if number % 2 == 0:
        return "This is an even number"
    return "This is an odd number"

print(main(input("What is your input?\n")))