class Robot:
    def __init__ (self, name, DOFs):
        self.name = name 
        self.DOFs = DOFs

    def introduce(self):
        print(f"I am {self.name}, a {self.DOFs} DOF robot.")

    
    def move(self):
        print("I can move.")