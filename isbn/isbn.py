import sys
for s in sys.argv[1:]:
 V,C=10,0
 for c in s:
  if c.isdigit():C-=V*int(c);V-=1
 C%=11;print(s+[str(C),'X'][C==10])
