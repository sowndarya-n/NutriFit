import os

# Get the current working directory
current_directory = os.getcwd()

# Walk through the directory
for root, dirs, files in os.walk(current_directory):
    # Print the current directory path
    print(f"Directory: {root}")
    
    # Print the subdirectories
    for dir in dirs:
        print(f"  Subdirectory: {dir}")
    
    # Print the files
    for file in files:
        print(f"  File: {file}")
