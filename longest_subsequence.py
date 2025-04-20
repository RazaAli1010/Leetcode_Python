
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for i in range(0,len(s)):
            sub=set()
            count=1
            for j in range(i,len(s)):
                if s[j] in sub:
                    break
                else:
                    sub.add(s[j])
            count=len(sub) 
            result=max(count,result)       
        return result
def main():
    a=Solution()
    strin="abcabcbb"
    print(a.lengthOfLongestSubstring(strin))
main()
