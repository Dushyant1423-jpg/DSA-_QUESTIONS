def fast_expo(a, n):
    ans = 1

    while n > 0:
        if (n & 1) != 0:   # check last bit
            ans = ans * a

        a = a * a          # square
        n = n >> 1         # right shift

    return ans


# test
a = int(input("Enter base: "))
n = int(input("Enter power: "))

print(fast_expo(a, n))