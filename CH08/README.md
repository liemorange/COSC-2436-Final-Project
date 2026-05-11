[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23439578&assignment_repo_type=AssignmentRepo)
# 2436 Lab 8 Balanced Trees

## Setup

```bash
# Clone this repository
git clone <your-repo-url>
cd <repo-name>
```

## Running the Code

```bash
python3 solution.py
```


## Testing

Tests are automatically run via GitHub Actions on every push.

To run tests locally:
```bash
# See .github/workflows/classroom.yml for test commands
```
## Autograding

This assignment uses GitHub Classroom autograding. Your score is calculated based on:
- Code compilation (if applicable)
- Test results
- Code quality

See `.github/classroom/autograding.json` for the full grading rubric.


## Lab Report

### Student Information
- **Name:** Donghyun Lee
- **Date:** 4/62026

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** -1, 0, 1
- **Why rebalance?** To keep height shorter so the operation time stays fast O(log n)
- **Time Complexity (all operations):** O(log n)

#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   | left child is left heavy  | single right rotation |
| RR   | right child is right heavy | single left rotation |
| LR   | left child is right heavy  | left rotate child, then right rotate root |
| RL   | right child is left heavy  | right rotate child, then left rotate root |

Reflection Questions
1. Why is an unbalanced BST bad?
 Because height can degrade to O(n), making every operation as slow as a linear scan.
2. How do rotations maintain the BST property?
 Rotations only rewire pointers between nodes without changing the left-smaller right-larger ordering, so the BST property is preserved.
3. What other self-balancing trees exist?
 Red-Black trees, Splay trees, B-trees.
