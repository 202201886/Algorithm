class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):  # calculate the hash address
        return key % self.size

    def insert(self, key):  # find the hash address
        index = self.hash_function(key)

        # store the key in the table
        self.table[index] = key

    def search(self, key):  # find the hash address
        index = self.hash_function(key)

        # check if the key exists
        if self.table[index] == key:
            return index

        return -1

    def print_table(self):  # print the stored keys
        for index, key in enumerate(self.table):
            if key is not None:
                print("HTABLE[" + str(index) + "] = " + str(key))


if __name__ == "__main__":
    table = HashTable(1601)

    keys = [1025390, 1025400, 1025420, 1025700, 1025900]

    for key in keys:
        table.insert(key)

    table.print_table()