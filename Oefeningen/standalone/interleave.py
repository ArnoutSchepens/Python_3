def interleave(str1, str2):
    return "".join("".join(item) for item in (zip(str1, str2)))

print(interleave("hi", "ha"))
print(interleave("aaa", "zzz"))
print(interleave("lzr", "iad"))