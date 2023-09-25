robot_brands = ["ABB", "KUKA", "FANUC", "Omrom"]
print(robot_brands[1])
print(robot_brands[:3])

robot_brands.append("UR")
print(robot_brands)

robot_brands.remove("UR")
print(robot_brands)

robot_brands.sort()
robot_brands.reverse()

print(len(robot_brands))

robot_brands.append("UR")
print(robot_brands)
print(len(robot_brands))

robot_brands1 = ['Yaskawa', 'stabuli']
robot_brands.extend(robot_brands1)
print(robot_brands)
robot_brands.pop()

print(robot_brands.index("ABB"))
#print(robot_brands.index("SAI"))

print(robot_brands.count("ABB"))

robot_brands2 = robot_brands.copy()
print(robot_brands)
print(robot_brands2)

robot_brands.clear()
print(robot_brands)