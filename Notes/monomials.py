def monomials(deg,dim):
	if dim == 1: return [[k] for k in range(deg+1)]
	ans = [[m + [i] for i in range(deg-sum(m)+1)] for m in monomials(deg,dim-1)]
	return [x for y in ans for x in y]

