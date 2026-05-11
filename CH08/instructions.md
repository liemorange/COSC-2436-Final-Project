## Overview
In this assignment, you will implement an AVL Tree, a type of self-balancing binary search tree. AVL Trees maintain their balance through rotations, ensuring that operations such as insertion, deletion, and lookup remain efficient with a time complexity of O(log n). Understanding and implementing AVL Trees is crucial for optimizing data structures that require frequent updates and lookups.

## Learning Objectives
- Understand why balanced trees matter
- Implement AVL tree rotations
- Maintain O(log n) operations

## Requirements
1. Implement the `height` method to return the height of a node.
2. Implement the `balance_factor` method to calculate the balance factor of a node.
3. Implement the `rotate_right` method to perform a right rotation on a subtree.
4. Implement the `rotate_left` method to perform a left rotation on a subtree.
5. Implement the `_insert` method to insert a value into the AVL Tree and rebalance it if necessary.

## Getting Started
The starter code is provided in `avl_tree.py`. Begin by reviewing the `AVLNode` and `AVLTree` classes. The `AVLTree` class contains several methods marked with `TODO` comments where you will implement the required functionality. You can run the code using the Run button in your IDE to test your implementation.

## Implementation Steps
### Implement the `height` Method
- **TODO:** Implement the `height` method to return the height of a given node. If the node is `None`, return 0.
- **Explanation:** The height of a node is crucial for calculating the balance factor and determining if rotations are needed.
- **Example:**
  ```python
  node = AVLNode(10)
  print(tree.height(node))  # Output: 1
  print(tree.height(None))  # Output: 0
  ```

### Implement the `balance_factor` Method
- **TODO:** Implement the `balance_factor` method to calculate the balance factor of a node as the difference between the heights of its left and right children.
- **Explanation:** The balance factor helps determine if a node is balanced or if rotations are required.
- **Example:**
  ```python
  node = AVLNode(10)
  node.left = AVLNode(5)
  print(tree.balance_factor(node))  # Output: 1
  ```

### Implement the `rotate_right` Method
- **TODO:** Implement the `rotate_right` method to perform a right rotation on a subtree rooted at a given node.
- **Explanation:** Right rotation is used to rebalance a left-heavy subtree.
- **Example:**
  ```python
  # Before rotation:
  #     y
  #    /
  #   x
  #  /
  # A
  # After rotation:
  #   x
  #  / \
  # A   y
  ```

### Implement the `rotate_left` Method
- **TODO:** Implement the `rotate_left` method to perform a left rotation on a subtree rooted at a given node.
- **Explanation:** Left rotation is used to rebalance a right-heavy subtree.
- **Example:**
  ```python
  # Before rotation:
  # x
  #  \
  #   y
  #    \
  #     C
  # After rotation:
  #   y
  #  / \
  # x   C
  ```

### Implement the `_insert` Method
- **TODO:** Implement the `_insert` method to insert a value into the AVL Tree and rebalance it if necessary.
- **Explanation:** This method should perform a standard BST insert, update the node heights, calculate the balance factor, and perform rotations if needed.
- **Example:**
  ```python
  tree.insert(10)
  tree.insert(20)
  tree.insert(5)
  print(tree.inorder())  # Output: [5, 10, 20]
  ```

## Complete Program
```python
from typing import Optional, Any, List

class AVLNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y
    
    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(4)
    tree.insert(15)
    print("Inorder traversal of the AVL tree:", tree.inorder())
```

## Testing
To test your implementation, use the provided test cases in the starter code. Run the code to ensure all tests pass. The output should match the expected results if your implementation is correct.

## Grading Rubric
- Test AVL Tree Insertion and Balancing: 20 pts
- Test AVL Tree Left Rotation: 20 pts
- Test AVL Tree Right Rotation: 20 pts
- Test AVL Tree Left-Right Rotation: 20 pts
- Test AVL Tree Right-Left Rotation: 20 pts

## Tips and Hints
- Remember that the height of a `None` node is 0.
- Carefully update the height of nodes after performing rotations.
- Ensure that the balance factor is calculated correctly to determine when to perform rotations.
- Test your tree with various sequences of insertions to ensure it remains balanced.
- Review the rotation diagrams to understand how rotations affect the tree structure.

# Complete The Lab Report in README.md
## Lab Report

### Student Information
- **Name:** Donghyun Lee
- **Date:** 05/10/26

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** [Your answer] -1,0,1
- **Why rebalance?** [Your explanation] Because it would be better to use a linked list if it is too onesided.
- **Time Complexity (all operations):** O(?) O(log n) as it divide by 2 each time AVL

#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   |      left heavry on the left     | Single right rotation   |
| RR   |      right child heavy on the right     |  Single left rotation  |
| LR   |      left child is heavy on the right     |   Left rotate child, then right rotate root  |
| RL   |      right child is heavy on the left     |   Right rotate child, then left rotate root  |

### Reflection Questions

1. Why is an unbalanced BST bad?
Because it takes O(n) and loses its point to being able to partition half by half.
2. How do rotations maintain the BST property?
Rotations keep BST balanced and keeps the time O(log n) by having both larger and smaller parts organized.
3. What other self-balancing trees exist?
Red BLack trees, B-trees, Splay trees, etc.
