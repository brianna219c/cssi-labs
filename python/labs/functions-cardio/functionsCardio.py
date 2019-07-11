print("Welcome to bri's functions cardio!")
#
# num1 = int(raw_input("Give me side 1's length:"))
# num2 = int(raw_input("Give me side 2's length:"))
# num3 = int(raw_input("Give me side 2's length:"))
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2 #test is greater than s1
#     sum2 = s2 + s3 #test is greater than s2
#     sum3 = s3 + s1 #test is greater than s3
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("You have a triangle!")
#         return True #I have a triangle
#     else:
#         print("No triangle for you!")
#         return False #not a triangle :(
#
# is_triangle(num1, num2, num3)

# wordA = (raw_input("give me a word: "))
# wordB = (raw_input("give me another word: "))
# wordC = (raw_input("give me one last word: "))
# w1L = len(wordA)
# w2L = len(wordB)
# w3L = len(wordC)
#
# def longest_word(word1, word2, word3):
#     if word1 > word2 and word1  > word3: #test if its longest word
#         print( wordA + " is the longest")
#     elif word2 > word1 and word2 > word3: #test if its longest word
#         print( wordB + " is the longest")
#     elif word3 > word1 and word3 > word2: #test if its longest word
#         print( wordC + " is the longest")
#     elif word1 == word2:
#         print(word1 + " and" + word2 + " are  equal in length")
#     elif word1 == word3:
#         print(word1 + " and" + word3 + " are  equal in length")
#     elif word2 == word3:
#         print(word2 + " and" + word3 + " are  equal in length")
#     else:
#         print("All words are equal in length")
# longest_word(w1L, w2L, w3L)
word = raw_input("give me a word: ")
 def reverse_string(x):
     return x[:: -1]

print("This is your word backwards: "+ reverse_string(word))
