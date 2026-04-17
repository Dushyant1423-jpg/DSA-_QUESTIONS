# Convert uppercase characters to lowercase using bits
def to_lowercase(ch):
    return chr(ord(ch) | 32)


# test
print(to_lowercase('A'))  
print(to_lowercase('B'))  