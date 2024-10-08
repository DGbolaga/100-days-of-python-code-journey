######### Topic:  Functions with Outputs ###################
# Day 10 project: Calculator

from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract

def subtract(n1, n2):
  return n1 - n2

#Multiply

def multiply (n1, n2):
  return n1 * n2

#Divide
def divide (n1, n2):
  return n1 / n2

def exponents (n1, n2):
  return n1 ** n2

def square_root (n1, n2):
  return round((n1 ** (1 / n2)), 5)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponents,
  "sqr": square_root,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
    
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input("Type 'y' to continue calculating with {answer} or type 'n' to exit. ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator(
  
)