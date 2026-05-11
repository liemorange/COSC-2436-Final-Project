# Chapter 7: Binary Trees

## Overview
In this assignment, you will implement a binary tree in Python, focusing on the fundamental operations such as insertion, inorder traversal, and search. Understanding binary trees is crucial as they form the basis for many complex data structures and algorithms, including those used in databases and compression algorithms like Huffman coding.

## Learning Objectives
- Understand the structure and properties of binary trees
- Implement basic operations on binary trees
- Practice recursive algorithms for tree traversal
- Develop problem-solving skills using tree data structures

## Requirements
1. Implement the `insert` method to add elements to the binary tree.
2. Implement the `inorder_traversal` method to return elements in sorted order.
3. Implement the `search` method to find elements in the binary tree.

## Getting Started
You will find the starter code in `solution.py`. This file contains the skeleton of a `BinaryTree` class and a `Node` class. Begin by reviewing the structure of these classes. You can run the code using the provided test cases to see how the tree operations should work.

## Implementation Steps

### Implement the `insert` Method
- **Task**: Add a new integer to the binary tree.
- **Explanation**: If the tree is empty, the new data becomes the root. Otherwise, recursively find the correct position in the tree and insert the new node as a leaf.
- **Example**: Inserting `5` into a tree with root `7` and left child `3` results in `3` having a right child `5`.
- **Code**:
  ```python
  def insert(self, data: int) -> None:
      new_node = Node(data)
      if self.root is None:
          self.root = new_node
      else:
          self._insert_recursive(self.root, new_node)

  def _insert_recursive(self, current: Node, new_node: Node) -> None:
      if new_node.data < current.data:
          if current.left is None:
              current.left = new_node
          else:
              self._insert_recursive(current.left, new_node)
      else:
          if current.right is None:
              current.right = new_node
          else:
              self._insert_recursive(current.right, new_node)
  ```

### Implement the `inorder_traversal` Method
- **Task**: Traverse the tree in inorder and collect elements in a list.
- **Explanation**: Inorder traversal visits nodes in the left subtree, then the root, and finally the right subtree, resulting in sorted order.
- **Example**: For a tree with nodes `7`, `3`, `9`, the inorder traversal returns `[3, 7, 9]`.
- **Code**:
  ```python
  def inorder_traversal(self) -> List[int]:
      result = []
      self._inorder_recursive(self.root, result)
      return result

  def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
      if node is not None:
          self._inorder_recursive(node.left, result)
          result.append(node.data)
          self._inorder_recursive(node.right, result)
  ```

### Implement the `search` Method
- **Task**: Determine if a given integer is present in the binary tree.
- **Explanation**: Start at the root and compare the target value with the current node, deciding to search left or right based on the comparison.
- **Example**: Searching for `5` in a tree with nodes `7`, `3`, `9` returns `False`.
- **Code**:
  ```python
  def search(self, data: int) -> bool:
      return self._search_recursive(self.root, data)

  def _search_recursive(self, node: Optional[Node], data: int) -> bool:
      if node is None:
          return False
      if node.data == data:
          return True
      elif data < node.data:
          return self._search_recursive(node.left, data)
      else:
          return self._search_recursive(node.right, data)
  ```

## Testing
To test your implementation, run the provided test cases in the `main` section of `solution.py`. Ensure that the output matches the expected results. You can also add additional test cases to further validate your implementation.

## Grading Rubric
- Test search for existing element: 25 pts
- Test search for non-existing element: 25 pts
- Test insertion and inorder traversal with different data: 25 pts
- Test search in empty tree: 25 pts

## Tips and Hints
- Remember that binary trees are recursive structures, so recursive methods are often the simplest way to implement tree operations.
- Pay attention to edge cases, such as inserting into an empty tree or searching for a non-existent element.
- Use the inorder traversal to verify that your tree maintains the binary search tree property.
- Practice visualizing the tree structure to better understand how your code manipulates the tree.

## Lab Report

### Student Information
- **Name:** Donghyun Lee
- **Date:** 3/29/2026

### Algorithm Analysis

#### Binary Search Tree
- **Search Time (balanced):** O(log n)
- **Search Time (unbalanced):** O(n)
- **BST Property:** A binary search tree maintains the property that for each node, all elements in the left subtree are less, and all elements in the right subtree are greater.

#### Traversals
| Traversal | Order | Use Case |
|-----------|-------|----------|
| Preorder  | Root, Left, Right | Copying a tree |
| Inorder   | Left, Root, Right | Getting sorted elements |
| Postorder | Left, Right, Root | Deleting a tree |

### Reflection Questions

1. Why does inorder traversal give sorted output?
   - Inorder traversal visits nodes in ascending order for a binary search tree, as it processes the left subtree, then the node, and finally the right subtree.

2. When would a BST become unbalanced?
   - A BST becomes unbalanced when nodes are inserted in a sorted order, leading to a linear structure similar to a linked list.

3. What's the difference between BFS and DFS for trees?
   - BFS explores nodes level by level using a queue, while DFS explores as deep as possible along each branch before backtracking, typically using recursion or a stack.