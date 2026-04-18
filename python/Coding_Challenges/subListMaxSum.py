def subarray_min_max(arr):
    # Max subarray
    max_sum = float('-inf')
    max_curr = 0
    max_start = max_end = temp_start_max = 0

    # Min subarray
    min_sum = float('inf')
    min_curr = 0
    min_start = min_end = temp_start_min = 0

    for i, num in enumerate(arr):

        # 🔹 Max logic (Kadane)
        if max_curr < 0:
            max_curr = num
            temp_start_max = i
        else:
            max_curr += num

        if max_curr > max_sum:
            max_sum = max_curr
            max_start = temp_start_max
            max_end = i

        # 🔹 Min logic (reverse Kadane)
        if min_curr > 0:
            min_curr = num
            temp_start_min = i
        else:
            min_curr += num

        if min_curr < min_sum:
            min_sum = min_curr
            min_start = temp_start_min
            min_end = i

    return {
        "max_subarray": arr[max_start:max_end+1],
        "max_sum": max_sum,
        "min_subarray": arr[min_start:min_end+1],
        "min_sum": min_sum
    }


arr = [1, 2, 4, -7, 1, -5, 4]
result = subarray_min_max(arr)

print(result)