 # Swap two numbers without using any thirdvariable
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
