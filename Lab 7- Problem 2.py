#Name- Alexander Koschnitzki
#Date- 11-11-21

#Problem 2

#In this problem, it is able to use a function to be able to
#check to see if a number is in a list that you give it.
#You can input any number and it is able to tell if it
#is in that list.

def rangecheck(n):
    if n in range(1, 10):
        print("That Number is in range!")
    else:
        print("That Number is not in Range!")
rangecheck(600)