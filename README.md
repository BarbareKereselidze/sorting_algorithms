# Sorting Algorithms Visualizer

This Python project provides a simple command-line tool to visualize and compare various sorting algorithms. The implemented sorting algorithms include Bubble Sort, Insertion Sort, and Quick Sort. 
The code structure incorporates a decorator pattern to output sorting results, algorithm runtime and provides flexibility for adding more sorting algorithms in the future.

## Features:

* **Bubble Sort:** <br>
A basic sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

* **Insertion Sort:** <br>
This algorithm builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

* **Quick Sort:** <br>
A divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.

## Structure:

1. **sorting_algorithms.py:** <br>
Defines the sorting algorithms with a decorator for outputting results. 
2. **input_processing.py:** <br>
Contains functions for getting user input - list of numbers and choice of algorithm. 
3. **main.py:** <br>
The main script that ties everything together. It uses Click library for command-line interface.
4. **requirements.txt:** <br>
has all the requirements for the project

## How to Use:

1. Run the script. 
2. Enter a list of numbers separated by commas when prompted.
3. Choose a sorting algorithm from the provided options.
4. View the original list and the sorted result.

#### Feel free to use, modify, and expand upon this project with different sorting algorithms.