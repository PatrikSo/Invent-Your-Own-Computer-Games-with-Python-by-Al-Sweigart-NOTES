''' Topics to be covered:
Operators
Integers and Floating-point numbers
Values
Expressions
Syntax errors
Storing values in variables
'''
print("Example of Operator usage in Python: ------------")
def mathOperatorsExample(x, y):
    print("x + y =" , x + y) #Addition
    print("x - y =" , x - y) #Subtraction
    print("x / y =" , x / y) #Division
    print("x * y =" , x * y) #Multiplication

mathOperatorsExample(5, 10)

#Operators tell python what to do with the numbers sorrounding them
#Integers are whole numbers, such as 4, 99 and 0
#Floating-point numbers (floats) are fractions or numbers with decimal points
#Any of these are examples of values

#Expressions are how we handle values with operators (example: 2 + 2)
print("Examples of Expressions: ---------------")
print("2 + 2 + 2 + 2 =" , 2 + 2 + 2 + 2)
print("8*6 =" , 8*6)
print("10-5+6 =" , 10-5+6)
print("2 +       2 =" , 2 +       2)

#Parts of the expression inside parentheses are evaluated first
#Multiplication and division are done before addition and substraction
#The evaluation is performed left to right

#SyntaxError means Python didn't understand your instruction due to typing something incorrectly
print("Example of a SyntaxError: ----------------")
print("5 + ")
print("Uncompleted expressions ^^^^^^")

#Variables hold values, like a box that can hold something
#Assignment Statement stores a value into the variable, like an instruction to put something into the box you made
# '=' is an assignment operator, it assigns
print("Example of an assignment operator putting a value in a variable: --------------------------")
spam = 15
print("spam = 15")
print(spam)
print("spam = spam + 5")
print(spam + 5)

#NameError appears when you don't use the correct variable names in operations

'''
Chapter 1 Summary:
Learned basics of writing instructions in Python.
Expressions are values combined with operators.
Python evaluates your expressions into a single value
You can store values into variables so that your program remembers given value
'''
print("Chapter 1 Summary: \n Learned basics of writing instructions in Python.  \nExpressions are values combined with operators. \nPython evaluates your expressions into a single value \nYou can store values into variables so that your program remembers given value.")
