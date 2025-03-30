class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for j in range (len(nums)-1):
            if nums[j]==0:
                nums.remove(nums[j])
                nums.append(0)
def main():
    s=Solution()
    arr=[0,1]
    s.applyOperations(arr)
    print(arr)
main()
