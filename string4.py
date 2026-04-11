def anagm(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

anagm(s1, s2)