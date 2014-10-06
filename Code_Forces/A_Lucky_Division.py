import psyco
psyco.full()

T = input()

if T%4==0 or T%7==0 or T%47==0 or T%44==0 or T%77==0 or T%444==0 or T%447==0 or T%477==0 or T%777==0 or T%774==0 or T%744==0:
    print "YES"
else:
    print "NO"
