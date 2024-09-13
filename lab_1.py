import math
import numpy as np

def menu(): 
    while True:
        print(" Menu: ")
        print(" 1. Task 1 ")
        print(" 2. Task 2")
        print(" 3. Task 3")
        print(" 4. Exit ")
        
        choice = input(" Select a task: ")
        
        if choice == '1':
            task_integer5()
        elif choice == '2':
            task_math41()
        elif choice == '3':
            task_boolean12()
        elif choice == '4':
            print(" Exit!")
            break
        else:
            print(" Wrong choice. Please select again.")
            
def task_integer5():
    try:
        #input values A and B
        A = float(input(" A = "))
        B = float(input(" B = "))
    except ValueError: #error notification
        print(" The value may be numeric!")
        input(" Press enter to choose another task ")
    else:
        if A > B:
            result = A % B
            # output result
            print(" The length of the unoccupied part A:" , result )
        else:
            print(" A must be greater than B")
            
def task_math41():
    
    try: 
        # input x
        x = float(input(" x = ")) 
        
        if x >= 0:
            # First expression
            term1 = (np.cbrt(x) + math.sqrt(abs(x)**3)) / (math.log2(np.sin((abs(x)**2))**2))
        
            # Second expression
            term2 = (2 * math.pi * abs(np.tan(x))) / 12

            # The sum of both expressions to obtain the value of y
            y = term1 + term2
            # output result
            print(" The value of y at x = ", x ," :" , y)
        else:
            print ("Error")
            
    except ValueError: #error notification
        print(" Input error! x must be a number.")
        
def task_boolean12():
    
    try:
        #input A, B and C
        A = int(input(" A = "))
        B = int(input(" B = "))
        C = int(input(" C = "))
        if A > 0 and B > 0 and C > 0:
            print(" All of the numbers A, B, C are positive.")
        else:
            print( " Some of the numbers are negative: ")
            if A <= 0:
                print(" A < 0 ")
            if B <= 0:
                print(" B < 0 ")
            if C <= 0:
                print(" C < 0 ")
    
    except ValueError: #error notification
        print("A must be an integer!")
        input("Press enter to choose another task ")

menu()        
