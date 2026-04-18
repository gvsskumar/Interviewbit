
# def longest_substring(s):
#     char_map = {}
#     left = 0
#     max_length = 0

#     for i in range(len(s)):
#         if s[i] in char_map:
#             left = max(left, char_map[s[i]] + 1)

#         char_map[s[i]] = i
#         max_length = max(max_length, i - left + 1)
#         keys = list(char_map.keys())
#         result = list(''.join(keys))
#         print(char_map)
#     return max_length

# print(longest_substring(input_str))


# Method-2
# unique_substrings = set()

# for i in range(len(input_str)):
#     seen = set()
#     temp = ""
    
#     for j in range(i, len(input_str)):
#         if input_str[j] in seen:
#             break   # ❌ stop if duplicate character found
        
#         seen.add(input_str[j])
#         temp += input_str[j]
#         unique_substrings.add(temp)


# # smallest & largest by length
# # smallest = min(unique_substrings, key=len)
# largest = max(unique_substrings, key=len)
# print(f"single value:{largest}")

# max_len = max(len(s) for s in unique_substrings)

# result = [s for s in unique_substrings if len(s) == max_len]

# print(f"multiple values:{result}")