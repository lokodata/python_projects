'''
Goal: Create a calculator that can add, subtract, multiply, and divide

function calculator (will get all input)
function add (will add two numbers if "+" is entered)
function multiply (will multiply two numbers if "*" is entered)
function subtract (will subtract two numbers if "-" is entered)
function divide (will divide two numbers if "/" is entered)
'''


def multiply(num1, num2):  # multiply function
    return float(num1) * float(num2)


def divide(num1, num2):  # divide function
    return float(num1) / float(num2)


def add(num1, num2):  # add function
    return float(num1) + float(num2)


def subtract(num1, num2):  # subtract function
    return float(num1) - float(num2)


def calculator():  # calculator function
    expression = input('Enter a calculation: \n')

    '''
    I want to get an expression '15+15' or '15 - 15' and split it into a list
    ['15', '+', '15']
    '''
    expression_list = []
    expression_number = ''

    for char in expression:
        # if the char is a number, add it to the expression_number string so '45' will be like '4' then '4' + '5' = '45'
        if char.isdigit():
            expression_number += char

        # if the char is a space, check if the expression_number string has a number in it
        elif char.strip():
            # if it does, add it to the expression_list
            if expression_number:
                expression_list.append(expression_number)
                # this is to reset the expression_number string
                expression_number = ''
            # this is to add the operator to the list
            expression_list.append(char)

    # this is to add the last number to the list
    if expression_number:
        expression_list.append(expression_number)

    '''
    I want to check what is the operator so I can call the right function
    Currently it is on the second index of the list
    '''

    operators = ['*', '/', '+', '-']

    if expression_list[1] == operators[0]:
        return multiply(expression_list[0], expression_list[2])
    if expression_list[1] == operators[1]:
        return divide(expression_list[0], expression_list[2])
    if expression_list[1] == operators[2]:
        return add(expression_list[0], expression_list[2])
    if expression_list[1] == operators[3]:
        return subtract(expression_list[0], expression_list[2])


print(calculator())

'''
Current: Can only do calculations with two numbers and one operator

To be added / fixed:

- Add a while loop so the user can keep entering calculations
- Add a way to check if the user entered a valid expression
    - Expression should not end with an operator
    - Expression cannot consist of any letters or anything outside the operators
    - Expression cannot have two operators in a row
    - Expression cannot have two numbers in a row
- Add a way to check if the user entered a valid number
    - Number cannot have two decimal points
- Add a way to get multiple expressions at once
- Add a way to implement PEMDAS
- Add other operator 'x' and ',' and '()'
- Add a way to input a negative number and fractions
'''
