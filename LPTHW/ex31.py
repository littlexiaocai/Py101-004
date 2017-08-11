print"you enter a dark room with two doors,do you go through door #1 ro door #2"
door = raw_input(">")

if door == "1":
    print"1.take the cake"
    print"2.scream at the bear"
    bear = raw_input(">")

    if bear == "1":
        print"the bear eats your face off.good job!"
    elif bear == "2":
        print "the bear eats your legs off.good job!"
    else:
        print "well"
elif door == "2":
    print "you stare into the endlessabyss at cthulhu's retina"
    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print"your body survives powered by a mind of jello,good job!"
    else:
        print"the insanity rots your eyes into a pool of muck,good job"
else:
    print "you stumble around and fall on a knife and die,good job"
        
