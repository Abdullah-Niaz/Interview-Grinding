class HashMap:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                del self.buckets[index][i]
                return

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


students = HashMap()

students.insert(101, ("omer", 20))
students.insert(102, ("talha", 30))
students.insert(103, ("ali", 40))


students.display()

print(students.search(103))


students.insert(103, ("Ali", 95))


print(students.search(103))


students.delete(101)
students.display()
