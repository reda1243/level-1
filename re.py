Num1 = float(input("enter number one "))
operetor = input("enter operetor ")
Num2 = float(input('enter number two '))
def number(Num1,Num2,operetor):
    if operetor == "+":
        print(Num1 + Num2)
        
    elif operetor == "-":
        print(Num1 - Num2)
    elif operetor == "*":
        print(Num1 * Num2)
    elif operetor == "/":
        print(Num1 / Num2)
    elif operetor == '%':
        print(Num1 % Num2)
    elif operetor is not "+"and"/"and"+"and"*"and"%":
        print('opertor not true use + or - or * or / or %')
number(Num1,Num2,operetor)
        
        
