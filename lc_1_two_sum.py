from typing import List
# o(n), o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        

# The main block
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input
    nums = [2, 7, 11, 15]
    target = 9
    
    # Call the twoSum method
    result = solution.twoSum(nums, target)
    
    # Print the result
    print(f"Indices of the two numbers that add up to {target}: {result}")

