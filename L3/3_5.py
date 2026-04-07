def most_frequent_from_set(text, char_set):
    counts = {}
    for char in char_set:
        counts[char] = text.count(char)
        
    if not counts:
        return []
    
    max_count = max(counts.values())

    if max_count == 0:
         return []
    return [char for char, count in counts.items() if count == max_count]

my_string = "програмування на python це круто!"
my_set = {'а', 'о', 'п', 'р'}
result = most_frequent_from_set(my_string, my_set)
print(f"Найчастіші символи з множини: {result}")