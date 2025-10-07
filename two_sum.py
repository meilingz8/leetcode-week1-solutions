from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sumn = numbers[l] + numbers[r]
            if sumn == target:
                return [l + 1, r + 1]
            elif sumn < target:
                l += 1
            else:
                r -= 1

//two sum solution
