# NAME = ROHAN ELAHI
#ROLL NUMBER = 40547
#EMAIL = relahi508@gmail.com



#------------------------SIMPLE-CALCULATOR---------------------
# SIMPLE CALCULATOR IN PYTHON
#ADD
#SUBTRACT
#MULTIPLY
#DIVIDE

#IMPORTING MATH LIBRARY
import math

# DEFINING ADDITION FUNCTION 
def add():
    val1=int(input("Enter first no: ")) #INPUT
    val2=int(input("Enter second no: "))# INPUT
#OUTPUT
    print(f"The sum is:{val1+val2}")
    
# DEFINING SYBTRACTION FUNCTION  
def sub():
    val1=int(input("Enter first no: "))#INPUT
    val2=int(input("Enter second no: "))#INPUT
#OUTPUT
    print(f"The sum is:{val1-val2}")
    

#DEFINING MULTIPLICATION FUNCTION
def mul():
    val1=int(input("Enter first no: "))#INPUT
    val2=int(input("Enter second no: "))#INPUT
#OUTPUT
    print(f"The multilpication of no is:{val1*val2}")
    


#DEFINING SQUARE ROOT FUNCTION USING MATH LIBRARY
def sqrt():
    
    val1=int(input("Enter no: "))#INPUT
    res=int(math.sqrt(val1))#APPLYING SQUARE ROOT 
    #OUTPUT
    print(f"The square root of no is:{res}")





#DEFINING DIVISION FUNCTION
def div():
    try:# NO ERROR THEN TRY WILL RUN
        val1=int(input("Enter first no: "))
        val2=int(input("Enter second no: "))

        print(f"The division is:{val1/val2}")
    
    except:# IF ERROR WHILE DIVISION BY 0 
        if val2==0:
            #OUTPUT
            print("Math Error can't divide by zero") 
               


# MENU BAR USING WHILE TRUE FUNCTION TO MAKE THE CONDITION TRUE 
while True:
    print("----------CALCULATOR-----------")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. SQUARE ROOT")
    print("6. EXIT")
# TAKING USER INPUT
    operation = input("ENTER CHOICE TO PERFORM TASK: ")
#USING IF CONDITION
    if operation == "1":   
        add()
    # USING ELIF CONDITON      
    elif operation == "2":
        sub()
     # USING ELIF CONDITON        
    elif operation == "3":
        mul()
        
    # USING ELIF CONDITON         
    elif operation == "4":
        div()
    
    # USING ELIF CONDITON     
    elif operation == "5":
        sqrt()
    
        
    # USING ELIF CONDITON     
    elif operation == "6":
        print("EXITING THE CALCULATOR") 
        exit()
#OUTPUT
    else:
        print("INVALID ENTERY")   
    
       
        
