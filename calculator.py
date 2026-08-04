def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("enter first number:"))
for symbol in operations_dict:
    print(symbol)
continue_flag=True
while continue_flag:
    operation_symbol = input("choose an operation from the line above:")
    num2 = int(input("enter second number:"))
    calculator_function = operations_dict[operation_symbol]
    output = calculator_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {output}")
    should_continue=input(f"enter 'y' to continue the calcution with {output} or 'e' to exit")
    if should_continue == 'y':
        num1=output
    else:
         continue_flag=False
         print("exit")
        