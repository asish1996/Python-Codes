from __future__ import print_function
import numpy as np
import sys
import csv
import math

if __name__ == '__main__':
    traindata = sys.argv[1]
    testdata = sys.argv[2]
    max_depth = int(sys.argv[3])
    trainout = sys.argv[4]
    testout = sys.argv[5]
    metrics = sys.argv[6]

    print ("The train file is: %s" % (traindata))
    print ("The test file is %s" % (testdata))
    print ("The depth given is %s" % (max_depth))

def read_data_from_file(filename):
   oeros = ["democrat", "A", "y", "before1950", "yes", "morethan3min", "fast", "bensive",
               "high", "Two", "large"]
   with open(filename) as file_obj:
      fileedit = file_obj.readlines()
   fileedit = [x.strip("\r\n") for x in fileedit]
   fileedit = [x.strip("\n") for x in fileedit]
   fileedit = [x.replace(" ", "") for x in fileedit]
   attr_name = fileedit[0].split(",")
   attr_val = [[1 if a in oeros else 0 for a in inst.split(",")] for inst in fileedit[1:]]
   return (attr_name, attr_val)


with open("%s" %(traindata)) as csvfile:
   data = list(csv.reader(csvfile))
array = np.array(data)

atr1 = ["high", "Two", "large", "democrat", "before1950", "yes", "morethan3min", "A", "y", "fast", "bensive",
              ]
PH = (array.size / len(array)) - 1
N = int(PH)
a = array[1, N]
for i in range(len(array) - 1):
   i = i + 1
   if array[i][N] != a:
      b = (array[i][N])

if a in atr1:
   a == a and b == b
else:
   b == a and a == b


def entropy(Array):
   sum = 0
   for x in Array:
      sum += x
   if sum == 0 or sum == len(Array):
      return 0
   p = float(sum) / len(Array)
   return - p * math.log(p, 2) - (1 - p) * math.log(1 - p, 2)

class Node:
   def __init__(self, entropy, label = 1, attr = -1, l = None, r = None):
      self.entropy = entropy
      self.l = l
      self.r = r
      self.label = label
      self.attr = attr
      self.ones = 0
      self.zeros = 0
      self.fattr = -1
      self.mi = 0

def get_best(en, Ex, Attr):
   pool = []
   for attr in Attr:
      ones_temp = []
      zeros_temp = []
      for ex in Ex:
         if ex[attr] == 1:
            ones_temp.append(ex[-1])
         else:
            zeros_temp.append(ex[-1])
      pool.append(en - len(ones_temp)/float(len(Ex)) * entropy(ones_temp) - len(zeros_temp)/float(len(Ex)) * entropy(zeros_temp))
   return (max(pool), Attr[pool.index(max(pool))])

def dtree(Exm, atr1, attr):
   ones = 0
   for ex in Exm:
      ones += ex[-1]
   if ones == 0 or ones == len(Exm):
      root = Node(0)
      root.ones = ones
      root.zeros = len(Exm) - ones
      root.attr = attr
      if ones == 0:
         root.label = 0
      elif ones == len(Exm):
         root.label = 1
      return root
   frac = float(ones) / len(Exm)
   root = Node(- frac * math.log(frac, 2) - (1 - frac) * math.log(1 - frac, 2))
   root.ones = ones
   root.zeros = len(Exm) - ones
   root.attr = attr
   root.label = 0 if ones <= len(Exm) / 2 else 1

   if len(atr1) == 0:
      root.label = 0 if ones <= len(Exm)/2 else 1
      return root
   else:
      root.mi, A = get_best(root.entropy, Exm, atr1)
      root.fattr = A
      new_exl = []
      new_exr = []
      for ex in Exm:
         if ex[A] == 1:
            new_exl.append(ex)
         else:
            new_exr.append(ex)
      if len(new_exl) == 0:
         root.label = 0 if ones <= len(Exm) / 2 else 1
         return root
      if len(new_exr) == 0:
         root.label = 0 if ones <= len(Exm) / 2 else 1
         return root
      new_attr = [attr for attr in atr1 if attr != A]
      if root.mi >= 0:
         root.l = dtree(new_exl, new_attr, A)
         root.r = dtree(new_exr, new_attr, A)
   return root

def Porder(root, l, depth):
   if root == None or depth >= max_depth + 1:
      return
   print_out = ""
   if depth == 0:
      print_out += "[" + str(root.ones) + "+/" + str(root.zeros) + "-]"
   else:
      if depth > 1:
         print_out += "| "
      if l == 1:
         print_out += train_name[root.attr] + " = A: [" + str(root.ones) + a +"/" + str(root.zeros) + b +"]"
      else:
         print_out += train_name[root.attr] + " = notA: [" + str(root.ones) + a + "/" + str(root.zeros) + b+ "]"
   print (print_out)
   Porder(root.l, 1, depth + 1)
   Porder(root.r, 0, depth + 1)

current = []

def get_pred(root, ex, depth):
   global current
   if root == None or depth >= max_depth + 1:
      return
   if ex[root.fattr] == 1:
      current.append(root.label)
      get_pred(root.l, ex, depth + 1)
   else:
      current.append(root.label)
      get_pred(root.r, ex, depth + 1)

error_train = 0.0
train_name, train_val = read_data_from_file(traindata)
attr_num = len(train_name) - 1

root = dtree(train_val, [x for x in range(attr_num)], -1)
Porder(root, -1, 0)

for ex in train_val:
   current = []
   get_pred(root, ex, 0)
   if current[-1] != ex[-1]:
      error_train += 1

error_test = 0.0
test_name, test_val = read_data_from_file(testdata)

for ex in test_val:
   current = []
   get_pred(root, ex, 0)
   if current[-1] != ex[-1]:
      error_test += 1



metric = [(error_train / len(train_val)), (error_test / len(test_val))]
label1 = []
label2 = []

print (metric)

p = open("%s" %(metrics), 'w')
p.write("error(train): %g\n" %(metric[0]))
p.write ("error(test): %g\n" %(metric[1]))

train_list = open("%s" %(trainout), 'w')
for ex in train_val:
   current = []
   get_pred(root, ex, 0)
   if current[-1] != ex[-1]:
      train_list.write("%s" % a + '\n')
   else:
      train_list.write("%s" % b + '\n')


test_list = open("%s" %(testout), 'w')
for ex in test_val:
   current = []
   get_pred(root, ex, 0)
   if current[-1] != ex[-1]:
      test_list.write("%s" % a + '\n')
   else:
      test_list.write("%s" % b + '\n')




