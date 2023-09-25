from Robot import Robot
class FlyingRobot(Robot):
    def __init__ (self, name, DOFs, max_altitude):
        super().__init__ (name, DOFs) # we inherit these attributes from the Robot class
        self.max_altitude = max_altitude
    
    def move(self):
        print(f"I am a flying robot with a max altitude of {self.max_altitude}.")
        super().move() # we also call the move method from the base class
'''robot = FlyingRobot("SAI", 6, 210)
robot.introduce()
robot.move()'''