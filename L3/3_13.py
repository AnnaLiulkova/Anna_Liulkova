def rle_encode(text):
    if not text: 
        return ""
    res = ""
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res += text[i] + str(count)
            count = 1
    res += text[-1] + str(count)
    return res

def rle_decode(data):
    res = ""
    for i in range(0, len(data), 2):
        char = data[i]
        count = int(data[i+1])
        res += char * count
    return res

original = "aaaaaaaaaaaaaaaaaaaaabbccccdbbb"
encoded = rle_encode(original)
decoded = rle_decode(encoded)

print(f"Оригінал: {original}")
print(f"Стиснений: {encoded}")
print(f"Відновлений: {decoded}")