numbers = [     [10, 11, 12, 13, 14],
               [20, 21, 22, 23, 24],
               [30, 31, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

for i in range(cnum):
       csum = 0
       for j in range(rnum):
               csum += numbers[j][i]
       print("The summation of column {0}: {1}".format(i+1, csum))


