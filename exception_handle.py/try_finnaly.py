def read_file_content(file_path):
    file = None  # Initialize to None
    try:
        file = open(file_path, "r")
        content = file.read()
        # Intentionally causing an error
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero!")
    finally:
        # Check if 'file' is not None before attempting to close
        if file is not None:
            file.close()
            print("File closed.")

