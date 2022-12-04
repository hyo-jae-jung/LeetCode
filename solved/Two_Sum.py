from collections import deque

class Solution:
    def twoSum(self, nums:list, target: int)->list:
        nums_d = deque(nums)
        temp = 0

        while nums_d:
            i = nums_d.popleft()
            if target-i in nums_d:
                temp = i
                break
        
        return [i for i,j in enumerate(nums) if j==temp or j==target-temp]
        
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(list(range(1,10001)),19999))
