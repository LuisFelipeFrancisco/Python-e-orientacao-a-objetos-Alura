file = open("file.txt", "w") # Open the file in write mode
file.write("Hello World") # Write the string to the file
file.write("\nToday is a good day")
file.write("\nI'm learning Python")

line = file.readline() # Read the first line of the file
print(line)

file.close() # Close the file

# Access mode:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# "r+" - Read and Write - Opens a file for reading and writing, error if the file does not exist
# Python open() documentation: https://docs.python.org/3/library/functions.html#open