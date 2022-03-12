class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
    def hash(self, key):
        # Arguments: key
        # Returns: Index in the collection for that key
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 97
        index = primed % self.size
        return index
    def set(self, key, value):
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.
       index = self.hash(key)
       key_found = False

       for i, record in enumerate(self.buckets[index]):
           if len(record) == 2 and record[0] == key:
               self.buckets[index][i] = (key, value)
               key_found = True
               break
           if not key_found:
               self.buckets[index].append((key,value))
    def get(self, key):
        # Arguments: key
        # Returns: Value associated with that key in the table
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return record[1]
    def contains(self, key):
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return True
    def keys(self):
        # Returns: Collection of keys
        pass

if __name__ == '__main__':
    table = Hashtable()
    print(table.hash('dog'))
