

def rev_string(x):
    x_rev = []
    l = len(x)
    for i in range(l-1,-1,-1):
        x_rev.append(x[i])
    return ''.join(s for s in x_rev)