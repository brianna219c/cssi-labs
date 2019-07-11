print("Welcome to Bris Pluralizer!")
word1 = raw_input("please enter a word:")
num1 = int(raw_input ("please enter a number:"))

if num1 == 0 :
    print(str(num1) + " " + word1 + "s")
elif num1 >1 :
    print(str(num1) + " " + word1 + "s")
else:
        print(str(num1) + " " + word1)
