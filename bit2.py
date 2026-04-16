def odd_or_even(n):
    bitMask = 1

    if (n & bitMask) == 0:
        print("even number")
    else:
        print("odd number")


# test
odd_or_even(3)
odd_or_even(11)
odd_or_even(14)