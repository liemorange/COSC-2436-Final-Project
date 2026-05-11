"""
Lab 2: Simple Linked List Implementation
Demonstrates linked list concepts from Chapter 2.
"""
from typing import Any, Optional


class Node:
    """A node in the linked list."""
    
    def __init__(self, data: Any):
        # TODO: Initialize data and next attributes
        # self.data = data
        self.data = data
        # self.next = None
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    Simple singly linked list.
    
    Insert: O(1) at head, O(n) at tail
    Delete: O(1) at head, O(n) elsewhere
    Search: O(n)
    Access by index: O(n)
    """
    
    def __init__(self):
        # TODO: Initialize head and size
        # self.head = None
        self.head = None
        # self.size = 0
        self.size = 0
    
    def insert_at_head(self, data: Any) -> None:
        """Insert at beginning - O(1)"""
        # TODO: Implement insert_at_head
        # 1. Create new_node = Node(data)
        new_node = Node(data)
        # 2. Set new_node.next = self.head
        new_node.next = self.head
        # 3. Set self.head = new_node
        self.head = new_node
        # 4. Increment self.size
        self.size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert at end - O(n)"""
        # TODO: Implement insert_at_tail
        # 1. Create new_node = Node(data)
        new_node = Node(data)
        # 2. If self.head is None, set self.head = new_node
        if self.head is None:
            self.head = new_node
        # 3. Else traverse to end and set current.next = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        # 4. Increment self.size
        self.size += 1
    
    def delete_at_head(self) -> Optional[Any]:
        """Delete from beginning - O(1)"""
        # TODO: Implement delete_at_head
        # 1. If self.head is None, return None
        if self.head is None:
            return None
        # 2. Save data = self.head.data
        data = self.head.data
        # 3. Set self.head = self.head.next
        self.head = self.head.next
        # 4. Decrement self.size
        self.size -= 1
        # 5. Return data
        return data
    
    def search(self, target: Any, key=lambda x: x) -> Optional[Node]:
        """Search for element - O(n)"""
        # TODO: Implement search
        # 1. Set current = self.head, comparisons = 0
        current = self.head
        comparisons = 0
        # 2. While current is not None:
        while current != None:
        #    a. Increment comparisons
            comparisons += 1
        #    b. If key(current.data) == target, print and return current
            if key(current.data) == target:
                print(key)
                return current
        #    c. Set current = current.next
            current = current.next
        # 3. Print not found message and return None
        print(f"Not Found")
        return None
    
    def to_list(self) -> list:
        """Convert to Python list for display."""
        # 1. Create empty result list
        result = []
        # 2. Traverse linked list, appending each data to result
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        # 3. Return result
        return result
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"
