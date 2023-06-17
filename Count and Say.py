def count_and_say(n):
    sequence = "1"  # Starting sequence with "1"
    
    for a in range(1, n):
        current = ""
        count = 1
        prev_char = sequence[0]

        for i in range(1, len(sequence)):
            if sequence[i] == prev_char:
                count += 1
            else:
                current += str(count) + prev_char
                count = 1
                prev_char = sequence[i]

        current += str(count) + prev_char
        sequence = current

    return sequence

# Example usage:
n = 4
result = count_and_say(n)
print("Count and Say Sequence:", result)
