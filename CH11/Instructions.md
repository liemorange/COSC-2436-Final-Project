# Knapsack Problem — Dynamic Programming

> A beginner-friendly walkthrough. Every line of code you need is in this file, along with the reasoning behind it. Work through each part in order.

---

## Table of Contents

1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [Why Dynamic Programming?](#2-why-dynamic-programming)
3. [How the DP Grid Works](#3-how-the-dp-grid-works)
4. [A Tiny Warm-Up by Hand](#4-a-tiny-warm-up-by-hand)
5. [Setup](#5-setup)
6. [Part 1 — `calculate_total_value` (TODO 1)](#6-part-1--calculate_total_value-todo-1)
7. [Part 2 — Fill the DP Grid (TODOs 2–5)](#7-part-2--fill-the-dp-grid-todos-25)
8. [Part 3 — Display the Grid (TODOs 6–9)](#8-part-3--display-the-grid-todos-69)
9. [Part 4 — Run the Program (TODOs 10–11)](#9-part-4--run-the-program-todos-1011)
10. [Expected Output](#10-expected-output)
11. [Understanding the Letter Codes](#11-understanding-the-letter-codes)
12. [Debugging Checklist](#12-debugging-checklist)
13. [Submission](#13-submission)

---

## 1. The Problem in Plain English

You are packing a knapsack (a backpack) and you can only carry a fixed amount of weight — for example, 6 kilograms. You have a list of items to choose from. Each item has:

- a **name** (e.g., "GUITAR")
- a **weight** (how heavy it is)
- a **value** (how much money it's worth)

Your goal: **pick the combination of items that has the highest total value and still fits inside the weight limit**.

This assignment's test data:

| Item     | Weight (kg) | Value ($) |
| -------- | ----------- | --------- |
| GUITAR   | 1           | 1,500     |
| STEREO   | 4           | 3,000     |
| LAPTOP   | 3           | 2,000     |
| iPHONE   | 1           | 2,000     |
| BOOK     | 2           | 100       |
| GOLD BAR | 1           | 30,000    |

Knapsack capacity: **6 kg**.

**Think about it before reading on.** Can you eyeball the best answer? (The goal is $35,500. If you can't find it by hand, don't worry — that's exactly what dynamic programming is for.)

---

## 2. Why Dynamic Programming?

A naive approach would try every possible combination of items — include/exclude each one — and pick the best. With 6 items that's only 2⁶ = 64 combinations, but with 30 items it's over a billion. Brute force does not scale.

**Dynamic programming (DP)** is a technique that breaks a big problem into smaller overlapping subproblems, solves each subproblem exactly once, and stores the answer so we never re-compute it.

The key insight for knapsack: *if I already know the best way to pack the first 3 items into a 4 kg knapsack, I can use that to quickly figure out the best way to pack the first 4 items into a 4 kg knapsack — I only have to decide whether to add item #4 or not.*

That's the include-or-exclude decision we'll make in every cell of the grid.

---

## 3. How the DP Grid Works

We'll build a 2-dimensional grid. One dimension is "how many items are we allowed to consider" and the other is "what's our weight budget":

```
grid[i][w]  ==  the best list of items
                when we can ONLY use items 1..i
                and the total weight must be ≤ w
```

**Important:** each cell stores a **list of item names** like `["GUITAR", "LAPTOP"]`, **not** a dollar amount. We compute the dollar value from the list whenever we need it, using a helper function you'll write in Part 1.

### The recurrence

For every cell `grid[i][w]` we ask one question: *can the current item (item i) fit in budget w?*

```
if weight[i] > w:
    grid[i][w] = grid[i-1][w]                        # can't fit — just copy above
else:
    include = grid[i-1][w - weight[i]] + [item i]    # take it
    exclude = grid[i-1][w]                           # leave it
    grid[i][w] = whichever list is worth more
```

That's the whole algorithm. Everything else is plumbing.

---

## 4. A Tiny Warm-Up by Hand

Let's do a miniature version so the grid isn't scary:

**Items:** `GUITAR (1 kg, $1500)`, `LAPTOP (3 kg, $2000)`
**Capacity:** 3

The grid has 3 rows (0, 1, 2) and 4 columns (0, 1, 2, 3).

**Row 0** (no items allowed): every cell is `[]` — you can't pack anything.

**Row 1** (GUITAR only, weight 1):

| w | include branch            | exclude branch | winner          |
| - | ------------------------- | -------------- | --------------- |
| 1 | `[] + [GUITAR]` = $1500   | `[]` = $0      | `[GUITAR]`      |
| 2 | `[] + [GUITAR]` = $1500   | `[]` = $0      | `[GUITAR]`      |
| 3 | `[] + [GUITAR]` = $1500   | `[]` = $0      | `[GUITAR]`      |

**Row 2** (add LAPTOP, weight 3):

| w | can LAPTOP fit? | include branch                    | exclude branch        | winner             |
| - | --------------- | --------------------------------- | --------------------- | ------------------ |
| 1 | no (3 > 1)      | —                                 | copy row 1: `[GUITAR]`| `[GUITAR]`         |
| 2 | no (3 > 2)      | —                                 | copy row 1: `[GUITAR]`| `[GUITAR]`         |
| 3 | yes             | `grid[1][0] + [LAPTOP]` = $2000   | `grid[1][3]` = $1500  | `[LAPTOP]` (wins)  |

So the final answer at `grid[2][3]` is `[LAPTOP]`, worth $2000. That makes sense — you can't fit both, and the laptop alone is more valuable than the guitar alone.

Keep this table in mind as you write the real thing below. If the big version confuses you, come back to this.

---

## 5. Setup

1. Accept the GitHub Classroom assignment.
2. Clone your repository locally.
3. Open `main.py` in your editor.
4. Read through **all** of `main.py` first. Notice the 11 TODOs — you'll fill them in order.
5. You'll also need Python 3.10+. Check with `python3 --version`.

---

## 6. Part 1 — `calculate_total_value` (TODO 1)

### Why we need this

Our grid stores **lists of names**, but to compare two candidate lists we need to know their **dollar totals**. This helper converts one to the other.

### The code

Find **TODO 1** at the top of `main.py`:

```python
def calculate_total_value(solution, items):
    # TODO 1 — implement this helper (see Instructions Part 1).
    pass
```

Replace the body with:

```python
def calculate_total_value(solution, items):
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total
```

### What each line does

- `total = 0` — start an accumulator at zero.
- `for name in solution:` — loop over every name in the candidate list (names like `"GUITAR"`).
- `for item_name, weight, value in items:` — for each name, scan the master `items` list to find its entry.
- `if item_name == name:` — when we find a match…
- `total += value` — add that item's dollar value to the accumulator.
- `break` — stop scanning `items` as soon as we found the match (one match per name is all we need).
- `return total` — hand back the final sum.

### Quick sanity check

If `solution = ["GUITAR", "LAPTOP"]` and `items` is the full list from the bottom of the file, this should return `1500 + 2000 = 3500`.

---

## 7. Part 2 — Fill the DP Grid (TODOs 2–5)

### TODO 2 — handle "item too heavy"

Find:

```python
if weight > w:
    # TODO 2 — this item is too heavy; copy the cell directly above.
    pass
```

Replace the `pass` with:

```python
grid[i][w] = grid[i - 1][w][:]
```

**Why the `[:]`?** It makes a **copy** of the list. If you wrote `grid[i][w] = grid[i-1][w]` without the slice, both cells would point to the same list in memory — adding to one would secretly change the other, corrupting your grid. Always slice-copy.

---

### TODO 3 — build the two candidate lists

Find:

```python
# TODO 3 — build the two candidate solutions (each is a LIST of names).
include_solution = None
exclude_solution = None
```

Replace with:

```python
include_solution = grid[i - 1][w - weight][:] + [item_name]
exclude_solution = grid[i - 1][w][:]
```

**What's going on:**
- `include_solution` = "what if I take this item?" — start with the best list for the first `i-1` items in the remaining weight budget (`w - weight`), then append the current item's name.
- `exclude_solution` = "what if I skip this item?" — just the best list from above, unchanged.

Again, we `[:]`-copy so we don't mutate cells we've already filled in.

---

### TODO 4 — compute each candidate's dollar value

Find:

```python
# TODO 4 — compute each candidate's dollar value (each is an INTEGER).
include_value = None
exclude_value = None
```

Replace with:

```python
include_value = calculate_total_value(include_solution, items)
exclude_value = calculate_total_value(exclude_solution, items)
```

We're using the helper from Part 1. `include_value` and `exclude_value` are **integers** (dollar totals). Don't confuse them with the `_solution` variables, which are **lists**.

---

### TODO 5 — pick the winner

Find:

```python
# TODO 5 — store whichever solution has the higher value in grid[i][w].
pass
```

Replace with:

```python
if include_value > exclude_value:
    grid[i][w] = include_solution
else:
    grid[i][w] = exclude_solution
```

Use strict `>` so that ties favor the simpler "exclude" branch. Either choice works numerically, but this keeps the output deterministic and matches the autograder.

---

### Sanity check for Part 2

If you temporarily add `print(grid)` at the end of `knapsack()` and run the file, you should see a nested list where every inner element is either `[]` or a list of item names. No numbers. No `None`s. If you see `None`, a TODO is still `pass`ing.

---

## 8. Part 3 — Display the Grid (TODOs 6–9)

The grader checks specific substrings of your program's output, so **column widths matter**. Every column is exactly **12 characters wide**.

### TODO 6 — build the header row

Find:

```python
# TODO 6 — build the header row of capacity numbers (1..capacity),
# each right-aligned in cell_width characters.
header = ""
```

Replace the `header = ""` line — and leave the existing `print(" " * cell_width + header)` directly after untouched — with this:

```python
header = ""
for w in range(1, len(grid[0])):
    header += "{:>{width}}".format(str(w), width=cell_width)
```

**What's happening:** `"{:>{width}}".format("1", width=12)` produces `"           1"` — 11 spaces, then the digit, totalling 12 characters. The `>` means "right-align". We build the header column by column.

The `print(" " * cell_width + header)` line that's already there tacks 12 blank characters onto the front of the header — that's the invisible column above each row's item name.

---

### TODO 7 — start each row with the item name

Find (inside the `for i in range(1, n + 1):` loop):

```python
# TODO 7 — start each data row with the item name, LEFT-aligned in cell_width.
row = ""
```

Replace with:

```python
row = "{:<{width}}".format(items[i - 1][0], width=cell_width)
```

The `<` means **left-align** (name on the left, trailing spaces on the right). `items[i - 1][0]` is the name string — remember that `items[i - 1]` is a `(name, weight, value)` tuple and `[0]` grabs the name.

A 6-letter name like `"GUITAR"` becomes `"GUITAR      "` — 6 letters + 6 trailing spaces.

---

### TODO 8 — format non-empty cells

Find:

```python
if cell:
    # TODO 8 — format this non-empty cell as "$VALUE(LETTERS)",
    # right-aligned in cell_width.
    pass
```

Replace with:

```python
letters = "".join(name[0] for name in cell)
value = calculate_total_value(cell, items)
row += "{:>{width}}".format("${}({})".format(value, letters), width=cell_width)
```

**What each line does:**
- `letters = "".join(name[0] for name in cell)` — take the first character of each name in the cell and glue them into one string. For `["GUITAR", "LAPTOP"]` you get `"GL"`. For `["iPHONE"]` you get `"i"` (lowercase — see Section 11).
- `value = calculate_total_value(cell, items)` — re-use the Part 1 helper.
- The big `.format(...)` call first builds a string like `"$3500(GL)"`, then right-aligns it in 12 characters → `"   $3500(GL)"` (3 leading spaces + 9 chars).

---

### TODO 9 — empty cells

Find:

```python
else:
    # TODO 9 — append blank space so empty cells still take cell_width chars.
    pass
```

Replace with:

```python
row += " " * cell_width
```

Twelve spaces. The only reason we do this is so that every column lines up vertically in the printed table, even when a cell is empty.

---

## 9. Part 4 — Run the Program (TODOs 10–11)

### TODO 10 — call `knapsack`

Find:

```python
# TODO 10 — call knapsack(items, capacity) and store the result in `grid`.
grid = None
```

Replace with:

```python
grid = knapsack(items, capacity)
```

### TODO 11 — show the grid

Find:

```python
# TODO 11 — uncomment the line below to display the finished grid.
# display_grid(grid, items)
```

Remove the leading `# ` so it becomes:

```python
display_grid(grid, items)
```

Save the file. You're done coding.

---

## 10. Expected Output

Run:

```bash
python3 main.py
```

You should see **exactly** this (the spacing matters — every column is 12 characters wide):

```text
                       1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)
```

> If your columns don't line up, the problem is almost always a missing `{:>{width}}` format call. Re-read Part 3.

**The winning answer** is the bottom-right cell: **$35,500** from `GUITAR + LAPTOP + iPHONE + GOLD BAR` (weights 1+3+1+1 = 6 kg). That's the `(GLiG)` code.

---

## 11. Understanding the Letter Codes

Each cell shows a dollar total and a string of **first letters** of item names. The letters are concatenated in the order items were added to the list (which reflects the order the DP algorithm considered them, not alphabetical).

### Why is `i` lowercase for iPHONE?

Because the item's name in the data is literally `"iPHONE"` (with a lowercase `i` at the start). Python's `name[0]` returns whatever the first character is — no magic uppercasing. If you manually write `"I"`, the grader will reject your output.

### Why does the bottom-right show `GLiG` with two G's?

The two G's are two **different** items — the first is **G**UITAR, the second is **G**OLD BAR — because both names happen to start with G. That's a real source of confusion. To disambiguate visually, **you are allowed to use lowercase `g` for either Guitar or Gold Bar** (but not both). For example, these all pass the autograder:

- `$35500(GLiG)` — both G's uppercase (default)
- `$35500(gLiG)` — lowercase g = Guitar, uppercase G = Gold Bar
- `$35500(GLig)` — uppercase G = Guitar, lowercase g = Gold Bar
- Any other case combination of `GLiG`

The autograder matches case-insensitively on the letter codes, so you won't be penalized for your choice. You'd change this by editing line inside TODO 8:

```python
letters = "".join(name[0] for name in cell)
```

Into something like:

```python
letters = ""
for name in cell:
    if name == "GUITAR":
        letters += "g"
    else:
        letters += name[0]
```

This is **optional polish** — not required for credit.

---

## 12. Debugging Checklist

When something doesn't match the expected output, walk through these in order:

1. **Are you getting `None` in the grid?** A TODO is still `pass`ing or has `= None`. Re-check each one.
2. **Are the columns misaligned?** You forgot `"{:>{width}}"` or `"{:<{width}}"`. The autograder uses `grep` with the exact text — a single wrong space breaks it.
3. **Is your guitar row wrong?** Row 1 should be all `$1500(G)` six times. If not, TODO 2 or TODO 3 is wrong — likely you're not slice-copying (`[:]`).
4. **Are later rows mutating earlier ones?** Classic reference-aliasing bug. Every `grid[i-1][...]` read must be followed by `[:]` before you append to it.
5. **Does the full-capacity cell show `GLiG`?** If it shows something else (e.g., `GGLi` or `GSi`), your include-vs-exclude comparison is backward. Use strict `>`, not `>=`.
6. **Is iPHONE showing up as uppercase `I`?** You wrote a literal string somewhere instead of using `name[0]`. Let Python take the first character; don't type it yourself.
7. **Ran it, no output at all?** You left TODO 11 commented out. Remove the `# `.

---

## 13. Submission

1. Finish all **11 TODOs**.
2. Run `python3 main.py` and confirm the output matches Section 10 exactly.
3. Commit and push:

```bash
git add main.py
git commit -m "Complete knapsack DP assignment"
git push origin main
```

4. Open your repo on GitHub and watch the **Actions** tab. A workflow called **Autograding Tests** will run. All four tests must pass for full credit.

If a test fails, read its log in the Actions tab. The command it ran is shown at the top of each step — that's exactly the substring it was looking for in your output. Diff your output against that substring and the mismatch will usually jump out.

Good luck.
