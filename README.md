# Type-writer-Meca500

This project is a Python-based application designed to control a Meca500 robotic arm, enabling it to function as a typewriter. The application processes text input, identifies specific characters (such as spaces and newlines), and translates these into corresponding robotic actions.

## hardware requirements
- Meca500 robotic arm
- Computer with Python installed
- Network connection to the Meca500
- Vintage Typewriter
- Meca500 TypeWriter's end-effector
- Typewriter paper and ink

## key components
- **Character Actions**: Functions that handle specific character inputs (e.g., space, newline) and trigger corresponding robotic actions.
- **Robot Controller**: A class that manages the connection to the Meca500 and defines methods for moving the robot to safe positions, pressing keys, performing shifts, and handling carriage returns.
- **Parser**: A component that reads text input and identifies characters, invoking the appropriate character actions.
- **Main Application**: The entry point of the application that initializes the robot controller, processes text input, and orchestrates the overall functionality.