var = ["guitar", "violin", "cello", "flute", "harmonium", "tabla", "drums"]

for i in var:
    print(i)
    print(len(i))
    print("loop 1\n")
for i in var[:]:
    print(i)
    print(len(i))
    print("loop 2\n")
for i in var[2:6]:
    print(i)
    print(len(i))
    print("loop 3\n")
for i in var[-1:-3]:
    print(i)
    print(len(i))
    print("loop 4\n")
for i in var[-1:]:
    print(i)
    print(len(i))
    print("loop 5\n")
for i in var[::-1]:
    print(i)
    print(len(i))
    print("loop 6\n")
#Used extended slicing in loop 6 to iterate in reverse
#But this cannot be applied to all the lists. For some we need to use xrange, and its role is exactly similar to a for loop in c or java.
for i in xrange(len(var)-1,-1,-1):
    x = var[i]
    print(x)
    print("loop 7\n")
for i in reversed(var):
    print(i)
    print(len(i))
    print("loop 8\n")
#This another way to iterate a list in reverse manner.