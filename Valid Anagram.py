def is_anagram(s1, s2):
    # Sort the characters of both strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    # Compare the sorted strings
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False

# Example usage:
string1 = "listen"
string2 = "silent"
is_valid_anagram = is_anagram(string1, string2)
print("Valid Anagram:", is_valid_anagram)
