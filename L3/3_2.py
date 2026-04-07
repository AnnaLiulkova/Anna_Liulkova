def count_substring(main_string, substring):
    if not substring:
        return 0
    
    count = 0
    sub_len = len(substring)
    
    for i in range(len(main_string) - sub_len + 1):
        if main_string[i:i+sub_len] == substring:
            count += 1
            
    return count

text = "abcaabababcc"
sub = "abc"
result = count_substring(text, sub)
print(f"Підрядок '{sub}' зустрічається {result} раз(и)")