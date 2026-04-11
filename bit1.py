def ones_complement(binary):
    result = ""

    for bit in binary:
        if bit == '0':
            result += '1'
        else:
            result += '0'

    return result


# test
b = "1010"
print(ones_complement(b))