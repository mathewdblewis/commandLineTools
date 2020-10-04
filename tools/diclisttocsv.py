def diclisttoar(diclist,F={}):
	if F != {}: diclist = [{F[key]:dic[key] for key in F if key in dic} for dic in diclist]

	cols = list(set([x for y in diclist for x in y]))
	L = [[x for x in cols]]
	for dic in diclist:
		for c in cols:
			if c not in dic: dic[c] = ''
	for dic in diclist:
		L += [[dic[x] for x in cols]]
	return L

def artocsv(ar):
	return '\n'.join([','.join([str(x) for x in row]) for row in ar])

# example:
# x = diclisttoar([{'asdf':42},{2:57},{3:21,'asdf':66}])
# print(artocsv(x))


