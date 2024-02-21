from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]
            records[value] = index
        return []

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
