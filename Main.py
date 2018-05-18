#Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)
import math

def reverse(str):
    myList= list(str)
    myList.append("/n")
    myLen = len(myList)
    n = math.floor(myLen/2)
    for i in range(0, n):
        myList[i], myList[myLen-i-1] = myList[myLen-i-1], myList[i]
    #output as array
    #return myList
    #output as string
    return "".join(myList)

print(reverse("abcdefg"))
print(reverse("this will look very weird backwards"))