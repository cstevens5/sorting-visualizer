# sorting-visualizer

A simple visualizer for the bubble, insertion, and selection sorting algorithms

## Overview

This project is a visualization of some basic sorting algorithms written in python. Vertical gray bars are used to represent the elements that are being sorted. Each bar starts at the bottom of the screen and extends upwards to an arbitrary height. The height of each bar represents it's value when being sorted. The GUI for this project was set up using the python library pygame. When the program is run, instructions on how to perform desired actions are displayed near the top of the screen. Currently the project just implements three sorting algorithms, but more sorting algorithms will likely be added in the future.

## Bubble Sort

Bubble sort is a sorting algorithm that works by comparing adjacent elements in the list that being sorted. If the elements are out of order with respect to each other, then they are swapped. Bubble sort is a stable and in place sorting algorithm.

Time Complexity:
Best Case - $O(n)$

Average Case - $O(n^2)$

Worst Case - $O(n^2)$

where n represents the size of the list being sorted

Space Complexity:
$O(1)$

## Insertion Sort

Insertion sort is a comparison based sorting algorithm that sorts the array one element at a time. The sorted array is built by comparing array elements and placing one element in it's sorted position for each iteration. Insertion sort is a stable and an in place algorithm.

Time Complexity:

Best Case - $O(n)$

Average Case - $O(n^2)$

Worst Case - $O(n^2)$

Space Complexity:
$O(1)$

## Selection Sort

Selection sort is a comparison based sorting algorithm. The algorithm starts by finding the minimum/maximum element in the array and swapping it with the first element. The same process is then repeated with the second, third, fourth, etc. elements until the array is finally sorted. Selection sort is a stable and in place sorting algorithm.

Time Complexity:

Best Case - $O(n^2)$

Average Case - $O(n^2)$

Worst Case - $O(n^2)$

Space Complexity:
$O(1)$

## Installation

First you should copy the github repository by entering the following command in the terminal or command prompt:

```
git clone https://github.com/cstevens5/sorting-visualizer.git
```

Once you have cloned the repository, type the following command in the correct directory to run the program:

```
python3 main.py
```
