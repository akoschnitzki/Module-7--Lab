#Name- Alexander Koschnitzki
#Date- 11-11-21

#Problem 3

#In this problem, you can be able to create a list and
#it is able to multiply the numbers in the list. You can
#input any number in the list and it is able to multiply them.

def multiplyList(L):
    total = 1
    for x in L:
        total = x
    return total
numL = [5, 2, 7, -1]
print("total is ", multiplyList(numL))
