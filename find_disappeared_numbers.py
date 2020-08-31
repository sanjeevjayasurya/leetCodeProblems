class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:      
        if nums != []:
            unique_set = set(nums)
            new_set = set([x for x in range(1,len(nums)+1)])
            return list(new_set-unique_set)
        
            
# Better memory solution ( Deepti Talsera Approach )
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:      
        missing = []
        for i in nums:
            post = abs(i) - 1  # position of the number
            if nums[pos] > 0: 
                nums[pos] *= -1 # turning the number at the position negative
        for i in range(len(nums)):
            if nums[pos] > 0:
                missing.append(i+1)
        return missing