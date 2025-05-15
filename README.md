# Bloom-Filter
Bloom Filter is a space-efficient, probabilistic data structure for set membership testing. It can tell you definitely not (if the element is absent) or probably yes (if the element is present, with a small false-positive rate) in constant time and with very low memory overhead.
Key Operations
Add an element to the set.
Check whether an element is in the set.
How It Works
Uses a fixed-size bit array of length m.
Applies k independent hash functions to each element, mapping it to k bit positions.
Add: Set all k bits to 1.
Check: If any of the k bits is 0, the element is definitely not in the set; otherwise, it’s probably in the set.
Pros & Cons
✅ Very memory-efficient for large sets.
✅ Constant-time add and check.
❌ False positives possible (controlled by m and k).
❌ No deletions (unless you use a counting Bloom filter variant).
# Source Code
A Python implementation of a Bloom Filter: a space-efficient probabilistic set membership structure.  
Full code in src/bloom_filter.py .
