a=5080000
b=5330000
c=5550000
d=b-a
e=c-b
print ("The population change from 2004 to 2014 d=",d,"million")
print ("The population change from 2014 to 2024 e=",e,"million")
if d > e:
    print ("Population growth is decelatating")
else:
    print  ("Population growth is accelerating")
# The population change from 2004 to 2014 d= 250000 million
# The population change from 2014 to 2024 e= 220000 million
# Population growth is decelatating

X = True
Y = False
W = X or Y
print ("The Boolean type of W is",W)
# The Boolean type of W is True

# Truth table for X OR Y
# X     | Y     | X or Y
# True  | True  | True
# True  | False | True
# False | True  | True
# False | False | False