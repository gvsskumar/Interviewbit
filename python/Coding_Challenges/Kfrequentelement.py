from collections import Counter
def kFrequent(nums, k):
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

print(kFrequent([1,1,1,2,2,3],2))