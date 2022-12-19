import pdb

class Solution:
    def longestCommonPrefix(self, strs: list):
        answer = list()
        a = strs.pop()
        temp = ''
        i=0
        j=i
        while j < len(a):
            # pdb.set_trace()
            temp+=a[j]
            if not all([True if temp in x else False for x in strs]):
                answer.append(temp[:-1])
                temp = ''
                j=i
            else:
                j+=1


        return answer

if __name__ == "__main__":
    s = Solution()
    case1=["flower","flow","flight"]
    case2=["dog","racecar","car"]
    case3=['abxyzi','abyyzi']

    print(s.longestCommonPrefix(case3))
