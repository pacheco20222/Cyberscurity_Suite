"""
I will import os library so we can use the os.path.join() function to join the path of the file for the logs.
Will also import json library to convert the data to json format.
"""
import os
import json

class Array:
    def __init__(self):
        self.array = []
        # Next we will get the log files path
        self.logs_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'array_logs.json')
        self.load_array()
    
    def return_array(self):
        """
        This will return the array, which will be the current data in the logs files
        """
        return self.array
    
    def load_array(self):
        """
        I will use this method to get the data from the logs file and store it in the array
        in the /app/logs/array_logs.json file.
        """
        if os.path.exists(self.logs_path): # Check if the file exists
            with open(self.logs_path, 'r') as logfile:
                self.array = json.load(logfile)
    
    def save_array(self):
        """
        I will use this method to save the array data to the logs file.
        """
        with open(self.logs_path, 'w') as logfile:
            json.dump(self.array, logfile, indent=4)
    
    def insert_element(self, element, index):
        """"
        This is one of the important methods of an array, which is to insert an element. I will check for valid index
        and then insert the element at the index.
        """
        try:
            index = int(index) # Making sure the index is an integer
            if 0 <= index <= len(self.array):
                self.array.insert(index, element)
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Eerror: {e}")
            return False
        
    def delete_element(self, index):
        """
        This is another important method of an array, which is to delete an element. I will check for valid index
        and then delete the element at the index.
        """
        try:
            index = int(index) # Making sure the index is an integer
            if 0 <= index < len(self.array):
                self.array.pop(index)
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")
            return False
    
    def update_element(self, element, index):
        """
        This is another important method of an array, which is to update an element. I will check for valid index
        and then update the element at the index.
        """
        try:
            index = int(index) # Making sure the index is an integer
            if 0 <= index < len(self.array):
                self.array[index] = element
                self.save_array()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")
            return False
    
    def access_element(self, index):
        """
        This is another important method of an array, which is to access an element. I will check for valid index
        and then access the element at the index.
        """
        try:
            index = int(index) # Making sure the index is an integer
            if 0 <= index < len(self.array):
                return self.array[index]
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")
            return False