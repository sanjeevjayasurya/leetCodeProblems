class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for i in arr:
            if i*2 in s:
                return True
            elif i%2 == 0:
                if int(i/2) in s:
                    return True
            if i not in s:
                if i == 0:
                    if(arr.count(0)>1):
                        return True
                s.add(i)
        return False
        
    
                