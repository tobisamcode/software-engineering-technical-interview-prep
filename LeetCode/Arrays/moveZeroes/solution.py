class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        count = 0
        for num in nums:
            if num:
                nums[count] = num
                count += 1
            
        for zero in range(count, len(nums)):
            nums[zero] = 0
        
        return nums