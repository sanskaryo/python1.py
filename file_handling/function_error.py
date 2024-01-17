def print_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
# Example usage
print_file_content("new_file.txt")
