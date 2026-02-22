import mecademicpy.robot as mdr
import time

class RobotController:
    def __init__(self, ip_address, mockup:bool=False):
        self.robot:mdr.Robot = mdr.Robot(ip_address)
        self.mockup = mockup

        if not mockup:
            self.robot.Connect()
            print(">> Robot connected successfully.")
        else:
            print(">> Mockup mode: Robot connection skipped.")

    def move_to_safe_position(self):
        print(">> Moving robot to a safe position...")
        if not self.mockup:
            # Example: Move to a predefined safe position (this is just a placeholder)
            raise NotImplementedError 
        else:   
            print(">> Mockup mode: Skipping actual movement.")
            time.sleep(0.5)  # Simulate time taken to move
        print(">> Robot is now in a safe position.")

    def shift_lock(self):
        print(">> Shift lock engaged: Robot is now in a safe state.")
        if not self.mockup:
            # Example: Engage shift lock (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual shift lock engagement.")
            time.sleep(0.5)  # Simulate time taken to engage shift lock
        print(">> Robot is now in shift lock mode.")

    def shift_unlock(self):
        print(">> Shift lock disengaged: Robot is now operational.")
        if not self.mockup:
            # Example: Disengage shift lock (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual shift lock disengagement.")
            time.sleep(0.5)  # Simulate time taken to disengage shift lock
        print(">> Robot is now operational.")

    def press_key(self, row:int, column:int):
        print(f">> pressing key at row {row}, column {column}...")
        if not self.mockup:
            # Example: Move to the key position and press it (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual key press.")
            time.sleep(0.5)  # Simulate time taken to press the key
        print(f">> Key at row {row}, column {column} has been pressed.")
        
    def press_space(self):
        print(">> pressing SPACE key...")
        if not self.mockup:
            # Example: Move to the space key position and press it (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual space key press.")
            time.sleep(0.5)  # Simulate time taken to press the space key
        print(">> SPACE key has been pressed.")
    
    def carriage_return(self):
        print(">> performing carriage return...")
        if not self.mockup:
            # Example: Move to the enter key position and press it (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual carriage return.")
            time.sleep(0.5)  # Simulate time taken to perform carriage return
        print(">> Carriage return has been performed.") 
        
    def new_line(self):
        print(">> performing new line...")
        if not self.mockup:
            # Example: Move to the enter key position and press it (this is just a placeholder)
            raise NotImplementedError
        else:
            print(">> Mockup mode: Skipping actual new line.")
            time.sleep(0.5)  # Simulate time taken to perform new line
        print(">> New line has been performed.")

def example_usage():
    robot = RobotController("192.168.0.1", mockup=True) 

    robot.move_to_safe_position()

if __name__ == "__main__": 
    example_usage()
    
    
    