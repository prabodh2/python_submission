def is_vowel(char):

    vowels = "AEIOUaeiou"
    return char in vowels

# Input a character from the user
user_char = input("Enter a character: ")

# Check if the entered character is a vowel
if len(user_char) == 1 and user_char.isalpha():
    if is_vowel(user_char):
        print(f"{user_char} is a vowel.")
    else:
        print(f"{user_char} is not a vowel.")
else:
    print("Please enter a valid single character.")
