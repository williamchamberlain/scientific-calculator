import time 
time.sleep(1)
print("Welcome to Will's Scientific Calculator")
time.sleep(2)
print("This will help you with all your maths problems!")






def add_up():
  time.sleep(1)
  num1=float(input("Enter a number: "))
  time.sleep(1)
  num2=float(input("Enter another number: "))
  num3= num1 + num2
  print(num3)
  
  
  
#add_up()


def minus_it():
  
 
  time.sleep(1)
  num1=float(input("Enter a number: "))
  time.sleep(1)
  num2=float(input("Enter another number: "))
  num3= num1 - num2
  print(num3)
  
#minus_it()


def times_it():
  
 
  time.sleep(1)
  num1=float(input("Enter a number: "))
  time.sleep(1)
  num2=float(input("Enter another number: "))
  num3= num1 * num2
  print(num3)
  
  
#times_it()


def divide_it():
 

  time.sleep(1)
  num1=float(input("Enter a number: "))
  time.sleep(1)
  num2=float(input("Enter another number: "))
  num3= num1 / num2
  print(num3)
  
#divide_it()
def pi_sum( ):
  time.sleep(1)
  num1=float(input("Enter a number: "))
  num2=3.14159265359
  num3 = num1*num2
  print(num3)

def exponential( ):
  time.sleep(1)
  num1=float(input("Enter a number: "))
  num2=float(input("Enter a power: "))
  num3 = num1**num2
  print(num3)
   
    
  
#exponential( )

exit="y"

choice=str(input("Would you like to +, - ,*,/ , power or pi (times) "))


while exit=="y":

  if choice == "+":
    add_up() 
    
  elif choice == "-":
    minus_it()
  
  elif choice == "pi":
    pi_sum()


  elif choice == "*":
    times_it()
  
  elif choice == "times":
    times_it()

  
  elif choice == "/":
    divide_it()
  
  elif choice == "power":
    exponential( )
  else:
    print("ERROR: input is not valid")

  if exit=="n":
    break

  exit=input("Would you like to restart y/n ")









