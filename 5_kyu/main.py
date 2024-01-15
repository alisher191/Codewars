def smash(words):
    s = ""
    s += words[0]
    for i in range(1, len(words)):
        s += f" {words[i]}"
    return s

print(smash(["hello", "world"]))
print(smash(["hello", "amazing", "world"]))
print(smash(["this", "is", "a", "really", "long", "sentence"]))