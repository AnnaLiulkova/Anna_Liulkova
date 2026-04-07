def calculate_letters_percentage(text):
    text = text.lower()
    vowels_chars = "аеєиіїоуюяaeiouy"
    
    vowels = 0
    consonants = 0
    
    for char in text:
        if char.isalpha(): 
            if char in vowels_chars:
                vowels += 1
            else:
                consonants += 1
                
    total_letters = vowels + consonants
    
    if total_letters == 0:
        return 0.0, 0.0
        
    v_percent = (vowels / total_letters) * 100
    c_percent = (consonants / total_letters) * 100
    
    return v_percent, c_percent

my_text = "Програмувати на Python це круто!"
v_pct, c_pct = calculate_letters_percentage(my_text)
print(f"Голосних: {v_pct:.1f}%")
print(f"Приголосних: {c_pct:.1f}%")