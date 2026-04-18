def is_match(text: str, pattern: str) -> bool:
    
    def dfs(i, j):
        # If pattern is exhausted
        if j == len(pattern):
            return i == len(text)

        # Check current match
        first_match = i < len(text) and (
            pattern[j] == text[i] or pattern[j] == '.'
        )

        # Handle '*' (look ahead)
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            return (
                dfs(i, j + 2) or        # skip "x*"
                (first_match and dfs(i + 1, j))  # use "*"
            )
        else:
            return first_match and dfs(i + 1, j + 1)

    return dfs(0, 0)

# print(is_match("aaa","a"))
# print(is_match("aaa","a."))
print(is_match("aa", "a*"))
print(is_match("ab", ".*"))
print(is_match("aab", "c*a*b"))
