print("Welcome to bri's calculator!")

num1 =int(raw_input("Give me a numnber:"))
num2 =int(raw_input("Give me another numnber:"))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

print(myAddFunction("Here is the sum:" + str(myAddFunction(num1, num2)))
