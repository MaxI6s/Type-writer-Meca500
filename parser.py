def extract_characters(file_path):
    """
    Reads a .txt file and returns a list of every character 
    found in the file, including spaces and newlines.
    """
    try:
        # Open the file in read mode ('r') with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire content of the file into a string
            content = file.read()
            
            # Convert the string into a list of characters
            char_list = list(content)
            
            return char_list
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# --- Example Usage ---
def examople_usage():
    # 1. Create a dummy file for testing
    with open('texts/test_file.txt', 'w', encoding='utf-8') as f:
        f.write("Hello World!\nPython is great.")

    # 2. Call the function
    characters = extract_characters('texts/test_file.txt')
    # 3. Print the result
    print(f"Total characters extracted: {len(characters)}")
    print(f"First 15 characters: {characters[:15]}")
    
if __name__ == "__main__":
    examople_usage()
    