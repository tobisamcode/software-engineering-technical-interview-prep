class Solution:
    def containsDuplicate(self, nums: List[int) -> bool:
        table = set()
        for num in nums:
            if num in table:
                return True
            else:
                table.add(num)
        return False

        