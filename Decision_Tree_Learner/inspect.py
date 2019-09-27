from __future__ import print_function
import sys
import csv
import numpy as np

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    print("The input file is: %s" % (infile))
    print("The output file is %s" % (outfile))

read = csv.reader(open("%s" % (infile),'r'), delimiter=",")
x = list(read)
data = np.array(x)
data = data[1:]
value = data[0][0]
y = data[:,-1]

value = y[0]
a = 0
b = 0
i = 0
while i < len(y):
    if y[i] == value:
        a = a+1
        i = i+1
    else:
        b = b+1
        i = i+1
c = 0
if a < b:
    c = a
else:
    c = b

er = c/float((a+b))

yes = a/float(a+b)
no = b/float(a+b)
if no == 0:
    entropy = -((yes)*(np.log2(yes)))
elif yes == 0:
    entropy = -((no)*(np.log2(no)))
else:
    entropy = -((yes) * (np.log2(yes)) + (no) * (np.log2(no)))

met = [er, entropy]

p = open("%s" %(outfile), 'w')
p.write ("entropy: %g\n" %(met[1]))
p.write("error: %g\n" %(met[0]))

