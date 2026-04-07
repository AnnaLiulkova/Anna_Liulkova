import re

def censor_text(text, forbidden_words):
    result_text = text
    
    for word in forbidden_words:
        # re.IGNORECASE - незалежність від регістру
        # \b - шукає ціле слово
        pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
        result_text = pattern.sub('[ЦЕНЗУРА]', result_text)
        
    return result_text

original_text = "Цей Секретний документ містить секретний код та інші дані, які не треба знати"
banned = ["секретний", "код"]
censored = censor_text(original_text, banned)

print(f"Оригінал: {original_text}")
print(f"Цензура: {censored}")