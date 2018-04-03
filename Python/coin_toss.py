import random

def coin_toss() :
    print "Starting the program..."
    attempt = 0
    heads = 0
    tails = 0
    for num in range(5000) :
        toss = random.randint(0,1)
        attempt += 1
        if toss == 0 :
            heads += 1
        else :
            tails += 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(attempt, heads, tails)
    print "Ending the program, thank you!"

coin_toss()