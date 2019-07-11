print("welcome to my cacuator")

def count_spaces(s):
    return s.count("  ")

def count_vowles(s):
     numA = s.count("a")
     numE = s.count("e")
     numI = s.count("i")
     numO = s.count("o")
     numU = s.count("u")
     numY = s.count("y")
     sunVowel = numA + numE + numO + numI +numU + numY
     return

print(count_vowels("hello there, you are the best!"))

countNum = count_vowels("hello there, you are the best!")
print(countNum)
