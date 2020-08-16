class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        _max = 0
        for i in nums: 
            if i == 0:
                count = 0
            else: 
                count += 1
            if count > _max :
                _max = count
        return _max