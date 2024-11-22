"""
We will be reading AI generated logs for each data structure, which will be located in the app/logs folder.
So we will be importing the os library to be able to read files, and the json library to help with converting data to the json format.
"""

import os
import json

class Array:
    def __init__(self):
        """
        Initialize the Array class with an empty array and define the path to the logs.
        Load the current array from the file array_logs.json.
        """
        self.array = []
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'array_logs.json') # Join the path ../logs/array_logs.json, since we need to go one directory back
        self.load_array()
        
    def current_array(self):
        """
        Return the current array.
        This ensures that we have the latest data from the file in case the user has made any changes.
        """
        return self.array
        
    def load_array(self):
        """
        Read the json file for the data and store it in the array.
        """
        if os.path.exists(self.logs_path):
            with open(self.logs_path, "r") as logfile: # Give the name logfile to the file being read
                self.array = json.load(logfile)
                
    def save_array(self):
        """
        Save the array when the user makes any changes.
        Save the data provided by the user.
        """
        with open(self.logs_path, 'w') as logfile:
            json.dump(self.array, logfile, indent=4) # Provide the indent 4, to get the matching format
            
    def insert_log(self, log, index):
        """
        Insert an item (log) into the array at the specified index.
        The method checks the index before inserting the element.
        
        Parameters:
        log (any): The log to be inserted.
        index (int): The position at which to insert the log.
        
        Returns:
        bool: True if insertion is successful, False otherwise.
        """
        try:
            index = int(index) # Ensure the index is an integer
            if 0 <= index <= len(self.array):
                self.array.insert(index, log)
                self.save_array() # Save the changes after adding a log
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as error:
            print(f"Error: {error}")
            return False
        
    def delete_log(self, index):
        """
        Delete the element at the specified index.
        The method checks the index before deleting the element.
        
        Parameters:
        index (int): The position of the log to be deleted.
        
        Returns:
        bool: True if deletion is successful, False otherwise.
        """
        try:
            index = int(index) # Ensure the index is an integer
            if 0 <= index < len(self.array): # Corrected the condition to allow deletion of the last element
                self.array.pop(index)
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as error:
            print(f"Error: {error}")
            return False
            
    def get_log(self, index):
        """
        Access the element at the specified index.
        The method checks the index before accessing the element.
        
        Parameters:
        index (int): The position of the log to be accessed.
        
        Returns:
        any: The log at the specified index if successful, None otherwise.
        """
        try:
            index = int(index) # Ensure the index is an integer
            if 0 <= index < len(self.array): # Corrected the condition to allow access to the last element
                return self.array[index]
            else:
                raise IndexError
        except (ValueError, IndexError) as error:
            print(f"Error: {error}")
            return None
            
    def update_log(self, log, index):
        """
        Update the log at the specified index with a new log.
        The method checks the index before updating the element.
        
        Parameters:
        log (any): The new log to replace the old log.
        index (int): The position of the log to be updated.
        
        Returns:
        bool: True if update is successful, False otherwise.
        """
        try:
            index = int(index) # Ensure the index is an integer
            if 0 <= index < len(self.array): # Corrected the condition to allow updating the last element
                self.array[index] = log
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as error:
            print(f"Error: {error}")
            return False