# Instructions to run

# run the program by on command-line by executing - 'python main.py filename'

# Thoughts -

# Input - file path

# Take command line argument - a file path

# Record the search term found on the last line of the file

# Check for substring within the line, if character is letter add to string and check if the next character is a not a letter. If so add a whitespace indicating the end of a word within the substring. Underscore characters are counted as alphabet characters and that case is handled specifically. The newline character signifies the end of the line and the output is ready to be formatted.

# A generator function to produce the correct list output

# Considerations -

# To ensure the functions are written clearly and produce a singular output, the search term and source text are searched for separately.

# Unittests created for different cases related to the file and others created to test the component fucntions need to be integrated for the program.

# Tests include differing line quantity e.g no lines, one line, one thousand lines

# Test for potential addition of file extension compatibility

# Additional testing could involve performance, creating a baseline approximation based on a specific number of rows to get an average time the algorithm should operate at based on file input size.

# A logger was added to give the user a message in response to an action/event that has occur in the program.

#
