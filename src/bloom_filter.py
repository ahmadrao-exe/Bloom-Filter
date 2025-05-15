import hashlib
import math
import random

class BloomFilter:
    def __init__(self, expected_items, false_positive_rate):
        """
        Initialize a Bloom Filter.

        Args:
            expected_items (int): Number of items you expect to store.
            false_positive_rate (float): Desired false-positive probability (e.g. 0.01).
        """
        # Calculate size of bit array (m) and number of hash functions (k)
        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_items)
        self.bit_array = [0] * self.size

    def _optimal_size(self, n, p):
        """
        m = - (n * ln(p)) / (ln(2)^2)
        """
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _optimal_hash_count(self, m, n):
        """
        k = (m / n) * ln(2)
        """
        k = (m / n) * math.log(2)
        return max(1, int(k))

    def _hashes(self, item):
        """
        Generate k hash values for the item using SHA-256 with different salts.
        """
        for i in range(self.hash_count):
            # Create a unique seed
            seed = i.to_bytes(2, byteorder='little', signed=False)
            digest = hashlib.sha256(seed + item.encode('utf-8')).hexdigest()
            # Convert hex digest to integer and map to bit array index
            yield int(digest, 16) % self.size

    def add(self, item):
        """Add an item to the Bloom filter."""
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def __contains__(self, item):
        """Check membership (use: `if item in bloom:`)."""
        return all(self.bit_array[index] for index in self._hashes(item))


if __name__ == "__main__":
    # Example usage
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)

    # Add some items
    bf.add("alice@example.com")
    bf.add("bob@example.com")
    bf.add("carol@example.com")

    # Check membership
    test_emails = ["alice@example.com", "dave@example.com"]
    for email in test_emails:
        if email in bf:
            print(f"{email} is possibly in the set.")
        else:
            print(f"{email} is definitely not in the set.")
