# Time complexity - O Log N
# Perform  binary search on array. check neighbors of midpoint.  if difference is equal to 1, update r  or  l depending  on comparison.
# ultimately, there will be case when L > r. at that point we have isolated the missing value index. we simply return l + 1 for result.

def find_missing_number(nums):
    l = 0
    r = len(nums) - 1

    if nums[0] != 1:
        return 1

    while l <= r:
        mid = l + (r - l) // 2

        # If the difference between the value and the index is 1, then the left side is correct
        if nums[mid] - mid == 1:
            l = mid + 1
        else:
            r = mid - 1

    # The missing number is at the position l + 1
    return l + 1
