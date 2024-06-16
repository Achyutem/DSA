#https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

def stringMatch(a: str, b: str):
    # If strings are exactly the same
    if a == b:
        return True

    # Initialize dictionaries for character frequencies
    countA = {}
    countB = {}

    # Populate the dictionaries with character frequencies
    for char in a:
        if char in countA:
            countA[char] += 1
        else:
            countA[char] = 1

    for char in b:
        if char in countB:
            countB[char] += 1
        else:
            countB[char] = 1

    # Compare the character frequencies
    if countA != countB:
        return False

    # Initialize mismatch count
    mismatch_count = 0

    # Iterate through each character of the strings
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_count += 1
            # If mismatches exceed 2, return False
            if mismatch_count > 2:
                return False

    # If mismatches are 2 or less, return True
    return True

# Test cases
print(stringMatch('bank', 'kanb')) 
print(stringMatch('abcdeeee', 'abcdeeda'))
