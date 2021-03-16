
Num1 = float(input(' : '))
Opertor = input('Enter opertor')
Num2 = float(input(' : '))

#this fontion for Addition
if Opertor is '+':
    def Add(Num1,Num2,opertor):
        if opertor == "+":
            return Num1 + Num2
    print(Add(Num1,Num2,Opertor))

#this fontion for Subtraction
elif Opertor is "-":
    def Sub(Num1,Num2,opertor):
        if opertor == "-":
            return Num1 + Num2
    print(Sub(Num1,Num2,Opertor))

#this fonction for Multiplication
elif Opertor is "*":
    def Mult(Num1,Num2,opertor):
        if opertor == "*":
            return Num1 + Num2
    print(Mult(Num1,Num2,Opertor))

#this fonction for Division
elif Opertor is "/":
    def Div(Num1,Num2,opertor):
        if opertor == "/":
            return Num1 + Num2
    print(Div(Num1,Num2,Opertor))