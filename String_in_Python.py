num_int = 9
num_float = 5.0
print(" There are " + str(num_int) + " arm robots in the factory, " + str(num_float) + " of them are broken.")
print("There are ", num_int, " arm robots in the factory, ", num_float, " of them are broken.")

factory_name = "SAI"
print("The factory's name is " , factory_name)

print("The first character in the factory name is " + factory_name[0])
print("The first character in the factory name is " + factory_name[2])

print(factory_name.lower())
print(factory_name.islower())

print(factory_name.upper().isupper())

print(len(factory_name))    #length of the string
print(factory_name[0:len(factory_name)-1])
print(factory_name[0:len(factory_name)-2])

print(factory_name.index("A")) 
print(factory_name.index("S"))

print(factory_name.replace("SAI", "NSK"))