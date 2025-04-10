import random

def create_file_with_random_statements():
    # Ask user for a filename
    filename = input("Enter a name for the new file (with .txt): ")

    # Some example random statements
    statements = [
        "Learning Python is fun!",
        "Practice makes perfect.",
        "Always handle errors in your code.",
        "Read and write files like a pro.",
        "Python is great for automation.",
    ]

    # Randomly select a few statements
    selected = random.sample(statements, k=3)

    try:
        with open(filename, 'w') as file:
            for statement in selected:
                file.write(statement + '\n')

        print(f"{filename} created successfully with random statements.")

    except Exception as e:
        print(f"Error creating file: {e}")
        return None

    return filename


def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modify lines - here we convert to uppercase as an example
        modified_lines = [line.upper() for line in lines]

        # Create a new output filename
        new_filename = f"modified_{filename}"

        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"File has been read and modified. New file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program flow
print("📄 Create a file and add random statements")
created_file = create_file_with_random_statements()

# Optional: Automatically read and modify the file just created
if created_file:
    print("\n🔄 Now let's read and modify the file you just created!")
    # You can skip the input step by passing the filename directly:
    # Or keep the interactive version:
    read_and_modify_file()
