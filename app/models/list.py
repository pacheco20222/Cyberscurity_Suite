import json
import os

class LogList:
    def __init__(self):
        """_We will initilize the list here, and we will get the path for the logs_
        """
        self.log_list = []
        self.path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'list_logs.json')
        self.load_logs_list()
        
    def load_logs_list(self):
        """_This method will load the logs from the logs file_
        """
        if os.path.exists(self.path):
            with open(self.path, 'r') as logfile:
                self.log_list = json.load(logfile)
    
    def save_logs_list(self):
        """_This method will save the logs to the logs file_
        """
        with open(self.path, 'w') as logfile:
            json.dump(self.log_list, logfile, indent=4)
    
    def access_log_list(self, index):
        """ 
        This method will be to access the list through the index
        """
        try:
            index = int(index)
            if 0 <= index <= len(self.log_list):
                return self.log_list[index]
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")
            return False
        
    def insert_log(self, element, index):
        """ 
        This will insert a log into the list
        """
        try:
            index = int(index)
            if 0 <= index <= len(self.log_list):
                self.log_list.insert(index, element)
                self.save_logs_list()
                return True
            else:
                raise IndexError
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")
            return False
        
    def update_log(self, element, index):
        """ 
        
        """