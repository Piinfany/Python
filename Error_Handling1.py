'''
Objective:
Create a Python script that:
1. Reads a file specified by the user.
2. Validates the content of the file.
3. Handles errors gracefully (e.g., file not found, invalid data).
4. Calculates and displays results based on valid data.

Detailed Instructions:
Prompt for File Name
    The script should ask the user to input the name of a file to read.

Handle Missing Files
    If the file does not exist, catch the `FileNotFoundError` and display the message:
Error: File '<file_name>' not found. Please try again.
Prompt the user to re-enter the file name.

Read and Process File
Open the file in read mode. Assume the file contains one value per line. Each line is expected to be:
    - A valid numeric value (integer or float).
    Process the file line by line:
    - If a line contains non-numeric data, display a message:
     Warning: Invalid data on line <line_number>: '<line_content>'
    and skip that line.
    - Otherwise, treat it as a valid number and add it to a list.

Display Results
After processing the file:
    - Display the total number of valid lines processed.
    - Display the sum of all valid numeric values.
'''
