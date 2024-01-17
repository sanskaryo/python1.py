try:
  # Open the file in read mode
  with open("abc.txt", "r") as file:
    # Read the entire file content
    content = file.read()
except FileNotFoundError:
  # Handle file not found error
  print("Error: File 'abc.txt' not found!")
except Exception as error:
  # Catch any other unexpected error
  print(f"Error: {error}")
else:
  # Successfully read the file content
  print("File content:")
  print(content)
finally:
  # Always close the file, even if an error occurs
  print("File closed.")
