from sys import exit
from math import log

op = input("***************************\n   Super Cool Calculator\n---------------------------\nadd  | Addition\nsub  "
           "| Subtraction\nmul  | Multiplication\ndiv  | ""Division\nexp  | Exponentiation\nsqrt | Radical\nlog  | "
           "Logarithm\n***************************\n>> ")

n1 = "p"
n2 = "y"


def numbercheck(a, b):
    global n1, n2
    while type(n1) is str or type(n2) is str:
        n1 = input(a)
        n2 = input(b)
        try:
            n1 = float(n1)
            n2 = float(n2)
            if n1 == int(n1):
                n1 = int(n1)
            if n2 == int(n2):
                n2 = int(n2)
        except ValueError:
            print("That's not a number")


if op == "add":
    numbercheck("Term 1\n>> ", "Term 2\n>> ")
    print(n1, "+", n2, "=", n1 + n2)
elif op == "sub":
    numbercheck("Term 1\n>> ", "Term 2\n>> ")
    print(n1, "-", n2, "=", n1 - n2)
elif op == "mul":
    numbercheck("Factor 1\n>> ", "Factor 2\n>> ")
    print(n1, "*", n2, "=", n1 * n2)
elif op == "div":
    numbercheck("Numerator\n>> ", "Denominator\n>> ")
    if n2 == 0:
        print("ERROR: You can't divide by zero.")
        exit()
    n3 = n1 / n2
    if n3 == int(n3):
        n3 = int(n3)
    print(n1, "/", n2, "=", n3)
elif op == "exp":
    numbercheck("Base\n>> ", "Exponent\n>> ")
    if n1 < 0 and n2 != int(n2):
        print("ERROR: This will result in an imaginary number.")
        exit()
    print(n1, "^", n2, "=", n1 ** n2)
elif op == "sqrt":
    numbercheck("Radicand\n>> ", "Degree\n>> ")
    if n1 < 0:
        print("ERROR: This will result in an imaginary number.")
        exit()
    n3 = n1 ** (1 / n2)
    if n3 == int(n3):
        n3 = int(n3)
    print("The", n2, "root of", n1, "equals", n3)
elif op == "log":
    numbercheck("Number\n>> ", "Base\n>> ")
    if n1 < 0 or n2 < 0:
        print("ERROR: This will result in an imaginary number.")
        exit()
    if n2 == 1:
        print("ERROR: A logarithm of base 1 is not possible.")
        exit()
    n3 = log(n1, n2)
    if n3 == int(n3):
        n3 = int(n3)
    print("The logarithm base", n2, "of", n1, "equals", n3)
else:
    print("ERROR: Not a valid operation.")
    exit()
