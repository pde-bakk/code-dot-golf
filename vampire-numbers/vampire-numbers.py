import collections
import sys

D={}
def dtally(xint: int) -> int:
	xint_backup = xint
	if xint in D.keys():
		return D[xint]
	t = 0
	# print(f'{xint=}', file=sys.stderr)
	while xint>0:
		add = (1<<((xint % 10) * 6))
		t += add
		xint //=10
		# print(f'added {add} so {t = }, new {xint =}', file=sys.stderr)
	D[xint_backup]=t
	return t

def stally(xint: int):
	if xint in D:return D[xint]
	st=sorted(str(xint))
	D[xint]=st
	return st

def get_counter(q):
	if q in D:return D[q]
	s=str(q)
	D[q] = collections.Counter(str(q))
	return D[q]

def fangs(x: int) -> int:
	nd = len(str(x))
	if nd&1:
		return 0
	nd //= 2
	lo = max(tens[nd-1], (x + tens[nd]-2)//(tens[nd]-1))
	# hi = int(min(x/lo,x**.5))

	# print(f'{x=}, {lo=}, {hi=}', file=sys.stderr)

	# t=dtally(x)
	# t=get_counter(x)
	# print(f'{x=}, dtally(x)={t}', file=sys.stderr)
	for a in range(max(tens[nd-1], (x + tens[nd]-2)//(tens[nd]-1)), int(min(x/lo,x**.5))+1):
		b = x//a
		if a*b==x and ((a%10)or(b%10))and get_counter(x)==get_counter(a)+get_counter(b):
		# if a*b==x and ((a%10)or(b%10))and t==dtally(a)+dtally(b):
		# if a*b==x and ((a%10)or(b%10)) and stally(x) == sorted(stally(a)+stally(b)):
			print(x)
			return 1
	return 0

tens = [10**i for i in range(20)]
for i in range(1_000_000):
	fangs(i)
# print(len(D),D,file=sys.stderr)
