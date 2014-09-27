from mpmath.lib import giant_steps, lshift, rshift
from math import log

START_PREC = 15

def size(x):
    if isinstance(x, (int, long)):
        return int(log(x,2))
    # GMPY support
    return x.numdigits(2)

def newdiv(p, q):
    szp = size(p)
    szq = size(q)
    szr = szp - szq
    if min(szp, szq, szr) < 2*START_PREC:
        return p//q
    r = (1 << (2*START_PREC)) // (q >> (szq - START_PREC))
    last_prec = START_PREC
    for prec in giant_steps(START_PREC, szr):
        a = lshift(r, prec-last_prec+1)
        b = rshift(r**2 * rshift(q, szq-prec), 2*last_prec)
        r = a - b
        last_prec = prec
    return ((p >> szq) * r) >> szr

print newdiv(30,6)
