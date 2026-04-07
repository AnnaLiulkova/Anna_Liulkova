def is_palindrome(word):
    word = word.lower() 
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

test_word = "шалаш"
if is_palindrome(test_word):
    print(f"Слово '{test_word}' є паліндромом.")
else:
    print(f"Слово '{test_word}' не є паліндромом.")

