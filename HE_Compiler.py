import re,sys

x = sys.stdin.read()
new = []
for l in x.split('\n'):
    comment = l.split('//')
    comment[0] = comment[0].replace('->', '.')
    new.append('//'.join(comment))
print '\n'.join(new)

