class RobotArm:
    def __init__(self, name, length, weight, color):
        self.name = name
        self.length = length
        self.weight = weight
        self.color = color
        self.position = 0

    def move(self, angle):
        self.position += angle

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Length: {self.length} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Color: {self.color}")
        print(f"Position: {self.position} degrees")

arm1 = RobotArm("Armrob", 50, 10, "Black")
arm1.move(45)
arm1.display_info()

arm1.move(-15)
arm1.display_info()

class RobotArm:
    def __init__(self, name, length, weight, color):
        self.name = name
        self.length = length
        self.weight = weight
        self.color = color
        self.position = 0

    def move(self, angle):
        self.position += angle

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Length: {self.length} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Color: {self.color}")
        print(f"Position: {self.position} degrees")

