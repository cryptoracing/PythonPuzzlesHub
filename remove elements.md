### Task Description:

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

### Acceptance Criteria:

To get accepted, you need to do the following:

1. Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important, as well as the size of `nums`.
2. Return `k`, which represents the count of elements not equal to `val`.

### Test Cases:

#### Test Case 1:
*Input:*
```python
nums = [3, 2, 2, 3]
val = 3
*Output:*
Expected nums: [2, 2, ?, ?]
Expected k: 2