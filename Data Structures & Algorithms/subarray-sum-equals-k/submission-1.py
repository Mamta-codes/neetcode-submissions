class Solution:
    def subarraySum(self, nums, k):
        count = 0
        running_sum = 0
        
        seen = {0: 1}

        for num in nums:
            running_sum += num

            needed = running_sum - k

            if needed in seen:
                count += seen[needed]

            seen[running_sum] = seen.get(running_sum, 0) + 1

        return count