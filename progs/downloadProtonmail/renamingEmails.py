from subprocess import run, check_output as call

def date(l):
	return l[-29:16-29].replace('T','.').replace('-','.').replace(' ','.')

def prepare(title):
	title = title.replace("'","\\'").replace('[','\\[').replace(']','\\]')
	title = title.replace("(","\\(").replace(")","\\)")
	title = title.replace('&','\\&').replace("$","\\$").replace(";","\\;")
	return title

def mvMailToDir():
	L = call("ls emails", shell=True).decode().split("\n")[:-1]
	for l in L:
		old = '\\ '.join(l.split(' '))
		new =   '_'.join(l.split(' '))
		old = prepare(old)
		new = prepare(new)
		temp = "mv emails/" + old + " fixed/" + date(l) + '_' + new
		# print(temp,'\n\n\n',old,'\n\n\n')
		try: call(temp,shell=True)
		except: pass

mvMailToDir()

