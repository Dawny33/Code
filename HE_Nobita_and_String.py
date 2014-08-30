class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.size() == 0
    def push(self,item):
        return self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)	

s = Stack()
k = int(raw_input())

for _ in range(k):
    T = raw_input()

    for j in T.split():
        s.push(j)

    p = []
    for i in range(s.size()):
        p.append(s.pop())

    st = ""
    for k in range(len(p)):
        st += p[k]
        st += " "

    print st[:-1]
