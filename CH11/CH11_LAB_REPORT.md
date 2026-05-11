# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** Donghyun Lee
- **Date:** 05/10/26
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** DP breaks a big problem into smaller subproblems, solves each one once, and saves the answer so you don't redo the same work. There are two ways to do it — top-down which is just recursion with caching, and bottom-up which builds up a table starting from the smallest cases.
- **Time complexity:**  Depends on the problem. Knapsack is O(n·W) and LCS is O(m·n)
- **When to use it:** When greedy isnt enough and you need the actual optimal answer — coin change, knapsack, edit distance, that kind of thing.

## Test Results

                       1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)

## Reflection Questions

Why do subproblems matter?
Same subproblems keep coming up over and over in plain recursion so you end up recomputing the same thing a ton of times. DP just saves the answer the first time and looks it up after that. Fibonacci is the classic example — without caching it's O(2^n) which blows upfast.

Memoization vs Tables(tabulation)?
Memoization is just recursion but you cache results as you go, so you only solve what you actually need. Tabulation fills in a table from the bottom up solving everything in order. Memoization is usually easier to write, tabulation avoids stack overflow issues and tends to run a bit faster in practice.

When does greedy fails the hardest on?
It always grabs the biggest items first which works fine for normally but like having one gigantic item that only fills a little more than half and disposes all other items because it is locked itself with that working first pick, it misses every better answers with different combinations.
## Challenges Encountered
The concept is itself was undeerstandable somehow however I had hard time working with the tables and figuring out which ones to fill in adding up. 