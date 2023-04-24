import unittest
import tempfile
import os
import re
import unicodedata
from main import FileProcessor
from log import logger 


class TestFileProcessing(unittest.TestCase): 
   
    
    
    def setUp(self):
        """Set up method to construct any global resources for tests"""
        self.valid_format = tempfile.NamedTemporaryFile(delete=False)
        self.valid_format.write("%^&This is an£$ ^&example@2343 of @£$the source^%$ text\n".encode('utf-8'))
        self.valid_format.write("Second23line has no string9?!\n".encode('utf-8'))
        self.valid_format.write("This£$@£$ is %£@434468^third(*$ line ofs43$2 source£267text\n".encode('utf-8'))
        self.valid_format.write("is\n".encode('utf-8'))
        self.valid_format.flush()
        self.valid_format.close() 

    def print_contents(self):
        """Print contents of the input file - debugging purposes"""
        with open(self.valid_format.name, 'r') as f: 
            for line in f: 
                print(line, end="")
            



    def tearDown(self) -> None: 
        """Tear down method to deconstruct any resources created for testing"""
        os.remove(self.valid_format.name)
        

    def test_empty_file(self): 
        """Test case for a file containing no lines """
        self.empty_file = tempfile.NamedTemporaryFile(delete=False)
        self.empty_file.close()

        with open(self.empty_file.name, 'r') as f: 
            lines = f.readlines()
        self.assertEqual(len(lines), 0 )

        os.remove(self.empty_file.name)

    def test_single_line_file(self): 
        """Test single line edge case, either no search term or no source text"""
        self.single_line_file = tempfile.NamedTemporaryFile(delete=False)
        self.single_line_file.write("A single line of text cannot contain source text and search term".encode('utf-8'))
        self.single_line_file.close()

        with open(self.single_line_file.name, 'r') as f: 
            lines = f.readlines()
        self.assertEqual(len(lines), 1)

        os.remove(self.single_line_file.name)

    def test_large_line_file(self): 
        """Test case for file containing large number of lines"""
        self.large_line_file = tempfile.NamedTemporaryFile(delete=False)
        for x in range(100_000): 
            self.large_line_file.write(f'This is line {x}\n'.encode('utf-8'))
        self.large_line_file.close()

        with open(self.large_line_file.name, 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 100_000)

        os.remove(self.large_line_file.name)

    def test_invalid_format(self): 
        """Testing file format for 'txt' files if required to be implemented"""
        self.txt_file = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        self.txt_file.close()

        with open(self.txt_file.name, 'r') as f: 
            self.file_name , self.extension = os.path.splitext(f.name)
        self.assertEqual(self.extension, ".txt")

        os.remove(self.txt_file.name) 

    def test_valid_search_term_reversed(self):
        """Testing alternative method of retrieving the search term, identifying the last line first"""
        search_term = ""
        with open(self.valid_format.name, "r") as f: 
            #move pointer to end of file, and return position
            f.seek(0, 2) 
            current_position = f.tell()


            while current_position > 0:
                current_position -= 1
                f.seek(current_position, 0)
                #newline character signifies end of line, read 1 character at a time
                if f.read(1) == '\n':
                    search_term = f.readline()
                    break
                else: 
                    search_term = f.readline()       
        self.assertIsInstance(search_term, str)

    def test_valid_search_term(self): 
        """Test to ensure the search term returned is a str type"""
        with open(self.valid_format.name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            try: 
                for line in lines: 
                    print(line.strip())
                search_term = lines[-1].strip()
            except Exception as e:
                raise ValueError(f"Error occured when reading lines: {e}" )
            
        self.assertIsInstance(search_term, str)

    def test_letter_only(self): 
        """Test to ensure only letters are added to final string"""
        f = FileProcessor(logger)
        search_term = f.find_search_term(self.valid_format.name)
        with open(self.valid_format.name, 'r', encoding='utf-8') as file: 
            lines = file.readlines()
            for line in lines[:-1]: 
                if search_term in line: 
                    #the pointer will point to character, if letter it will be added to string
                    output_string = ""
                    for index, char in enumerate(line): 
                        if char.isalpha(): 
                            output_string += char
                            if index < len(line) - 1 and not line[index+1].isalpha():
                                output_string += " "
                        elif char == "_":  
                            output_string += " "

        self.assertIsInstance(output_string, str)

    def test_file_algorithm_output(self): 
        """Test to ensure the output is of list type after being constructed by main algorithm"""
        f = FileProcessor(logger)
    
        search_term = f.find_search_term(self.valid_format.name)
        result = []
        with open(self.valid_format.name, 'r', encoding='utf-8') as file: 
            lines = file.readlines()
            for line in lines[:-1]: 
                if search_term in line: 
                    #the pointer will point to character, if letter it will be added to string
                    output_string = ""
                    for index, char in enumerate(line): 
                        if char.isalpha(): 
                            output_string += char
                            if index < len(line) - 1 and not line[index+1].isalpha():
                                output_string += " "
                        elif char == "_":  
                            output_string += " "
                        if index < len(line) -1 and line[index+1] == "\n": 
                            output_string = output_string.strip()
                            formatted_string = re.sub(r'\s+', " ", output_string)
                            result.append([formatted_string])
        
        self.assertIsInstance(result, list)

    def test_unicode_characters(self):
        
        test_string = "i told_her334Le vent se 7%3lève! . . . Il faut te@£nter de viv5)re!"
        unicode_char = "è"
        output_string = ""

        for index, char in enumerate(test_string): 
            if unicodedata.category(char)[0] == 'L':  # check if character is a letter
                output_string += char
                if index < len(test_string) - 1 and unicodedata.category(test_string[index+1])[0] != 'L':
                    output_string += " "
            elif char == "_":  
                output_string += " "
        
        self.assertIn(unicode_char, output_string) #assert that unicode character should be accounted for and added to the output string 



    def test_yield_function(self): 
        """Test ensuring generator function returns list object"""
        f = FileProcessor(logger)
        results = f.read_file_contents(self.valid_format.name)
        for result in results: 
            self.assertIsInstance(result, list)



if __name__ == "__main__":

    test = TestFileProcessing()
    
    test.setUp()
    test.print_contents()
    test.test_unicode_characters()

    
    


