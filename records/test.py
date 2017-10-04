import time

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    if not a:
        return b
    mask = 0xffffffff # 32-bit mask
    MAX = 0x7fffffff
    while b:
        carry = a&b
        print('a^b: ' + str(a^b))
        a = (a^b) & mask 
        b = (carry << 1) & mask 
        
        print('a: ' + str(a))
        print('b: '+ str(b))
        # time.sleep(0.1)
    # return a
    return a if a <= MAX else ~(a ^ mask)
    # if a>=0:
    #     return a&mask
    # else:
    #     return a&mask



def getCommonPrefix(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    for i in range(min(l1,l2)):
        if str1[i]!=str2[i]:
            return str1[:i]
    return str1 if l1<l2 else str2

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    print(len(strs))
    print(strs[0])
    if len(strs) > 0:
        print('>0')
        if len(strs) > 1:
            print('>1')
            common = getCommonPrefix(strs[0],strs[1])
            for s in strs[2:]:
                common = getCommonPrefix(common, s)
            return common
        else:
            print strs
            strs[0]
    else:
        return ''
                
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i,n in enumerate(nums):
        print i,n
        if n > i:           
            return i
    return len(nums)


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    return not (n & (n-1))




def reverseBits(n):
    #mask = 0xffffffff
    if n:
        r = 0
        for i in range(32):
            r = r<<1
            if n&1:
                r = r+1
            n = n >> 1
            print bin(n), bin(r)
        return r+n
    else:
        return n

print reverseBits(1)
                