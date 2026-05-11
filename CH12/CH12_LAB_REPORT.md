# Chapter 12: Regression (Intro to Machine Learning) — Lab Report

## Student Information
- **Name:** Donghyun Lee
- **Date:** 05/10/2026
- **Course:** COSC 2436
## Algorithm Summary
- **How it works:** Linear regression fits a straight line through your data to predict a continuous output. You are trying to find the the predictions as close to the actual values as possible. That's done by minimizing predictions. You can solve by finding it iteratively with gradient descent. 

- **Time complexity:** Normal equation is O(n·d^2) because of the matrix inversion. Gradient descent is O(n·d) per iteration.

- **When to use it:** When your data has a roughly linear relationship like forecasting, temperature prediction,etc. Also commonly used as a starting baseline before trying anything fancier.

## Test Results

Bakery Data:
    weather  weekend_holiday  game_on  loaves
0         3                0        0      42
1         5                1        1      95
2         2                0        0      30
3         4                1        0      72
4         1                0        1      38
5         5                0        0      55
6         3                1        1      78
7         4                0        0      50
8         2                1        0      58
9         5                1        0      85
10        1                0        0      22
11        3                0        1      52
12        4                1        1      88
13        2                0        1      44
14        5                0        1      70
15        3                1        0      65
16        4                0        1      62
17        1                1        0      48
18        2                1        1      70
19        4                1        0      75

Features shape: (20, 3)
Target shape: (20,)

KNN model trained with k=4

Today's conditions: Weather=4, Weekend/Holiday=1, Game=0
Predicted loaves to bake: 70.5

## Reflection Questions

What does R^2 mean and what it actually tels you?
It is 0 and 1 scale predictions on how much I am spot on and it tells you how well your model fits into the data.

How does gradient descent actually work?
It keeps nudging the parameters little by little in whichever direction makes the error smaller, too big and it overshoots and never settles, too small and it takes forever to get anywhere. You just keep doing that until it stops improving .

How does this connect to everything else we learned?
It's still just finding the best solution in the end, finding the best parameters to minimize error. It isn't that different from finding the shortest path or the most valuable items to pack,etc. 

## Challenges Encountered
The algorighm code was way too complicated and the imports such as pandas and numpy were not understood right away. For example on this solution "today_features = np.array([[weather, weekend_holiday, game_on]])", you were putting input variables in a format that exactly matches the 2D array. But honestly I was not sure what the specific variables mean without seeing the solution code.
