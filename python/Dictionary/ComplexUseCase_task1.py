# Implement a simple word auto-complete using a prefix dictionary.

class AutoComplete:
    def __init__(self, words):
        self.prefix_dict = {}
        self.build_prefix_dict(words)

    def build_prefix_dict(self, words):
        for word in words:
            prefix = ""
            for ch in word:
                prefix += ch
                if prefix not in self.prefix_dict:
                    self.prefix_dict[prefix] = []
                self.prefix_dict[prefix].append(word)

    def suggest(self, prefix):
        return self.prefix_dict.get(prefix, [])


# Example usage
words = ["apple", "app", "apply", "bat", "ball"]

auto = AutoComplete(words)

print(auto.suggest("ap"))
print(auto.suggest("ba"))
print(auto.suggest("app"))