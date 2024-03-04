def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Test cases
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print("Example 1:")
print("Input:", nums1)
print("Output:", majority_element(nums1))
print()

print("Example 2:")
print("Input:", nums2)
print("Output:", majority_element(nums2))
