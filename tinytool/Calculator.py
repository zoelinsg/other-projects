# Calculator
import re 
print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run  = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation  = input("Enter equation:") #輸入方程式
    else:
        equation = input(str(previous)) #可以繼承

    if equation == 'quit': #輸入quit後結束程式
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()+" "]','',equation)
        
        if previous == 0:
            previous = eval(equation) 
        else:
            previous = eval(str(previous)+equation)

        #print("You Typed",previous)

while run:
    performMath()  