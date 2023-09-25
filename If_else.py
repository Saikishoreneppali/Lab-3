  #Example-1
print('Example-1')
sensor1_dist = 1.1 # distance read by sensor 1 in meters
sensor2_dist = 1.3 # distance read by sensor 2 in meters
threshold_dist = 1.2 # threshold distance for considering an obstacle in meters


if sensor1_dist < threshold_dist or sensor2_dist < threshold_dist:
    print("Warning: obstacle detected! Stopping!")
else:
    print("No obstacle, moving forward!")

print("Example-2")
  #Example-2
joystick_in = "right"

if joystick_in == "right":
    print("moving 1st joint in positive direction")
elif joystick_in == "left":
    print("moving 1st joint in negative direction")
elif joystick_in == "up":
    print("moving the 2nd joint in positive direction")
elif joystick_in == "down":
    print("moving the 2nd joint in the negative direction")
else:
    print("the joystick is in the neutral position, no movement")

print('Example 3')
def min_num(a,b,c):
    if a < b and a < c:
        return "The smallest number is " + str(a)
    elif b < a and b < c:
        return "The smallest number is " + str(b)
    elif c < a and c < b:
        return "The smallest number is " + str(c)
    else:
        return "They are equal"
    
print(min_num(2,21,4))
