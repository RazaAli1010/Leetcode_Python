class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        majority_element=0
        i=0
        for i in range (len(nums)-(i+(n//2))):
            if nums[i]==nums[i+(n//2)]:
                majority_element=nums[i]
                break
        return majority_element
def main():
    s=Solution()
    arr=[2,2,1,1,1,2,2]
    print(s.majorityElement(arr))
main()