import os
import sys
import re
from log import logger



# may need to make while loop run till lines are fully read in file as opposed to indefinetly
class FileProcessor:
    def __init__(self, logger):
        self.logger = logger


    def check_path(self, filepath) -> bool:
        """Function to check if input is a file path
        :param filepath 
        """
        return os.path.isfile(filepath)
    

    def find_search_term(self, filepath) -> str:
        """Function will record value of the search term found on last line and return as a string
        :param filepath 
        """
   
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            try: 
                search_term = lines[-1].strip()
            except Exception as e:
                raise ValueError(f"Error occured when searching for a search term: {e}" )
            
        return search_term


    def read_file_contents(self, filepath) -> list:
        """Function will read the file's contents
        :param filepath
        """
       
        search_term = self.find_search_term(filepath)
        result = []
        with open(filepath, 'r', encoding='utf-8') as file: 
            lines = file.readlines()
            for line in lines[:-1]: 
                if search_term in line: 
                    output_string = ""
                    for index, char in enumerate(line): 
                        if char.isalpha(): #if character is letter add to string 
                            output_string += char 
                            if index < len(line) - 1 and not line[index+1].isalpha(): #if within bounds and next character is not letter add space
                                output_string += " "
                        elif char == "_":  #_  is included as letter not symbol character
                            output_string += " "
                        if index < len(line) -1 and line[index+1] == "\n": # if end of line  
                            output_string = output_string.strip()
                            formatted_string = re.sub(r'\s+', " ", output_string) #replace all whitespace with single space to format list
                            result.append([formatted_string])
        return result 
                 

    def yield_final_result(self, results) -> list: 
        """Generator Function takes the nested list and outputs individual lists
        :param results"""
        for result in results: 
            yield [elem for elem in result]


    def run(self):
        """Function takes file input from user and runs main algorithm"""

        results = None
        try:
            input_path = sys.argv[1]
            results = self.read_file_contents(input_path)
            if results: 
                for result in self.yield_final_result(results): 
                    print(result)
                self.logger.info("Code ran successfully")
            elif results == None or len(results) < 2: 
                self.logger.error(f'''An Error occurred, failed to generate results,
                    check file for correctly formatted source text and search term''')
        
        except Exception as e: 
            self.logger.error(f"An error occurred, please input correct file path: {str(e)}")
       
        
        
        


if __name__ == "__main__":
    file_processor = FileProcessor(logger)
    file_processor.run()


