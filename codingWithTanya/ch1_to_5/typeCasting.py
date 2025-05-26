#TYPECASTING  a type of explicit type conversion
a= "31.2"  #string
b = float(a)
t= type(b)
print (t)

# IMPLICIT TYPE CONVERSION
print("\n\n performing implicit type conversion: \n")
a=10
b=3.14
c=a+b   #Python automatically converts a into float type 
e=type(c)
print(e)
