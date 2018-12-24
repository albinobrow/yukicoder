#!/usr/bin/python
import numpy as np

n,k=list(int(input()) for i in range(2))
l=sorted(list(int(input()) for i in range(n)))
if k > 2:
	print(int(round(l[-1]-l[0])))
else:
	m=-float("inf")
	for i in range(1,n):
		a=np.mean(l[:i])
		b=np.mean(l[i:])
		c=int(round(b-a))
		if m < c:
			m=c
	print(m)
