# SETS METHODS

# CAN SETS HAVE VALUES OF DIFF DATA TYPES??  ANS=YES
s={1,2,3,4,5,"Tanya"}
print(s,type(s))

# 1. add() 
print("\nadd() method")
s.add(5+5)
s.add(2)
s.add("Mamgai")
print(s)

print("\n\nremove() method")
# 2. remove(element)
# Description: Removes an element from the set. If the element is not found, it raises a KeyError.
my_set = {1, 2, 3}
my_set.remove(2)
# my_set.remove(4)   => this will give keyerror if executed as 4 is not in set
print(my_set)  
print("2 has been removed")

# 3. discard(element)
# Description: Removes an element from the set. If the element is not found, it does not raise an error (unlike remove()).
print("\n\ndiscard() method")
my_set = {1, 2, 3}
print("orignal set is=> ",my_set)
my_set.discard(2)  # Removes 2
my_set.discard(4)  # Does nothing since 4 isn't in the set (WILL NOT GIVE KEYERROR)
print("After using discard method to discard 2 & 4 => ",my_set)  


# 4. clear()
# Description: Removes all elements from the set, leaving it empty.
print("\n\n")
print("(4) clear() method")
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  
print("set becomes empty")

# 5. copy()
# Description: Returns a shallow copy of the set.
print("\n\n(5) clear() method")
my_set = {1, 2, 3}
new_set = my_set.copy()
print("the orignal set my_set was=> ",my_set)
print("after copying values of my_set to new_set, the new_set is=>",new_set)



# (6.) union(*sets)
# Description: Returns a new set with elements from the set and all other sets passed as arguments. It combines all unique elements from the sets.
print("\n\n(6)union method")
set1 = {1, 2, 3}
print("set1 is=> ",set1)
set2 = {3, 4, 5}
result = set1.union(set2)
print("set2 is=> ",set2)
print("after union of set 1 & 2 result is: ")
print(result)  
result2= set2.union(set1)
print("set2 union set1 will give =>",result2)

# (7.) intersection(*sets)
# Description: Returns a new set with elements that are common to all sets.
print("\n\nintersection() method")
set1 = {1, 2, 3}
print("set 1 is=> ",set1)
set2 = {2, 3, 4}
print("set 2 is=>",set2)
result = set1.intersection(set2)
print("intersection of set 1 and set 2 is:")
print(result)  

