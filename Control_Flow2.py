#Vowel Counting Program
#Create a Python program that counts the number of vowels in a given string and outputs the result. The program should handle both uppercase and lowercase letters and consider only the English vowels: a, e, i, o, u.
#Example Runs:
#Input: Hello World Output: The total number of vowels in the string is: 3
#Input: Python Output: The total number of vowels in the string is: 1
#Input: (empty string) Output: The input string is empty. No vowels found.

st = input("Enter any word : ").lower()
c = 0
if not st:
    print("The input string is empty.")
else :
    for x in st:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            c = c + 1

    if c > 0 :
        print("The total number of vowels in the string is : ", c)
    else:
        print("The input string is empty. No vowels found.")

