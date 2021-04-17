import sys

add = lambda num, num2: num + num2

subtract = lambda num, num2: num - num2

divide = lambda num, num2: num / num2

multiply = lambda num, num2: num * num2

symbols = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    '(': 'Start',
    ')': 'End'
}

orderOfOperations = {
    '(': 0,
    '*': 1,
    '/': 1,
    '+': 2,
    '-': 2
}

nums = '0123456789'

# Takes the expression
calculation = input('Calculation: ').split(' ')

expressionWithoutSpaces = '('

# Parse the expresssion
for character in calculation:
    if character != ' ':
        expressionWithoutSpaces += character

expressionWithoutSpaces += ')'

if expressionWithoutSpaces.count('(') != expressionWithoutSpaces.count(')'):
    print('You have put an incorrect statement. The statement has a different number of open paranthesis as close paranthesis.')
    sys.exit()

listOfExpressions = []

number = ''
for character in expressionWithoutSpaces:
    if character not in nums and not symbols.get(character):
        print(f'{character} is not valid.')
        sys.exit()
    if character not in nums:
        if number != '':
            listOfExpressions.append(number)
        number = ''
        listOfExpressions.append(symbols.get(character))
        continue
    number += character

if number != '':
    listOfExpressions.append(number)

def chunk(startIndex, endIndex, listOfExpressions):
    listOfItems = []
    print(startIndex, endIndex)
    listOfItems = listOfExpressions[startIndex + 1: endIndex - 1]
    if "Start" not in listOfItems:
        result = listOfItems[1](int(listOfItems[0]), int(listOfItems[2]))
        del listOfExpressions[startIndex: endIndex + 1]
        listOfExpressions.insert(startIndex, result)
        parse(listOfExpressions)
    else:
        parse(listOfItems)

def parse(listOfItems):
    startIndex = ''
    endIndex = ''
    print(listOfItems)
    for element in listOfItems:
        if element == 'Start':
            startIndex = listOfItems.index(element)
        if element == 'End':
            endIndex = len(listOfItems) - listOfItems[::-1].index(element)
        if startIndex != '' and endIndex != '':
            chunk(startIndex, endIndex, listOfItems)
    
parse(listOfExpressions)
print(listOfExpressions)