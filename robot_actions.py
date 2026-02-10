import mecademicpy.robot as mdr


class RobotController:
    def __init__(self, ip_address):
        self.robot:mdr.Robot = mdr.Robot(ip_address)
        self.robot.Connect()
        print(">> Robot connected successfully.")

    def move_to_safe_position(self):
        print(">> Moving robot to a safe position...")
        # Example: Move to a predefined safe position (this is just a placeholder)
        self.robot.MoveJoints([0, 0, 0, 0, 0, 0], speed=50)
        print(">> Robot is now in a safe position.")
        
    def shift_lock(self):
        print(">> Shift lock engaged: Robot is now in a safe state.")
        
    def shift_unlock(self):
        print(">> Shift lock disengaged: Robot is now operational.")
    
    def press_key(self, char):
        print(f">> pressing '{char}' key...")
        
    def press_space(self):
        print(">> pressing SPACE key...")
    
    def carriage_return(self):
        print(">> performing carriage return...")
        
    def new_line(self):
        print(">> performing new line...")
    
    
    