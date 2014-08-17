T = raw_input()
T = int(T)

p = raw_input()
p = map(int,p.split())

arr = []
arr.append(p)

jk = max(arr)
maxx = []
for j in arr:
    if j==jk:
        maxx.append(jk)


minn = []
for k in arr:
    if k == min(arr):
        minn.append(k)


if len(maxx)==len(minn):
    print str(maxx[0]-minn[0])+" "+len(maxx)

elif len(maxx)>len(minn):
    print str(maxx[0]-minn[0])+" "+len(minn)

elif len(maxx)<len(minn):
    print str(maxx[0]-minn[0])+" "+len(maxx)

