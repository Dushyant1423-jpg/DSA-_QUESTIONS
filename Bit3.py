def is_power_of_two(n):
    if n > 0 and (n & (n - 1)) == 0:
        return True
    else:
        return False


# test
num = int(input("Enter number: "))

if is_power_of_two(num):
    print("Power of 2")
else:
    print("Not power of 2")