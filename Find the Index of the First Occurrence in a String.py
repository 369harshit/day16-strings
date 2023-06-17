def find_first_occurrence(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            return i

    return -1  # If the pattern is not found

# Example usage
text = "Hello, World!"
pattern = "World"
index = find_first_occurrence(text, pattern)
print(index)  # Output: 7
