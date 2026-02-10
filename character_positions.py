import json

class Layout:
    def __init__(self, layout_name: str):
        self.data:dict = self.load_layout(layout_name)
        self.keys:list = self.data.get("keys", {})
        self.name:dict = self.data.get("layout_name", {})
        self.unit_size_mm:dict = self.data.get("unit_size_mm", None)
    
    def load_layout(self, layout_name: str):
        with open(f'layouts/{layout_name}.json', 'r', encoding='utf-8') as file:
            layout_data = json.load(file)
            return layout_data
        
    def get_character_position(self, char: str):
        for key in self.keys:
            if key.get("label") == char or key.get("shift_label") == char:
                return [key.get("x")*self.unit_size_mm['x'],
                        key.get("y")*self.unit_size_mm['y'],
                        key.get("z")*self.unit_size_mm['z']] 
    
    
def example_usage():
    layout = Layout('US_ANSI')
    test_chars = ['a', 'Z', '1', '!', '@', ' ']
    
    for char in test_chars:
        position = layout.get_character_position(char)
        print(f"Character: '{char}' => Position: {position}")

if __name__ == "__main__":
    example_usage()