i = 0
numbers= []

while i<6:
    print "At the top i is %d" %i
    numbers.append(i)

    i = i+1
    print "numbers now",numbers
    print"At the bottom i is %d" %i

print "The numbers:"

for num in numbers:
    print num


def test_while(j):
    i = 0
    while i<j:
        print "At the top i is %d" %i
        numbers.append(i)
    
        i = i+1
        print "numbers now",numbers
        print"At the bottom i is %d" %i

test_while(10)


    
