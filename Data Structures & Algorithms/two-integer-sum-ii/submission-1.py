class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        previousNums = {}
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in previousNums:
                return [previousNums[diff] + 1, idx + 1]
            previousNums[num] = idx
        return None