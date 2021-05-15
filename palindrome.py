
def verify(a):
    x = 0;
    i = len(a) - 1;
    b = True;
    while x <= i:
        while a[x] == ' ':
            x = x + 1;
        while a[i] == ' ':
            i = i - 1;
        if a[x] != a[i]:
            return False;
        x = x + 1;
        i = i - 1;
    return True;
