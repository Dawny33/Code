def strrev(sval):
  if len(str(sval)) == 1: return sval
  else:
    strcon = str(sval)
    return int(strcon[::-1])

T = input()
while(T):
  T -= 1
  s, t = [x for x in raw_input().split()]
  x = int(strrev(str((int(strrev(s)) + int(strrev(t))))))
  print(x)
