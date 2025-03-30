class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=3:
            return s
        char_list=[]
        for char in s:
            if len(char_list)>=2 and char==char_list[-1] and char==char_list[-2]:
                continue
            char_list.append(char)
        return ''.join(char_list)

                



