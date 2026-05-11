# Lab 04: Quicksort

## 1. Overview

In this lab you will implement the **quicksort** algorithm — one of the most widely used sorting algorithms in computer science. Quicksort uses a **divide-and-conquer** strategy: pick a pivot, partition the array into smaller and larger elements, and recursively sort each partition.

### Objectives
- Understand the quicksort algorithm and its divide-and-conquer approach
- Implement a recursive sorting algorithm in Python
- Analyze the efficiency of quicksort (average vs. worst case)

### Prerequisites
- Familiarity with recursion (Lab 03)
- Basic understanding of sorting algorithms
- Experience with Python functions and lists

---

## 2. Algorithm Background

### How Quicksort Works

1. **Pick a pivot** — choose an element from the array (we'll use the first element)
2. **Partition** — split the remaining elements into two groups:
   - Elements **less than or equal to** the pivot
   - Elements **greater than** the pivot
3. **Recurse** — quicksort each group
4. **Combine** — concatenate: `sorted_less + [pivot] + sorted_greater`

### Visual Example

```
quicksort([10, 5, 2, 3])

  pivot = 10
  less_than_or_equal = [5, 2, 3]
  greater = []

  quicksort([5, 2, 3])
    pivot = 5
    less_than_or_equal = [2, 3]
    greater = []

    quicksort([2, 3])
      pivot = 2
      less_than_or_equal = []
      greater = [3]

      quicksort([]) → []        ← Base case!
      quicksort([3]) → [3]      ← Base case!

      result: [] + [2] + [3] = [2, 3]

    result: [2, 3] + [5] + [] = [2, 3, 5]

  result: [2, 3, 5] + [10] + [] = [2, 3, 5, 10]
```

### Time Complexity

| Case | Complexity | When It Happens |
|------|-----------|-----------------|
| **Average** | O(n log n) | Random or mixed data |
| **Best** | O(n log n) | Good pivot choices |
| **Worst** | O(n²) | Already sorted data with first-element pivot |

---

## 3. Getting Started

### How to Access This Lab

1. Go to your **Section page** on StudySite.ai
2. Find **"Lab 04: Quicksort"** in the Portfolio Assignments list
3. Click **"Start Coding"** to open the coding environment

### First Time Setup

When you open the lab for the first time:
1. You'll be prompted to **accept the GitHub Classroom assignment** — this creates your personal copy of the lab repository
2. Click **"Accept on GitHub"** and complete the process in the popup window
3. Once accepted, your starter code loads automatically into the editor

### Your Coding Workflow

The StudySite.ai coding environment gives you everything you need:

| Area | What It Does |
|------|-------------|
| **Code Editor** (left) | Edit your `main.py` file using the tabbed editor |
| **Terminal** (right) | See output when you click the Run button |
| **AI Tutor** (chat panel) | Ask your AI Tutor for help — it knows this lab and can guide you step by step |

**How to work on the lab:**

1. **Edit** your code in `main.py` (click the tab to switch files)
2. Click the **▶ Run** button to execute your code and see output in the terminal
3. Click the **Commit** button to save your work to GitHub and trigger the autograder
4. After a few moments, you'll see a ✅ (green check) or ❌ (red X) indicating whether your tests passed

> **Tip:** Commit early and often! Every commit triggers the autograder so you can see your progress.

---

## 4. Project Structure

```
lab04_quicksort/
├── main.py                   # YOUR WORK - implement quicksort here
├── Instructions/             # This file
├── README.md                 # Your lab report (fill in after coding)
└── _tutor-guides/            # AI tutor reference (hidden)
```

---

## 5. Step-by-Step Implementation

Open the `main.py` tab and implement the `quicksort` function by following these steps.

### Step 1: Handle the Base Case

The base case stops the recursion. An array with 0 or 1 elements is already sorted.

```python
def quicksort(array):
    # Step 1: Base case — if the array has fewer than 2 elements, it's already sorted
    if len(array) < 2:
        return array
```

**Why?** An empty list `[]` or a single-element list `[5]` doesn't need sorting. Just return it as-is.

**After this step:** Click **▶ Run**. The last two test cases (`[1]` and `[]`) should now print correctly.

### Step 2: Choose the Pivot

The pivot is the element we compare everything else against. We'll use the **first element**.

```python
    # Step 2: Choose the pivot (first element)
    pivot = array[0]
```

### Step 3: Partition into Two Groups

Use list comprehensions to split the remaining elements (everything after the pivot) into two groups:

```python
    # Step 3: Partition — elements <= pivot go left, elements > pivot go right
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
```

**Key details:**
- `array[1:]` means "everything except the first element" (since the first element is our pivot)
- `less` contains elements **less than or equal to** the pivot
- `greater` contains elements **greater than** the pivot

### Step 4: Recurse and Combine

Recursively sort each partition, then combine them with the pivot in the middle:

```python
    # Step 4: Recursively sort each partition and combine
    return quicksort(less) + [pivot] + quicksort(greater)
```

**Why `[pivot]`?** The pivot is a single value, but we need it as a list to concatenate with the other sorted lists.

### Complete Solution

When you're done, your function should look like this:

```python
def quicksort(array):
    # Base case
    if len(array) < 2:
        return array
    
    # Choose pivot
    pivot = array[0]
    
    # Partition
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    
    # Recurse and combine
    return quicksort(less) + [pivot] + quicksort(greater)
```

---

## 6. Testing Your Code

### Test Locally

Click the `main.py` tab, then click the **▶ Run** button. You should see this output:

```
[2, 3, 5, 10]
[10, 15, 33]
[1, 2, 3, 4, 5]
[1]
[]
[1, 2, 3, 4, 5, 6, 7, 8]
```

### Submit for Grading

1. Click the **Commit** button in the editor toolbar
2. Enter a commit message (e.g., "Implement quicksort")
3. The autograder runs automatically on GitHub
4. Look for ✅ (green check) or ❌ (red X) — you can commit as many times as you need

---

## 7. Autograding

Your code is graded automatically each time you click **Commit**. The autograder runs these tests:

| Test | Points | What It Checks |
|------|--------|---------------|
| Syntax and Compilation Check | 10 | `main.py` compiles without syntax errors |
| Functional Test - Quicksort Output | 90 | All 6 test cases produce correct sorted output |

**Total: 2 tests, 100 points**

---

## 8. Lab Report

After completing the code, click the `README.md` tab and fill in your lab report:

```markdown
# Lab 04: Quicksort

## Student Information
- **Name:** Dongnhyun Lee
- **Date:** 05/10/26

## Quicksort Concepts

### Divide and Conquer
[Explain how quicksort uses divide-and-conquer in your own words]
Making easy to solve smaller problems, a big problem can be solved like it is 'divided' and 'conquered' like an easy piece of cake. 
### The Three Steps
1. **Choose pivot:** [Explain] Choose any element and make it be compared to the other elements.
2. **Partition:** [Explain] Reorder the array based on the pivot you chose. Bigger ones to the right and smaller ones to the left. 
3. **Recurse and combine:** [Explain] Repeat the process recursively until it reaches the base case of having no more partitions then combine back to the first recursion. 

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
[Draw out each recursive call step by step, showing the pivot, less, and greater at each level]
quicksort([3, 5, 2, 1, 4])
  pivot = 3
  less    = [2, 1]
  greater = [5, 4]

  quicksort([2, 1])
    pivot = 2
    less    = [1]
    greater = []

    quicksort([1]) → [1]   # base case
    quicksort([]) → []     # base case

    → [1] + [2] + [] = [1, 2]

  quicksort([5, 4])
    pivot = 5
    less    = [4]
    greater = []

    quicksort([4]) → [4]   # base case
    quicksort([]) → []     # base case

    → [4] + [5] + [] = [4, 5]

  → [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]


## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | The pivot is always the medium value that splits partitions very evenly which is unlikely  |
| Average | O(n log n) | The pivot is moderately the medium value  |
| Worst | O(n²) | It is always the smallest or the largest value so it is mostly no different from selection sort  |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
It is the worst case and larger partitions are always the biggest therefore making the pivot selection process meaningless. 
2. How could you improve pivot selection to avoid worst-case performance?
Rnadomize the pivot or maybe check if the list is sorted already or reverse or so.
3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
It is a good search since the real world data would be much and much bigger inputs, and for quicksort, it is better memory than merge sort. 
4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
Because the first element is the pivot itself and it should be excluded from the list of values to be compared.
```

---

## 9. Submission Checklist

- [ ] `quicksort` function implemented in `main.py`
- [ ] Click **▶ Run** on `main.py` — output matches expected output
- [ ] Click **Commit** — autograder shows ✅ (green check)
- [ ] Lab report completed in `README.md`
- [ ] Final commit with completed lab report
