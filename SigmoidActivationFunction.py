from decimal import Decimal

#-----Defining Sigmoid activation function-----
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


print("Enter Number")
num1 = float(input(""))


num2 = sigmoid(num1)


print(round(num2, 4))