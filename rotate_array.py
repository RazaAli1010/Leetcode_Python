class Solution(object):
    def rotate(self,nums,k):
        n=len(nums)
        k%=n
        def reverse(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
                
                
def main():
    arr=[1,2,3]
    a=4
    s=Solution()
    s.rotate(arr,a)
    print(arr)
main()