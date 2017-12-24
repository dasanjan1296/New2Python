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
#xrange doesn't exist in Python 3 onwards
#for i in xrange(len(var)-1,-1,-1):
    #x = var[i]
    #print(x)
    #print("loop 7\n")
for i in reversed(var):
    print(i)
    print(len(i))
    print("loop 8\n")
#This another way to iterate a list in reverse manner.

for i in range(10):
    print("anjan\n")
    print(i)
    print("loop 9")
for i in range(5,12):
    print(i)
    print("loop 10\n")
for i in range(10, 40, 3):
    print(i)
    print("loop 11\n")
#The following code traverses the list var in reverse manner, which xrange did above. P.S. xrange has been merged i nrange in Python 3 onwards.
for i in range(len(var)-1,-1,-1):
    print(var[i])
    print("loop 12\n")

var1 = 25

while var1<40 :
    print(var1)
    print("loop 13")
    var1 += 1
#If we dont think about the termination of the loop, it will become an infinite loop and crash the computer.
