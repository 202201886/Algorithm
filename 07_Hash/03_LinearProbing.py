class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):  # calculate the hash address
        return key % self.size

    def insert(self, key):  # find the first hash address
        index = self.hash_function(key)

        # check the next position if a collision occurs
        while self.table[index] is not None:
            if self.table[index] == key:
                return  # don't insert duplicate keys

            index = (index + 1) % self.size

        # store the key in the table
        self.table[index] = key

    def search(self, key):  # find the first hash address
        index = self.hash_function(key)
        start_index = index

        # check the next position if needed
        while self.table[index] is not None:
            if self.table[index] == key:
                return index

            index = (index + 1) % self.size

            if index == start_index:
                break

        return -1

    def print_table(self):  # print the stored keys
        for index, key in enumerate(self.table):
            if key is not None:
                print("HTABLE[" + str(index) + "] = " + str(key))

if __name__ == "__main__":
    table = HashTable(13)

    keys = [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]

    for key in keys:
        table.insert(key)

    table.print_table()