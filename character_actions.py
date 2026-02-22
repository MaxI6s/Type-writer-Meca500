from robot_actions import RobotController
from layout import Layout

def on_space(robot: RobotController):
    robot.press_space()

def on_newline(robot: RobotController):
    robot.new_line()

def on_char(robot: RobotController, row:int, column:int, is_shifted:bool):
    if is_shifted:
        robot.shift_lock()
    robot.press_key(row, column)
    if is_shifted:
        robot.shift_unlock()

def character_actions(robot: RobotController, layout: Layout, char: str):
    """
    Dispatches actions based on the character type.
    """

    match char:
        case ' ':
            on_space(robot)
        case '\n':
            on_newline(robot)
        case _:
            try:
                row, column, is_shifted = layout.get_key(char)
                print(f"Character '{char}' found at row {row}, column {column}, shifted: {is_shifted}")
                on_char(robot, row, column, is_shifted)
            except ValueError as e:
                print(f"Warning: {e}")

# --- Example Usage (using your previous file) ---

def example_usage():
    robot = RobotController("192.168.0.100", mockup=True)
    layout = Layout('layouts/TYPEWRITER.json')

    test_string = "Hello World!\nThis is a test."
    for char in test_string:
        character_actions(robot, layout, char)
        
if __name__ == "__main__":
    example_usage()