class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqiue_items = set()
        for num in nums:
            if num in unqiue_items:
                return True
            unqiue_items.add(num)
        return False