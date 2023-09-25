from Robot import Robot

class WheeledRobot(Robot):
    def __init__ (self, name, DOFs, num_wheels):
        super().__init__ (name, DOFs) # here we inheretited the name and DOFs from the Robot class
        self.num_wheels = num_wheels
    
    def move(self):
        print(f"I am a wheeled robot with {self.num_wheels} wheels.")
        super().move()
robot = WheeledRobot("SAI", 4, 2)
robot.introduce() 
robot.move()