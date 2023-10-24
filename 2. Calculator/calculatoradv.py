#I wanted to make one where the user could do multiple operations in a row like 2 + 4 - 7. The other 
#calculator would just not allow the user to do that. It would stop after 1 operation. 

#Gonna make some function that perform diverse operations like asking for a number
#asking for an operator and performing the operation.
def getNumber(prompt):
    while True:         
        try:
            return float(input(prompt))
        except ValueError:
            print ("Please enter a number")


def getOperator():
    while True:
        operator = input("Enter an operator (+, -, *, /) or '=' to get the final result: ")
        if operator in ('+', '-','*','/', '='):
            return operator
        else:
            print("Please enter an operator")

def perform_operation(total, operator, number):
    if operator == '+':
        return total + number
    elif operator == '-':
        return total - number
    elif operator == '*':
        return total * number
    elif operator == '/':
        return total / number


# This is where the main code starts


while True:                                             #This is a loop that will keep asking the user to enter a number followed by entering the w
    total = getNumber("Enter your first number: ")      #second loop that is asking the user to enter an operator. 

    while True:
        operator = getOperator()
                                                        #In the second loop we ask the user to enter an operator, if it's '=' we break out of it, print the
        if operator == '=':                             #total and ask if they want to perform another calculation. If it's not '='
            break                                           

        number = getNumber(f"Enter the next number for {operator} operation: ") #If its another operator like + or - we then ask for another number
        total = perform_operation(total, operator, number)                      #and another operator again, he could choose = or keep going.
    
    print ("The result is ", total)                         #Once we are out of the loop we print the total.

    another = input("Would you like to perform another operation? (Y/N): ")  #And we ask the user if he wants to use the calculator again. Then if he types
                                                                             # yes. we go back to our first loop and do it all again. 
    if another.upper() != 'Y':
         break

