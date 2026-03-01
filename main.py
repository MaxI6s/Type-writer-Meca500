from robot_actions import RobotController
from layout import Layout

from parser import *
from character_actions import *

PATH_TO_TEXT = "texts/poem_example.txt"
MOCKUP_MODE = False

def main():
    layout = Layout('layouts/TYPEWRITER.json')

    robot = RobotController("192.168.0.100", mockup=MOCKUP_MODE)
    robot.move_to_safe_position()
    
    with open('texts/test_file.txt', 'w', encoding='utf-8') as f:
        f.write("Hello World!\nPython is great.")

    characters = extract_characters('texts/test_file.txt')

    for char in characters:
        character_actions(robot, layout, char)

if __name__ == "__main__":
    main()
