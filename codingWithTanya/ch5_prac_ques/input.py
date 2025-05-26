#using input
a = input ("Enter num1: ")   #treats i/p as a string
b = input("Enter num2: ")    #treats i/p as a string
print("Number a is: ",a)
print("Number b is: ",b)
print("Sum is: ",a+b)  # but this will give concatenation of strings as outputs 

# TO AVOID THIS USE INT KEYWORD
c = int(input ("Enter num1: ") )  
d = int(input("Enter num2: "))    
print("Number a is: ",a)
print("Number b is: ",b)
print("Sum is: ",c+d)