from art import logo
#from replit import clear

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = ("+","-","*","/")
operation_text = (" for addition"," for subtraction"," for multiplication"," for division")
operation_functions = {
  "+": add, 
  "-": subtract, 
  "*": multiply,
  "/": divide, 
}

n1_conversion = []
n2_conversion = []

def calculator():
  print(logo)
  n1 = float(input("Enter first number: "))
  #for x in range(len(n1)):
  #  n1_conversion.append(ord(n1[x]))
  #  print(n1_conversion)
  #  if ord(x) > 57 or ord(x) < 48:
  calculate = True
  while(calculate):
    for index in range(len(operations)):
      print(operations[index]+operation_text[index], sep = "")
    operation_input = input("Please enter one of the above symbols for the operation you'd like to do: ")
    n2 = ord(input("Enter next number: "))
    answer = operation_functions[operation_input](n1,n2)
    print(f"{n1} {operation_input} {n2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or 'n' to restart from 0: ").lower() == 'y':
      n1 = answer
    else:
      clear()
      calculator()
      calculate = False
      
calculator()
    
  