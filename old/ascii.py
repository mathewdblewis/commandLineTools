#!/usr/local/bin/python3

import sys

def getErrors(files):
	msg = []
	for file in files:
		try:
			lines = open(file).read().split('\n')
			good = True
			for linenum in range(len(lines)):
				badchars = [char for char in lines[linenum] if ord(char)>=128]
				if badchars != []:
					if good:
						msg += [""]
						msg[-1] += "non ascii characeters are present in '"+file+"' on lines:\n"
						allgood,good = False,False
					msg[-1] += "line " + str(linenum+1).zfill(4) + ": " + ", ".join(badchars) + "\n"
		except:
			msg += [""]
			msg[-1] += "file '" + file + "' could not be read"

	return '\n'.join(msg)


if __name__ == "__main__":
	print(getErrors(sys.argv[1:]))


