min = 372304
max = 847060

def check(password):
    res = [int(x) for x in str(password)]
    previous = res[0]
    first = True
    duplicate = False
    for number in res:
        if first:
             first = False
             continue
        if number < previous:
            return False
        if number == previous:
            duplicate = True
        previous = number

    return duplicate

#print (check(122345))
#print (check(111123))
#print (check(223450))
#print (check(123789))

counter = 0
for x in range(min, max + 1):
    good = check(x)
    #print ("%d %s" % (x, good))
    if good:
        counter += 1

print (counter)
