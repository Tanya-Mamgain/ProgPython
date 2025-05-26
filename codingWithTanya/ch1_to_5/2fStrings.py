# we can use fstrings to print required data directly instead of using concatenation 
name = input("Enter your name:\t")
print(f"Good afternoon {name}")

# if you do not  use fstrings then {name} will be printed as it is
name1=input('Enter your name')
print("Good Afternoon , {name1}")

#The correct way to avoid using fstrings and print name will be using concatenation
name3=input("Enter your name:\t")
print("Good afternoon "+name3+"\n\thiii ")