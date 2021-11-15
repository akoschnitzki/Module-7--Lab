#Name- Alexander Koschnitzki
#Date- 11-11-21

#Problem 4

#In this problem, it is able to use function to take number
#from a list to be able to create another list. You can input
#any number into the list and it can create another list from those numbers.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))