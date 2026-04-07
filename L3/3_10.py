def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]

    return " ".join(reversed_words)

text = "привіт світ це тестс номер 10"
result = reverse_words_in_sentence(text)
print(f"Вхідне речення: {text}")
print(f"Результат: {result}")