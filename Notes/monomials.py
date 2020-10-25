def monomials(deg,dim):
	if dim == 0: return [[]]
	ans = [[[i]+m for i in range(deg-sum(m)+1)[::-1]] for m in monomials(deg,dim-1)]
	ans = [x for y in ans for x in y]
	return [x[1:] for x in sorted([[sum(x)]+x for x in ans])][::-1]



