#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards

def reverse(word):
    x = ""
    for i in range(len(word)):
        x += word[-1-i]
    return x


word = str(input("give me a word or sentence: "))
word = word.lower()
reverse = reverse(word)
print(f"reverse = {reverse}")
if reverse == word:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")