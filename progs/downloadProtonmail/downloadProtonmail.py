L = call("ls ~/Downloads/*.eml", shell=True).decode().split("\n")[:-1]
for l in L:
	old = '\\ '.join(l.split(' '))
	new =   '_'.join(l.split(' '))
	temp = "mv " + old + " emails/" + date(l) + '_' + new
	print(temp,'\n\n\n',old,'\n\n\n')
	call(temp,shell=True)





