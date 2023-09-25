from WheeledRobot import WheeledRobot
from FlyingRobot import FlyingRobot 
robot1 = WheeledRobot("Rover", 3, 4)
robot1.introduce() 
robot1.move() 
robot2 = FlyingRobot("DroneX", 6, 100)
robot2.introduce()
robot2.move()