# Annabelle Murray
# create 2 python functions
# Create 3 calls to each function with test data to test them out.
# You do not need to use assert statements.


def count_vowels(nums):
    """
    this first function takes a list of characters in the parameter and returns the number of vowels in the list
    """

    count = 0
    for i in range(0, len(nums)):
        if nums[i] == 'a':
            count = count + 1
        if nums[i] == 'e':
            count = count + 1
        if nums[i] == 'i':
            count = count + 1
        if nums[i] == 'o':
            count = count + 1
        if nums[i] == 'u':
            count = count + 1
    return count


def contains_bracket_match(str, bracket):
    """
    this second function takes a string and an open bracket as the parameters and
    returns 'True' if there is a matching closing bracket, and 'false' otherwise
    """
    if bracket == '(' and ('(' and ')' in str):
        return "True"
    if bracket == '[' and ('[' and ']' in str):
        return "True"
    if bracket == '{' and ('{' and '}' in str):
        return "True"
    if bracket == '<' and ('<' and '>' in str):
        return "True"
    else:
        return "False"


str1 = ['w', 'e', 'l', 'l', 1, 0]
print("actual: " + str(count_vowels(str1)) + ". expected: 1")
str2 = ['a', 'b', 'c', 'd', 'e']
print("actual: " + str(count_vowels(str2)) + ". expected: 2")
str3 = ['x', 'y', 'z']
print("actual: " + str(count_vowels(str3)) + ". expected: 0")

test_str1 = "<Hello World>"
print("actual: " + str(contains_bracket_match(test_str1, '<')) + ". expected: True")
test_str2 = "Hello World (and space"
print("actual: " + str(contains_bracket_match(test_str2, '(')) + ". expected: False")
test_str3 = "{ <[)> }"
print("actual: " + str(contains_bracket_match(test_str3, '[')) + ". expected: False")