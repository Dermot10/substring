# Instructions to run

# run the program by on command-line by executing - 'python main.py filename'

# run tests on the command line by executing - 'python -m unittest test_file.py'

# Thoughts -

# Input - file path

# Take command line argument - a file path

# Record the search term found on the last line of the file

# Check for substring within the line, if character is letter add to string and check if the next character is a not a letter. If so add a whitespace indicating the end of a word within the substring. Underscore characters are counted as alphabet characters and that case is handled specifically. The newline character signifies the end of the line and the output is ready to be formatted.

# A generator function to produce the correct list output

# Exception handling is key to good software design and was added to account for different behaviours

# Considerations -

# To ensure the functions are written clearly and produce a singular output, the search term and source text are searched for separately.

# I considered potential open the file and iterating backwards starting at the last line, this overcomplicated the code, a unittest was created for this case ensure the search term is of str type.

# Unittests were created for different cases related to the file and others created to test the component fucntions need to be integrated for the program.

# Tests include differing line quantity e.g no lines, one line, one thousand lines

# Test for potential addition of file extension compatibility

# Additional testing could involve performance, creating a baseline approximation based on a specific number of rows to get an average time the algorithm should operate at based on file input size. This would allow for future file size related testing.

# Testing for unicode characters was added, this testing allowed for me to update my current algorithm and improve upon it dealing with that edge case.

# The short dummy data files were added as they assisted in testing the code's behaviour with different cases. The unittests account for this but was used for quick testing.

# A logger was added to give the user a message in response to an action/event that has occur in the program.
