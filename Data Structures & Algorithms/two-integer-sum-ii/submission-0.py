class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        previousNums = {}
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in previousNums:
                return [previousNums[diff], idx + 1]
            previousNums[num] = idx + 1
        return None