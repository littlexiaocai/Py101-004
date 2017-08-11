my_name = 'caicai'
my_age = 30
my_height = 175.67 
my_weight = 122
my_teeth = 'white'
my_eyes = 'white'
my_hair = 'brown'

print"let talk about %s"%my_name
print"He is %r inches tall"%my_height
print"He get %s eyes and %s hair."%(my_eyes,my_hair)
print"He get %f"%my_height 
print"He get %f"%round(my_height) 
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" %(binary,do_not)
x = "caicai love haohao"
print"i said:%s." % y
print x+y

print "caicai love haohao" * 10


jiajia = "%s%s%s%s" 

print jiajia %(1,2,3,4)

print jiajia %(5,6,7,8)

days = "Mon Tue Wed Thu Fri Sat Sun"

months="Jan\nFeb\nMar\nApr"

print "here are the monthsi,%r"%months

tabby_cat = "\tIm tabbed in"
persian_cat = "im split\non a line"

backslash_cat = "i am \\ a \\ cat"

fat_cat= '''

\t* cat food
\t* Fishies
\t* catnip\n\t* Grass

'''
print fat_cat

for i in["/","-","|","\\","|"]:
    print"%s\r"% i,
