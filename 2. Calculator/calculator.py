#This is my first project ever! Went through W3school and jumped straight into that project. 

#So here is my first ever project, a very simple calculator that does only 1 operation. 

def get_number(prompt):                                 #ask the user for a single number
    while True:
        try:
            number = float(input(prompt))               #handles exceptions, in this case if it's not a number, we type try so that the programm
            return number                               #tries something and instead of crashing, if it doesn't work we go to the except line, perform
        except ValueError:                              #what's written under that line and we try again since it's an infinite while loop.    
            print("Invalid input! Please enter a number.")

def format_result(result):                              # we format the result to be an int if it's not a decimal number. So that the output is not 2.00 when
    if result == int(result):                           # it's 2
        return int(result)
    else:
        return result

def addition(x, y):
 return x + y

def substraction(x, y):                                 # these are functions that perform an operation on the number
    return x - y

def multiply(x, y):
    return x * y

def divide (x, y):
   if y != 0: 
    return x / y
   else:
    return "Error: Division by zero is not allowed." 


i = True                                                # the whole code is wrapped in a while loop so that the user can make another operation if he
                                                        # desires.   
while i:

    num1 = get_number("Enter your first number: ")
    
    num2 = get_number("Enter your second number: ")
    


    


    operation = input("Enter either +, -, * or /: ")                   # we ask the user to enter an operator that checks if it fits the symbols             
    while operation not in ('+', '-', '*', '/'):
        print("Invalid operator!")
        operation = input("Please enter either +, -, * or /: ")

    if operation == '+':                                                #this is where we call the functions that perform the calculation
        
        result = addition(num1, num2)

    if operation == '-':
        
        result = substraction(num1, num2)

    if operation == '*':
        
        result = multiply(num1, num2)

    if operation == '/':
        
        result = divide(num1, num2)


    result = format_result(result)                                   #and we print the final result

   
     
    print("The result is: ", result)

        
 
     

    while True:                                                                         #this is where we ask the user if he wants to make another operation
     question1 = input("Do you want to make another calculation? (Type Y or N): ")
     if question1.upper() == 'Y':
        i = True
        break  
     elif question1.upper() == 'N':
        i = False
        break  
     else:
        print("Invalid input! Please enter either Y or N.")
 