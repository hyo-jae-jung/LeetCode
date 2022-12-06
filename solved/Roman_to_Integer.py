import sys

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        temp = [dic[i] for i in s]
        answer = []
        for i in range(len(temp)-1):
            if temp[i] < temp[i+1]:
                answer.append(-1*temp[i])
            else:
                answer.append(temp[i])
        else:
            answer.append(temp[-1])
            
        return sum(answer)

if __name__ =="__main__":
    s = Solution()
    print(s.romanToInt(sys.stdin.readline().strip()))
