## Overview
In this assignment, you will implement a program to help pack a truck efficiently using a greedy algorithm. You will learn to calculate the volume of boxes and determine how to fit them into a truck based on volume constraints. This exercise will enhance your understanding of greedy strategies and approximation algorithms, which are useful for solving NP-hard problems.

## Learning Objectives
- Understand and implement a greedy algorithm
- Calculate the volume of 3D objects
- Apply approximation algorithms to solve packing problems
- Handle user input and output in a Python program

## Requirements
1. Implement the `volume` method in the `Box` class to calculate the volume of a box.
2. Implement the `pack_truck` function to use a greedy strategy for packing boxes into a truck based on their volumes.
3. Extend the program to check if individual box dimensions fit within the truck dimensions, in addition to volume constraints.

## Getting Started
You will begin with the provided starter code in `solution.py`. The code includes a `Box` class and a `pack_truck` function with TODO comments indicating where you need to add your implementation. Start by understanding the class and function definitions, then proceed to implement the missing parts as described in the TODO comments.

## Implementation Steps
### Box Volume Calculation
- **TODO**: Implement the `volume` method in the `Box` class.
  - **Task**: Calculate the volume by multiplying the length, width, and height of the box.
  - **Why**: This is necessary to determine how much space each box will occupy in the truck.
  - **Example**: For a box with dimensions 2x3x4, the volume is `2 * 3 * 4 = 24`.
  - **Code**:
    ```python
    def volume(self) -> float:
        return self.length * self.width * self.height
    ```

### Greedy Packing Strategy
- **TODO**: Implement the `pack_truck` function.
  - **Task**: Sort the boxes by volume in descending order, then add them to the truck until the volume limit is reached.
  - **Why**: This strategy helps maximize the number of boxes packed by prioritizing larger boxes first.
  - **Example**: Given boxes with volumes [10, 20, 30] and a truck volume of 50, the function should pack boxes with volumes 30 and 20.
  - **Code**:
    ```python
    def pack_truck(boxes: list, truck_volume: float) -> list:
        boxes.sort(key=lambda box: box.volume(), reverse=True)
        packed_boxes = []
        used_volume = 0
        for box in boxes:
            if used_volume + box.volume() <= truck_volume:
                packed_boxes.append(box)
                used_volume += box.volume()
        return packed_boxes
    ```

### Input and Calculate Truck Volume
- **TODO**: Prompt the user to enter the truck's dimensions and calculate its volume.
  - **Task**: Gather input for length, width, and height, then calculate the volume.
  - **Why**: Knowing the truck's volume is essential for determining how many boxes can fit.
  - **Code**:
    ```python
    truck_length = float(input("Enter truck length: "))
    truck_width = float(input("Enter truck width: "))
    truck_height = float(input("Enter truck height: "))
    truck_volume = truck_length * truck_width * truck_height
    print(f"Truck volume: {truck_volume}")
    ```

### Input Boxes
- **TODO**: Allow the user to input box details and create `Box` objects.
  - **Task**: Continuously prompt for box dimensions until the user types 'done'.
  - **Why**: This allows dynamic input of box data for testing different scenarios.
  - **Code**:
    ```python
    while True:
        label = input("Enter box label (or 'done' to finish): ")
        if label.lower() == 'done':
            break
        length = float(input("Enter box length: "))
        width = float(input("Enter box width: "))
        height = float(input("Enter box height: "))
        box = Box(label, length, width, height)
        boxes.append(box)
    ```

### Pack the Truck and Display Results
- **TODO**: Use the `pack_truck` function to determine which boxes to pack and display the results.
  - **Task**: Call the function with the list of boxes and truck volume, then print the packed boxes.
  - **Why**: This provides the final output of the program, showing the user which boxes fit.
  - **Code**:
    ```python
    packed_boxes = pack_truck(boxes, truck_volume)
    print("Packed boxes:")
    for box in packed_boxes:
        print(f"{box.label} with volume {box.volume()}")
    ```

## Complete Program
```python
class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float) -> list:
    boxes.sort(key=lambda box: box.volume(), reverse=True)
    packed_boxes = []
    used_volume = 0
    for box in boxes:
        if used_volume + box.volume() <= truck_volume:
            packed_boxes.append(box)
            used_volume += box.volume()
    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    truck_length = float(input("Enter truck length: "))
    truck_width = float(input("Enter truck width: "))
    truck_height = float(input("Enter truck height: "))
    truck_volume = truck_length * truck_width * truck_height
    print(f"Truck volume: {truck_volume}")

    boxes = []  # List to store box objects

    while True:
        label = input("Enter box label (or 'done' to finish): ")
        if label.lower() == 'done':
            break
        length = float(input("Enter box length: "))
        width = float(input("Enter box width: "))
        height = float(input("Enter box height: "))
        box = Box(label, length, width, height)
        boxes.append(box)

    packed_boxes = pack_truck(boxes, truck_volume)
    print("Packed boxes:")
    for box in packed_boxes:
        print(f"{box.label} with volume {box.volume()}")

    print("\nThank you for using the Truck Cargo Calculator.")
```

## Testing
To test your implementation, use the Run button in the web IDE. Enter various box and truck dimensions to see how the program packs the boxes. Ensure that the output matches the expected behavior described in the requirements.

## Grading Rubric
- Compilation and Syntax Check: 10 pts
- Functional Test - Single Box Fits: 45 pts
- Functional Test - Multiple Boxes Fit: 45 pts

## Tips and Hints
- Remember to check that the volume calculation in the `volume` method is correct.
- Ensure that the sorting in `pack_truck` is in descending order to follow the greedy strategy.
- Test edge cases, such as when no boxes fit or when all boxes fit perfectly.
- Use print statements to debug and verify that each step of your algorithm is working as expected.
- Be mindful of user input and handle unexpected input gracefully.

# Lab Report Template (create and insert into a new file named: LAB_REPORT.md)

## Student Information
**Name:** [Your Name]  
**Date:** [Date]  
**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---

# Algorithm Understanding

**What type of problem is this algorithm solving?**  
[Your answer — optimization / approximation / packing problem]

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
[Your explanation]

**What is the greedy choice made in this algorithm?**  
[Your answer]

---

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
[Your explanation]

**What would happen if we sorted the boxes in ascending order instead?**  
[Your explanation]

**Why do we keep track of `used_volume`?**  
[Your explanation]

---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
[Your explanation]

**Give an example where a box fits by volume but not by dimensions.**  
[Your example]

**How would you modify the algorithm to check dimension constraints before packing a box?**  
[Your explanation]

---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
[Your explanation]

**How is this problem related to the Knapsack Problem?**  
[Your explanation]

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
[Your explanation]

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
[Your explanation]

**Why are greedy algorithms often preferred despite not always being optimal?**  
[Your explanation]
