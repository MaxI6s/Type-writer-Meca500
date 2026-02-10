from robot_actions import RobotController
from character_positions import Layout

def on_space(robot: RobotController, Layout: Layout):
    robot.press_space()

def on_newline(robot: RobotController):
    robot.new_line()
    robot.carriage_return()

def on_shift_char(robot: RobotController, char: str):
    robot.shift_lock()
    robot.press_key([0, 0, 0])
    robot.shift_unlock()

def on_default_char(robot: RobotController, char: str):
    robot.press_key([0, 0, 0])

def character_actions(robot: RobotController, char: str, shift_chars:set):
    """
    Dispatches actions based on the character type.
    """

    match char:
        case ' ':
            on_space()
        case '\n':
            on_newline()
        case _ if char in shift_chars:
            # This catches any number (0-9)
            on_shift_char(char)
        case _:
            # The '_' is a wildcard (anything not listed above)
            on_default_char(char)

# --- Example Usage (using your previous file) ---

def example_usage():
    shift_characters = set('!@#$%^&*()_+<>?:"{}|')  # Define which characters are considered "shift chars"
    
    test_string = "Hello World!\nThis is a test string with numbers: 12345."
    
    for char in test_string:
        character_actions(char, shift_characters)
        
if __name__ == "__main__":
    example_usage()