# check  if a palindrome number or not
# def palindrome(num):
#     temp = num
#     rev = 0
#     while temp > 0:
#         dig = temp % 10
#         rev = rev * 10 + dig
#         temp //= 10
#     if num == rev:
#         return True
#     else:
#         return False
def is_palindrome(s):
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    return True


s = "racecar"
print(is_palindrome(s))