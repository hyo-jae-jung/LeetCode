class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x[0] == '-':
            return False
        else:
            for i in range(int(len(x)/2)+1):
                if x[i] != x[-1*(1+i)]:
                    return False
            else:
                return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('121525121'))
