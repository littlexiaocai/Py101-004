from sys import argv
from os.path import exists

script,from_file,to_file = argv
print"copying from %s to %s" %(from_file,to_file)

#in_file=open(from_file)
#indata = in_file.read()

indata=open(from_file).read()

print"the input file is %d bytes long" %len(indata)

print"does the output file exist? %r" %exists(to_file)
print "ready,hit return to continue,ctrl_c to abort."

raw_input()

open(to_file,'w').write(indata)

print"alright,all done"

#out_file.close()
#in_file.close()
