s = raw_input()

arr = []
for i in range(len(s)):
    arr.append(ord(s[i]))

stri = ""
for j in range(len(arr)):
    if arr[j]>97:
        arr[j] = arr[j]-1

    stri.join(chr(arr[j]))
    
print stri
    
