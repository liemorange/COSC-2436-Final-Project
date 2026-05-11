# Lab 5: Implementing a Hash Table

### Objectives
- Implement a basic hash table with linear probing for collision resolution
- Understand hash functions and their role in hash tables
- Practice handling collisions in a hash table

### Prerequisites
- Basic understanding of Python classes and functions
- Familiarity with list operations in Python

---

## 2. Algorithm/Concept Background
A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array, where each key-value pair is stored. If two keys hash to the same index, a collision occurs, which can be resolved using techniques like linear probing.

Example of linear probing:
```python
# Suppose hash_table = [None, None, None, None]
# Insert key 'a' with hash 1
hash_table[1] = ('a', value_a)
# Insert key 'b' with hash 1 (collision)
# Probe next slot
hash_table[2] = ('b', value_b)
```

| Property | Value |
|---|---|
| Time Complexity (Average) | O(1) |
| Time Complexity (Worst) | O(n) |
| Space Complexity | O(n) |

---

## 3. Your Coding Environment
### Workspace Layout
| Area | What It Does |
|---|---|
| Code Editor (left) | Edit your files using the tabbed editor |
| Terminal (right) | See output when you click the **Run** button |
| AI Tutor (chat panel) | Ask your AI Tutor for help — it knows this lab and can guide you step by step |

### Workflow
1. Edit your code in the editor tabs
2. Click **Run** to execute and see output in the terminal
3. When ready, click **Commit** to save your work to GitHub and trigger the autograder
4. A ✅ (green check) or ❌ (red X) will appear showing whether tests passed

Tip: Commit early and often to track your progress!

---

## 4. Project Structure
```
.
├── main.py  # YOUR WORK
```

---

## 5. Step-by-Step Implementation

### Step 1: Implement the `__init__` Method
Add code to initialize the hash table with a given size and set up the internal storage.
```python
def __init__(self, size: int):
    self.size = size
    self.table = [None] * size
```
This sets up the hash table with the specified size and initializes all positions to `None`.

### Step 2: Implement the `hash_function` Method
Add code to compute the hash index for a given key.
```python
def hash_function(self, key: Any) -> int:
    return hash(key) % self.size
```
This function returns an index based on the hash of the key and the table size.

### Step 3: Implement the `insert` Method
Add code to insert key-value pairs into the hash table, handling collisions with linear probing.
```python
def insert(self, key: Any, value: Any) -> None:
    index = self.hash_function(key)
    while self.table[index] is not None:
        index = (index + 1) % self.size
    self.table[index] = (key, value)
```
This code finds an empty slot using linear probing and inserts the key-value pair there.

### Step 4: Implement the `search` Method
Add code to find a value associated with a given key, handling collisions.
```python
def search(self, key: Any) -> Any:
    index = self.hash_function(key)
    start_index = index
    while self.table[index] is not None:
        if self.table[index][0] == key:
            return self.table[index][1]
        index = (index + 1) % self.size
        if index == start_index:
            return None
    return None
```
This searches for the key using linear probing and returns the associated value if found.

### Step 5: Test Your Code
Click **Run** — the output should match the expected output.

---

## 6. Testing Your Code
### Run Your Code
Click **Run** to execute and check the output.

### Submit for Grading
Click **Commit**, enter a message, and look for ✅ or ❌.

Expected output:
```
100
200
300
None
```

---

## 7. Autograding
| Test | Points | What It Checks |
|---|---|---|
| Compilation and Syntax Check | 10 | Code compiles without errors |
| Functional Test | 90 | Correctness of hash table operations |

Total: 100 points

---

## 8. Lab Report
Click the README.md tab and fill in your lab report.

```markdown
# Lab Report

## Student Information
- **Name:** Donghyun Lee   
- **Date:** 05/10/26

## Key Concepts
- Describe what a hash table is and how it works.
- Explain linear probing and its role in handling collisions.

## Tracing Exercise
- Trace through the example where keys 'apple', 'banana', and 'orange' are inserted.
- Show the state of the hash table after each insertion.

## Complexity Analysis
| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |

## Reflection Questions
1. What are the advantages of using a hash table?
That it has both advantages of arrays and linked lists when the table is well optimized in average.
2. How does the hash function affect the performance of a hash table?
It affects the most problematic issue of optimizing a hash table, which are mostly even distribution and collision handling  to keep the time complexity consistent to take average case of O(1).
3. What are other collision resolution techniques besides linear probing?
Chaining that creates a linked list is used to avoid collision. Also, there are quadratic probing similar to linear probing, and double hashing that uses a second hash function.
```

---

## 9. Submission Checklist
- [ ] All functions implemented
- [ ] Click Run — output matches expected
- [ ] Click Commit — autograder shows green check
- [ ] Lab report completed in README.md
- [ ] Final commit with completed lab report