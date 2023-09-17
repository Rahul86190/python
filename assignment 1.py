l=[1,2,3,4,5,6]
print("list is :",l )
s=0
l2=[]
for i in l:
    i=i**2
    l2.append(i)
    s=s+1

print ("Square of the list is :" ,l2)
print("Sum of square list elements is: ",s)