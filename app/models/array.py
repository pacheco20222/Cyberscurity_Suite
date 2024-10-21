class Array():
    def __init__(self):
        self.array = []

    def insert(self, index, item):
        # Allow inserting at the end of the array when index == len(array)
        if 0 <= index <= len(self.array):
            self.array.insert(index, item)
            return True
        return False
    
    def delete(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
            return True
        return False

    def access(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        return None
    
    def update(self, index, item):
        if 0 <= index < len(self.array):
            self.array[index] = item
            return True
        return False
    
    def get_array(self):
        return self.array