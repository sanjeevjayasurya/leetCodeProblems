class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = len(A) - 1
        i = 0
        while i < j:
            if A[i] % 2 > A[j] % 2: 
                A[i], A[j] = A[j], A[i]
            
            if A[i] % 2 == 0: 
                i += 1
            if A[j] % 2 == 1: 
                j -= 1 
        return A
            