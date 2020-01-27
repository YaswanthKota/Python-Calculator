import re
print("THE CALCULATOR")
print("Type 'Quit' To Exit")
print("Multiply With Zero To Calculate New Equation\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter Equation To Calculate")
    else:
        equation= input(str(previous))
    if equation.lower()=="quit":
        print("Good Bye ,Man!")
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:()""]','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
