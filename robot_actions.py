import mecademicpy.robot as mdr
import time

class RobotController:
    def __init__(self, ip_address, mockup:bool=False):
        self.mockup = mockup

        if not mockup:
            self.robot = mdr.Robot(ip_address)
            self.robot.Connect()
            print(">> Robot connected successfully.")
            self.robot.ResetError()
            self.robot.ActivateAndHome()
            self.robot.WaitHomed()
            
        else:
            print(">> Mockup mode: Robot connection skipped.")

    def move_to_safe_position(self):
        print(">> Moving robot to a safe position...")
        if not self.mockup:
            self.robot.MoveJoints(0, -40, 40, 0, 0, 0)
            print(">> Moving to (0, -40, 40, 0, 0, 0)")
        else: 
            print(">> Mockup mode: Skipping actual movement.")
            time.sleep(0.5)  # Simulate time taken to move
        print(">> Robot is now in a safe position.")

    def shift_lock(self):
        print(">> Shift lock engaged: Robot is now in a shifted state.")
        if not self.mockup:
            self.robot.StartProgram("shift_lock")
            self.robot.WaitIdle()
        else:
            print(">> Mockup mode: Skipping actual shift lock engagement.")
            time.sleep(0.5)  # Simulate time taken to engage shift lock
        print(">> Robot is now in shift lock mode.")

    def shift_unlock(self):
        print(">> Shift lock disengaged: Robot is now in normal state.")
        if not self.mockup:
            self.robot.StartProgram("shift_unlock")
            self.robot.WaitIdle()
        else:
            print(">> Mockup mode: Skipping actual shift lock disengagement.")
            time.sleep(0.5)  # Simulate time taken to disengage shift lock
        print(">> Robot is now in normal state.")

    def press_key(self, row:int, column:int):
        print(f">> pressing key at row {row}, column {column}...")
        if not self.mockup:
            # Example: Move to the key position and press it (this is just a placeholder)
            self.robot.StartProgram("TEST_move_to_key")
            self.robot.WaitIdle()
        else:
            print(">> Mockup mode: Skipping actual key press.")
            time.sleep(0.5)  # Simulate time taken to press the key
        print(f">> Key at row {row}, column {column} has been pressed.")
        
    def press_space(self):
        print(">> pressing SPACE key...")
        if not self.mockup:
            self.robot.StartProgram("space")
            self.robot.WaitIdle()
        else:
            print(">> Mockup mode: Skipping actual space key press.")
            time.sleep(0.5)  # Simulate time taken to press the space key
        print(">> SPACE key has been pressed.")
    
    def new_line(self):
        print(">> performing new line...")
        if not self.mockup:
            self.robot.StartProgram("new_line")
            self.robot.WaitIdle()
        else:
            print(">> Mockup mode: Skipping actual new line.")
            time.sleep(0.5)  # Simulate time taken to perform new line
        print(">> New line has been performed.")

def example_usage():
    robot = RobotController("192.168.0.100", mockup=True) 

    robot.move_to_safe_position()

if __name__ == "__main__": 
    example_usage()