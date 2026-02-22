class Layout:
    def __init__(self, layout_file):
        self.layout_file = layout_file
        self.keys = []
        self.space_key = None
        self.enter_key = None
        self.shift_lock_key = None
        self.shift_unlock_key = None
        self.load_layout()
    
    def load_layout(self):
        # Load the layout from the JSON file and populate the keys and special keys
        import json
        with open(self.layout_file, 'r') as f:
            data = json.load(f)
            self.keys = data.get("keys", [])
            self.space_key = data.get("space_key", {})
            self.enter_key = data.get("enter_key", {})
            self.shift_lock_key = data.get("shift_lock_key", {})
            self.shift_unlock_key = data.get("shift_unlock_key", {})

    def get_key(self, char: str):
        # Return the key position for the given character
        for key in self.keys:
            if key['label'] == char:
                return key['x'], key['y'], False
            if key['shift_label'] == char:
                return key['x'], key['y'], True
        raise ValueError(f"Character '{char}' not found in layout.")

def example_usage():
    layout = Layout('layouts/TYPEWRITER.json')
    print("Keys:", layout.keys)
    print("Space Key:", layout.space_key)
    print("Enter Key:", layout.enter_key)
    print("Shift Lock Key:", layout.shift_lock_key)
    print("Shift Unlock Key:", layout.shift_unlock_key)

if __name__ == "__main__":
    example_usage() 