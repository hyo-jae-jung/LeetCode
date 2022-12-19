class Solution:
    def mergeTwoLists(self, list1, list2):
        list1.sort(reverse=True)
        list2.sort(reverse=True)
        answer=[]
        while all([len(list1),len(list2)]):
            if list1[-1] <= list2[-1]:
                answer.append(list1.pop())
            elif list1[-1] >= list2[-1]:
                answer.append(list2.pop())
        else:
            answer.extend(list1)
            answer.extend(list2)
        
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists([3,4,2,6,5,1],[5,3,1]))
