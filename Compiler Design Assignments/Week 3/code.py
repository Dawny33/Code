f=open("grammer.txt",'r')
p4=[]
p3=[]
while True:
	s=f.readline()
	if s=="EOF":
		break
	l=len(s)
	for i in range(0,l-1):
		if s[i:i+2]=="->":
			break
	p4.append(s[0:i])
	p3.append(s[i+2:l-1])
l=len(p3)
p1=[]
p2=[]
for i in range(0,l):
	s=p3[i]
	a=s.split('|')
	l=len(a)
	for j in range(0,l):
		p2.append(a[j])
		p1.append(p4[i])
l=len(p2)
oc=0
op=[]
for i in range(0,l):
	l=len(p2[i])
	d=0
	for j in range(0,l):
		if ord(p2[i][j])>=65 and ord(p2[i][j])<=90: 
			d=1
			break
	if d==0:
		oc=oc+1
		op.append(p2[i])
op.append("$")
opr=[]
l=len(op)
for i in range(0,l):
	if len(op[i])==1:
		opr.append(op[i])
a=[]
for i in range(0,oc+1):
	b=[]
	for j in range(0,oc+1):
		b.append(0)
	a.append(b)
f=open("precidence.txt",'r')
j=0
while True:
	s=f.readline()
	if s=="EOF":
		break
	p=map(int,s.split())
	l=len(p)
	for i in range(0,l):
		a[j][i]=p[i]
	j=j+1
# a is precidence table
# p1 is left stack
# p2 is right stack
f=open("input.txt",'r')
b=[]
while True:
	r=f.readline()
	if r=="EOF":
		break
	l=len(r)
	b.append(r[0:l-1])
l=len(b)
c=[]
#input formatting
for i in range(0,l):
	if b[i] not in op:
		c.append("id")
	else:
		c.append(b[i])

c.append("$")
# c is input stack
L=len(c)
d=[]
d.append("$")
q=[]
i=0
# main loop for input parsing
print "stack"+"\t\t\t"+"input stack"
while(i<L):
	l=len(d)
	r=d[l-1]
	x=len(op)
	for j in range(0,x):
		if op[j]==r:
			break
	u=j
	for j in range(0,x):
		if c[i]==op[j]:
			break
	v=j
	if a[u][v]==0:
		if r=="$" and c[i]=="$":
			print "Successful"
			break
		else:
			print "Unsuccessful"
			break
	elif a[u][v]==1:
		e=d.pop()
		if e in opr:
			#print e
			t=len(p2)
			for j in range(0,t):
				if e==p2[j]:
					z=p1[j]
					break
			r=len(q)
			s=q[r-2]+z+q[r-1]
			#print s
			print "reduced "+q[r-1]+e+q[r-2]+" to "+s
			del q[r-1]
			del q[r-2]
			q.append(s)
		else:
			q.append(e)
	elif a[u][v]==2:
		d.append(c[i])
		i=i+1
	r=len(q)
	t=len(p2)
	for j in range(0,r):
		z=0
		for k in range(0,t):
			if q[j]==p2[k]:
				z=1
				break
		if z==1:
			print "reduced "+q[j]+" to "+p1[k]
			q[j]=p1[k]
	w=""
	l=len(c)
	for j in range(i,l):
		w=w+c[j]
	print d,"  ",q,"  ",w
	
