objects_colors = {
    "ball": "red",      # take care of indendation 
    "cube": "green",
    "flower": "pink",
    "pyramid": "blue"
}
print("the ball is " + objects_colors["ball"])
print("the cube is " + objects_colors["cube"])
print("the pyramid is " + objects_colors["pyramid"])

print(objects_colors.get("floer", "no such object"))
print(objects_colors.get("flower", "no such object"))
# a dictionary that maps robot arm joints to their corresponding min, max, and default joint angles
import math as m
arm_dict = {
    "joint1": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },

        "joint2": {
        "min" : -m.pi,
        "max" : m.pi,
        "default" : 0,
    },

        "joint3": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },

}

joint_angles_1 = arm_dict["joint1"]
print(joint_angles_1)
print(arm_dict["joint2"]["max"])
print(arm_dict["joint3"]["min"])