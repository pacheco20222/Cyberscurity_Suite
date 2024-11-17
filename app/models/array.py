"""
We will be reading AI generated logs for each data structure, which will be located in the app/logs folder
So we will be importing the os library to be able to read files, and the json library to help with converting data to the json format
"""

import os
import json

class Array:
    def __init__(self):
        """
        class array, where we will define a empty array at first, and dfefine the path to the logs
        and we will load the current array in the file array_logs.json
        """
        self.array = []
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'array_logs.json') # Here we are joining the path ../logs/array_logs.json, since we need to go one directory back
        self.load_array()
        
    def current_array(self):
        """Here we are just returning the current array 
        (in any case the user has made any changes we want to have the current data from the file)"""
        return self.array
        
    def load_array(self):
        """
        This method is the one I use to read the json file for the data, and store it in the array
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, "r") as logfile: #Give the name logfile to the file I am reading
                self.array = json.load(logfile)
                
    def save_array(self):
        """Here we simply will save the array when the user makes any changes, save with the data the user provided"""
        with open(self.logs_path, 'w') as logfile:
            json.dump(self.array, logfile, indent=4) # provide the indent 4, to get tha matching format
            
    def insert_log(self, log, index):
        """
        Here we give the user the option to insert a item (log) to the array
        the method checks the index before it inserts the element
        """
        try:
            index = int(index) #This is just to make sure it gets the index as an integer
            if 0 <= index <= len(self.array):
                self.array.insert(index, log)
                self.save_array() #Save the changes when adding a log
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as error:
            print(f"Error: {error}")
            return False
        
    def delete_log(self, index):
        """Again I check for index, and validate and then delete that element in that index"""
        try:
            index = int(index) #Check if the user provides a valid int as an index
            if 0 <= index <= len(self.array):
                self.array.pop(index)
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as error:
            print(f"Error: {error}")
            
    def get_log(self, index):
        """
        The user will be able to access the element, again, I will check for a valid index
        before letting the user access the element
        """
        try:
            index = int(index) #This is just to make sure it gets the index as an integer
            if 0 <= index <= len(self.array):
                return self.array[index]
            else:
                raise ValueError
        except (ValueError, IndexError) as error:
            print(f"Error: {error}")
            
    def update_log(self, log, index):
        """ Check again for the index, and get the index and the log user wants to update with"""
        try:
            index = int(index) #Check if the user provides a valid int as an index
            if 0 <= index <= len(self.array):
                self.array[index] = log
                self.save_array()
                return True
            else:
                raise IndexError
        except(IndexError, ValueError) as error:
            print(f"Error: {error}")