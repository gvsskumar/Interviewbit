# Input → "ABA"
# Output → A, B, A, AB, BA, ABA

text = "ABA"
result = []
for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        result.append(text[i:j])
print(",".join(result))        