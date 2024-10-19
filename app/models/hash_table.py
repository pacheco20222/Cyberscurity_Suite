class HashTable:
    def __init__(self):
        self.size = 10  # You can adjust the size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        for idx, element in enumerate(self.table[hashed_key]):
            if element[0] == key:
                self.table[hashed_key][idx] = (key, value)  # Update value if key exists
                return
        self.table[hashed_key].append((key, value))  # Add new key-value pair

    def search(self, key):
        hashed_key = self._hash(key)
        for element in self.table[hashed_key]:
            if element[0] == key:
                return element[1]  # Return value if found
        return None

    def delete(self, key):
        hashed_key = self._hash(key)
        for idx, element in enumerate(self.table[hashed_key]):
            if element[0] == key:
                del self.table[hashed_key][idx]  # Delete the key-value pair
                return True
        return False

    def get_table(self):
        return self.table