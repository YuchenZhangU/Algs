def getCommonPrefix(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    for i in range(min(l1,l2)):
        if str1[i]!=str2[i]:
            return str1[:i]
    return str1 if l1<l2 else str2

class Solution(object):            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 0:
            if len(strs) > 1:
                common = getCommonPrefix(strs[0],strs[1])
                for s in strs[2:]:
                    common = getCommonPrefix(common, s)
                return common
            else:
                return strs[0]
        else:
            return ''
                
        