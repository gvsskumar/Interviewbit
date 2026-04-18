# ✅ 1. Brute Force (All Substrings)
# Idea:
# Generate all substrings
# Check if each has unique characters
# ⏱ Complexity:
# Time: O(n²), Space: O(n)
def longest_substring_bruteforce(s):
    max_len = 0
    longest = ""

    for i in range(len(s)):
        seen = set()
        temp = ""

        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            temp += s[j]

        if len(temp) > max_len:
            max_len = len(temp)
            longest = temp

    return longest, max_len
# print(longest_substring_bruteforce('abcaabdg'))

#===========================#
# ✅ 2. Sliding Window (Optimized – MOST IMPORTANT 🔥)
#Idea:
# Use two pointers (left, right)
# Expand window
# If duplicate → shrink window
# Time: O(n), Space: O(n)

def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0
    longest = ""

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest = s[left:right+1]

    return longest, max_len
#print(longest_substring('abcaabdgaabbccstrdhgaf'))
#===============================#
# ✅ 3. Sliding Window with Index Map (Best for Interviews ⭐)
# Idea:
# Store last index of characters
# Jump left pointer directly
# Time: O(n), Space: O(n)
def longest_substring_map(s):
    char_map = {}
    left = 0
    max_len = 0
    longest = ""

    for right, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= left:
            left = char_map[ch] + 1

        char_map[ch] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest = s[left:right+1]

    return longest, max_len
print(longest_substring_map('abcaabdgaabbccstrdhgafz'))
