def min_chars_to_make_palindrome(string):
    n = len(string)
    for i in range(n-1, -1, -1):
        if is_palindrome(string[:i+1]):
            return n - i - 1

def is_palindrome(string):
    return string == string[::-1]

# Example usage:
string = "AACECAAAA"
min_chars = min_chars_to_make_palindrome(string)
print("Minimum characters required:", min_chars)
