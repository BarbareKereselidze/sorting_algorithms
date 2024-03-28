# Sorting Algorithm Implementation

This Python project provides a simple command-line tool to compare various sorting algorithms and their runtimes. 
The code structure incorporates a decorator pattern to output sorting results and calculate
algorithm runtime, it also provides flexibility for adding more sorting algorithms in the future. <br>
**Current implemented sorting algorithms include: Bubble Sort, Insertion Sort, Quick Sort, Selection Sort, Merge Sort** <br>

## Included Sorting Algorithms:

* **Bubble Sort:** <br>
A basic sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. <br>
  * Time Complexity: O(n^2)
  * Space Complexity: O(1)


* **Insertion Sort:** <br>
This algorithm builds the final sorted array one item at a time. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, 
heapsort, or merge sort.  <br>
  * Time Complexity: O(n^2)
  * Space Complexity: O(1)


* **Quick Sort:** <br>
A divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the 
other elements into two sub-arrays according to whether they are less than or greater than the pivot. <br>
  * Time Complexity: O(n log n)
  * Space Complexity: O(n)


* **Selection Sort:** <br>
Selection Sort sorts an array by repeatedly finding the minimum element from the unsorted part and 
swapping it with the first unsorted element. <br>
  * Time Complexity: O(n^2)
  * Space Complexity: O(1)


* **Merge Sort:** <br>
Merge Sort is a divide-and-conquer algorithm that divides the array into smaller sub-arrays, 
sorts them, and then merges them back together. <br>
  * Time Complexity: O(n log n)
  * Space Complexity: O(n)

## How to Run:
1. Install necessary dependencies using:
```commandline
pip install -r requirements.txt
```
2. Go to the project directory in terminal.
3. Run the script as is for the runtime to be displayed. If you don't want to display runtime, run:
```commandline
 python3 main.py -t
```
4. Enter a list of numbers separated by commas when prompted and 
choose a sorting algorithm from the provided options. The output should look like this:

```commandline
Enter a list of numbers separated by commas: 6, 19, -7, 9.7, 5, 134, 12, -13, -8.9, -5.1, 6.8

Your list: [6.0, 19.0, -7.0, 9.7, 5.0, 134.0, 12.0, -13.0, -8.9, -5.1, 6.8]

Choose which algorithm you want to use:
1. bubble sort algorithm
2. insertion sort algorithm
3. quick sort algorithm
4. selection sort algorithm
5. merge sort algorithm

Input choice: 3
You chose: quick sort algorithm

Sorted numbers: [-13.0, -8.9, -7.0, -5.1, 5.0, 6.0, 6.8, 9.7, 12.0, 19.0, 134.0]
function took 0.000022 seconds to execute.
```
