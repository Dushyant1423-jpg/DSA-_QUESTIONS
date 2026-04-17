def power(num):
    if num > 0:
        result = num ** num
        print(result)
    else:
        print("Not defined")


num = int(input("Enter any number: "))
power(num)