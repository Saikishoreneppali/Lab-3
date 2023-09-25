import time
import random 


def move_robot(distance):
    print("Moving robot forward ...")
    time.sleep(1)           #move forward by giving some delay
    print(f"The robot has moved {distance} units.")     #f means function


def detect_obstacle():
    obstacle = random.choice([True, False])
    return obstacle 

position = 1

while not detect_obstacle():
    distance = random.randint(1, 5)
    move_robot(distance)
    position += distance

print("Obstacle is detected! Stopping the robot.")
print(f"The final position of the robot is {position}")

print('For loops')

for letter in "Robotics":
    print(letter)

# we can also use for loops with other data types like lists

robotics_engineers = ["Tim", "Hannah", "John", "Bella"]
for robotic_engineer in robotics_engineers:
    print(robotic_engineer)
# let's do another for loop with the indexes
for index in range(len(robotics_engineers)):
    print(index)
    print(robotics_engineers[index])

# you can loop through a series of numbers or range of numbers
for number in range(3, 10):
    print(number)