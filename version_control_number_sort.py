vs = ["1.1.0", "1.2.1", "a1.0.1","0.9.1", "1.1.2", "1.3.4", "2.0.9"]

def mycmp(x):
    temp = ''.join(str.split(x, "."))
    print(temp)
    return(temp)

# key takes a function that takes one value
# and return a single value that can be used
# to guide sorting
sorted(vs, key=mycmp)

mycmp(vs[0])