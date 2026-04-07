def get_unique_words(sentence):
    words = sentence.split()
    
    unique_words = list(dict.fromkeys(words)) #list(set(words))
    return unique_words

my_sentence = " у цьому     реченні   існують існують кілька    кілька однакових слів слів"
result = get_unique_words(my_sentence)
print("Список унікальних слів:")
print(result)