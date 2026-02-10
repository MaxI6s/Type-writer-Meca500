def on_space():
    print(">> Found a SPACE: Processing space character...")
    pass

def on_newline():
    print(">> Found a NEWLINE: Starting a new line...")
    pass

def on_shift_char(char):
    print(f">> Found a SHIFT CHAR: Doing special processing with {char}...")
    pass

def on_default_char(char):
    # What to do with everything else
    print(f">> Standard processing for: '{char}'")
    pass

def character_actions(char: str, shift_chars:set):
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