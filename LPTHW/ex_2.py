#age = raw_input("how tall are you?")
#height = raw_input("how much do you weigh")
#weight = raw_input("how much do you weigh")

#print"so,you're %r old,%r tall and %r heavy."%(age,height,weight)o

from sys import argv

#script,user_name = argv

#prompt = '>'
#
#print"hi %s,im the %s script"%(user_name,script)
#print"do you like me %s?"%user_name
#likes = raw_input(prompt)
#print"where do you live %s?"%user_name
#lives=raw_input(prompt)
#
#print"what kind of computer do you have?"
#computer=raw_input(prompt)
#
#
#print"""
#alright,so you said %r ablout liking me.
#you live in %r.not sure where that is.
#and you have a %r computer.
#NICE.
#"""%(likes,lives,computer)

script,filename = argv
txt = open(filename)
print"here's your file %r:"%filename
print txt.readlines(2)

print"we are going to erase %r" %filename
print"if you dont want that,hi ctrl-c"
print"if you do want that,hi RETURN"

raw_input("?")

print"opening the file"
target = open(filename,'w')

print"truncating the file.goodbye!"

target.truncate()

print"now im going to ask you for three lines"

line1 = raw_input("line1")
line2 = raw_input("line2")
line3 = raw_input("line3")

print"im gonig to write thsese to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print"and finally,we close it"
target.close()

