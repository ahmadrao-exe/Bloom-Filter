import hashlib

class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        for i in range(self.hash_count):
            h = hashlib.sha256((item + str(i)).encode()).hexdigest()
            yield int(h, 16) % self.size

    def add(self, item):
        for i in self._hashes(item):
            self.bit_array[i] = 1

    def check(self, item):
        return all(self.bit_array[i] for i in self._hashes(item))


# Initialize filter
bf = BloomFilter()

print("Bloom Filter Demo (type 'exit' to quit)")
while True:
    action = input("\nType 'add' to add email, 'check' to check email: ").strip().lower()
    if action == 'exit':
        break
    elif action == 'add':
        email = input("Enter email to add: ").strip()
        bf.add(email)
        print(f"{email} added to Bloom Filter.")
    elif action == 'check':
        email = input("Enter email to check: ").strip()
        if bf.check(email):
            print(f"{email} is possibly in the set.")
        else:
            print(f"{email} is definitely not in the set.")
    else:
        print("Invalid command. Please type 'add', 'check', or 'exit'.")
