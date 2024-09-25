def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome('kayak')) #True
print(is_palindrome('Kayak')) #True
print(is_palindrome('folklor'))  # False







    
                  