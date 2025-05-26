# WAP to detect double space in string 
para= "Tanya is a good  girl and  "
print(para.find("  ")) 
print(para.find("gi"))
print(para.find("GI"))  #it gives a value of -1 if given string does not contain substring to be found
print(para)