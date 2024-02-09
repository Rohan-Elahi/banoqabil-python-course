# FIZZ BUZZ

def fizz_Buzz():

    print("The nums from 1 to 100 ")

    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(i,"FizzBuzz")


        elif i%3==0:
            print(i,"Fizz")


        elif i%5==0:
            print(i,"Buzz")









# Prime No checker

def prime_no():
    num = int(input("Enter a number: ")) #5

    if num > 1:
        
        for i in range(2, num): #2-->4
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print("Please enter a number greater than 1.")


        
    


# Sum of the digits
        
def Sum_of_digit():

    no=int(input("Enter the no: "))

    sum_result=0


    if no<1:
        print("Can't perform operation ")

    if no>=1:
        for i in range(1,no+1):
            sum_result=sum_result+i
        print(f"The result is {sum_result}")
        
        









# Factorial Calculator


def factorial_calculator():
    num=int(input("Enter the you want to factorial: "))

    default=1
    if num==0:
        print("The factorial of 0 is 1")
    elif num<1:
        print("The factorial doesn't exist for negative no ")



    elif num>1:
        for i in range(1,num+1):
            default=default*i
        print(f"The factorial of {num} is {default} ")       










# multiplication table generator

def multiplication_cal():

    val1=int(input("Enter any no you want to print the table: "))

    for i in range(1,11):
        print(val1," x " ,i, '=', i*val1 )







# Even odd checker
        
def even_odd_checker():
    val=int(input("Enter any no: "))

    if val%2==0:
        print("Even No ")

    else:
        print("Odd No ")






def menu():
    
    while True:
        print("---------------\t MENU----------------")
        print("1 - Even Odd Checker")
        print("2 - Multiplication Checker")
        print("3 - factorial_calculator")
        print("4 - Sum_of_digit")
        print("5 - Fizz Buzz")
        print("6 - Prime No Checker ")
        print("7 - Exit")
        choice = input("Enter the operation you want to perform: ")
        print()
        if choice == "1":
            even_odd_checker()
        elif choice == "2":   
            multiplication_cal()

        elif choice == "3":
            factorial_calculator()
        elif choice == "4":
            Sum_of_digit()
        elif choice == "5":
            fizz_Buzz()
        
        elif choice == "6":
            prime_no()
            
        elif choice == "7":
            exit()
         
        else:
            print("Invalid choice. Please enter a valid option.")

menu()
