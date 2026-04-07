def is_valid_identifier(word):
    if not word:
        return False
    
    eng_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_first = eng_letters + "_"
    valid_all = eng_letters + "0123456789_"
    
    if word[0] not in valid_first:
        return False
        
    for char in word[1:]:
        if char not in valid_all:
            return False
            
    return True

test_id_1 = "_myVar123"
test_id_2 = "2ndVariable!"
test_id_3 = "AnyWord"
test_id_4 = "Аnd3ndVariable_"

print(f"'{test_id_1}' є ідентифікатором: {is_valid_identifier(test_id_1)}")
print(f"'{test_id_2}' є ідентифікатором: {is_valid_identifier(test_id_2)}")
print(f"'{test_id_3}' є ідентифікатором: {is_valid_identifier(test_id_3)}")
print(f"'{test_id_4}' є ідентифікатором: {is_valid_identifier(test_id_4)}")