# Funcion suma
def sum(num1: float, num2: float) -> float:
    return (num1 + num2)
def mult(num1: float, num2:float) -> float:
    return (num1 * num2)
num1=float(input("Put your first number: "))
num2=float(input("Put your second number: "))
num3= mult(num1, num2)
print("Yur add is: " + str(sum(num1,num2)) + "\n Your multiplication is: " + str(num3) )
