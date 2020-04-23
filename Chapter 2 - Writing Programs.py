''' Topics to be covered:
Strings
String Concatenation
Data Types (Strings and Integers)
Using the File Editor to write programs
Saving and Running programs in IDLE
Flow of Execution
Comments
The print() function
The input() function
Case sensitivity
'''

#Text values are called Strings, can be stored in variables as well
print("Example of String being Stored in variable: ------------")
print("spam = 'Hello' ")
spam = 'Hello'
print(spam)
print("\n")

print("Examples of Strings: --------------")
#Even numbers can be represented as strings, these numbers are NOT integers
print('Hello world!')
print('KITTENS')
print('12345_hi')
print('12303429iiojfjxcn,zsdfg')
print("\n")

#String Concatination: combining two strings with the + operator
print("Example of Concatination: --------------")
print(" 'Hello' ' + ' 'World!' ")
print('Hello ' + 'World!')
print("\n")

#All values have data types
#+ operator works differently for Integers and Strings as they are different types

#Creating the Hello World program:------------------------------------
print("Example Program, says hello world and asks for name: -----------")
#Source-code: instructions Python will follow when the program runs

#This program says hello and asks for my name.
def program():
    print('Hello World!')
    print('What is your name?')
    myName = input()
    print('It is good to meet you, ' + myName)

program()
print("\n")

#input() asks for the user to put something into the consol, saves the input
#def methodName(): makes a method by the name of methodName.

''' Chapter 2 summary
Understanding Strings and Functions(Methods) lets you interact with the user
Text is the main way programs interact with the user
input() asks for the user's input, saves it as a string
print() lets you print into the consol, display text on the consol
Strings are just a data type used to handle text
'''

print("Chapter 2 summary: -------------------")
print("\nUnderstanding Strings and Functions(Methods) lets you interact with the user \nText is the main way programs interact with the user \ninput() asks for the user's input, saves it as a string \nprint() lets you print into the consol, display text on the consol \nStrings are just a data type used to handle text")
