'''CounthowmanytimeslowercasevowelsoccurredinaStringenteredbytheuser'''

def vowel_count(string):
    '''Counts the number of lowercase vowels in a string'''
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
    return count
user_input = input("Enter a string: ")
print("Number of lowercase vowels in the string:", vowel_count(user_input))