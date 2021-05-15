
def count(a):
    space = True;
    count = 0;
    for c in a:
        if(c == ' '):
            space = True;
        elif(space == True):
            space = False;
            count = count + 1;
    return count;
