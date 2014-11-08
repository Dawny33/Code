def isPalindrome(String):
    stringSize = len(String)
    start = 0
    end = stringSize - 1
    while start < end and String[start] == String[end]:
        start += 1
        end -= 1
    if start < end:
        return False
    else:
        return True

def isKPalindrome(String, k):
    if k > 0:
        for i in range(len(String)):
            subString = String[:i] + String[i+1:]
        if isKPalindrome(subString, k-1) == True:
            return True
        return False
    elif k == 0:
        return isPalindrome(String)
    else:
        print 'Error number k'
        
    return False 

print isKPalindrome(raw_input(),1)
