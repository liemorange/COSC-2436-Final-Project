# Lab Report Template (create and insert into a new file named: LAB_REPORT.md)

## Student Information
**Name:** Donghyun Lee
**Date:** 05/10/26  
**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---

# Algorithm Understanding

**What type of problem is this algorithm solving?**  
[Your answer — optimization / approximation / packing problem]
Optimization as it asks the best solution on the given conditions.
**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
[Your explanation]
Not always as it just picks the biggest box each time which seems smart but sometimes a different combination of smaller boxes would actually fit more total volume

**What is the greedy choice made in this algorithm?**  
[Your answer]
Picking the biggest box that still fits.
---

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
[Your explanation]
So we fill the truck with the big stuff first and use the leftover space for smaller boxes rather than the other way around
**What would happen if we sorted the boxes in ascending order instead?**  
[Your explanation]
You'd pack a bunch of small boxes first and then the big ones might not fit even though they would've if you loaded them first.
**Why do we keep track of `used_volume`?**  
[Your explanation]
To know how much space is left so we do not accidentally overload the truck.
---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
[Your explanation]
A box could be 1x1x100 and technically "fit" by volume but won't actually go in if the truck is only 50 units tall.
**Give an example where a box fits by volume but not by dimensions.**  
[Your example]
Where volume is okay but it's too long to fit inside.
**How would you modify the algorithm to check dimension constraints before packing a box?**  
[Your explanation]
Before adding a box, check length, width, and height are all less than or equal to the truck's inner dimensions not just that the volumes add up.
---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
[Your explanation]
A back has 10 units left and you have boxes of size 6, 5, and 5. Greedy picks 6 and stops but obviously 5+5 is better.
**How is this problem related to the Knapsack Problem?**  
[Your explanation]
You have a capacity limit and a bunch of items and you're trying to maximize what you pack in. The knapsack problem just usually has values attached too.
**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
[Your explanation]
Dynamic programming would find the actual optimal solution but way slower, you'd be checking every possible combination which gets expensive for real.
**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
[Your explanation]
You track both used volume and used weight, and check that neither goes over the limit before adding a box. Sorting gets trickier too since the biggest box isn't always the lightest.

**Why are greedy algorithms often preferred despite not always being optimal?**  
[Your explanation]
They're fast and simple as for most real situations "good enough" is fine and nobody wants to wait forever for the perfect answer.