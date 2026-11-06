class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):  # calculate the hash address
        return key % self.size

    def insert(self, key):  # find the first hash address
        start_index = self.hash_function(key)

        # check the next position if a collision occurs
        for i in range(self.size):
            index = (start_index + i ** 2) % self.size

            if self.table[index] == key:
                return  # don't insert duplicate keys

            if self.table[index] is None:  # store the key in the table
                self.table[index] = key
                return

        print("Hash table is full")

    def search(self, key):  # find the first hash address
        start_index = self.hash_function(key)

        # check the next position if needed
        for i in range(self.size):
            index = (start_index + i ** 2) % self.size

            if self.table[index] == key:
                return index

            if self.table[index] is None:
                return -1

        return -1

    def print_table(self):  # print the stored keys
        for index, key in enumerate(self.table):
            if key is not None:
                print("HTABLE[" + str(index) + "] = " + str(key))


if __name__ == "__main__":
    table = HashTable(13)

    keys = [15, 28, 41, 67, 54]

    for key in keys:
        table.insert(key)

    table.print_table()