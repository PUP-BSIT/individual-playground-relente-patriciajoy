#Write a program that takes a character and tells whether it is consonant or vowel

character = str(input("Enter a character: "))

if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'): 
    print("The character is a vowel.")  
else:
    print("The character is a consonant.")