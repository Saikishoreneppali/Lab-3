robotic_engineers = ("Hannah", "Jim", "Bella", "John")
print(robotic_engineers)

print(robotic_engineers[1]) #2nd value in the tuple

e1, e2, e3, e4 = robotic_engineers # unpacking the tuple into the variables
print(e1, e2, e3, e4)
print(e3)

#robotic_engineers[1] = "Bob"  #changes in touple

robotic_partners = [('Hannah', 'john'), ('Jim', 'Bella')]   # lists in touple
print(robotic_partners)

robotic_partners = [(robotic_engineers[0],robotic_engineers[3]), (robotic_engineers[1], robotic_engineers[2])] 
print(robotic_partners)
print(robotic_partners[0])