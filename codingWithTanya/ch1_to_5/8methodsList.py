mylist = ["apple", "Orange",5,345.5,False,"Akash","Rohan"]
print("the orignal string before using any methods is: \n",mylist)
mylist.append("Tanya")
print("after using apend() method") 
print(mylist)

#SORT()
l1 = [1,34,62,2,6,11]
l1.sort()
print(l1)

#reverse()
l1.reverse()
print(l1)
l1.insert(3,33333)
print(l1)
l1.pop(3)
print(l1)
print(l1.pop(1))
print(l1)
l1.remove(11)
print(l1)

l1=[1,2,3,4,5,5,5,6,7,8]
l1.remove(5)
print(l1)