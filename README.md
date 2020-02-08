# Sorting Algorithm
## Description
Bubble sort, insertion sort, shell sort, merge sort, and selection sort implemented in Python
## Content
* bubble_sort.py
    * bubbleSort(nums_list) : returned sorted version of nums_list using bubble sort
    * shortBubbleSort(nums_list) : bubble sort but with detection to see if exchanges were made in order to stop early
* insertion_sort.py
    * insertionSort(nums_list) : simple insertion sort, return sorted version of nums_list
    * gapInsertionSort(nums_list,start_i,gap) : insertion sort with gap
    * shellSort(nums_list,gap) : shellSort with user input gap, second pass is insertionSort (gap=1)
    * havlenShellSort(nums_list) : shellSort that automatically detect the length of nums_list and make gape be half of it
* merge_sort.py
    * mergeSort(nums_list) : merge sort, recursion
* selection_sort.py
    * selectionSort(nums_list) : selection sort

## Usage
Use A as test:
```python
A= [1,9,2,5,3,6,7,4,8,2]
```
* bubble_sort
```python
# testing the two bubble sort algorithm
print(bubbleSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(shortBubbleSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```
* insertion_sort
```python
A= [1,9,2,5,3,6,7,4,8,2]
print(insertionSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```
* merge_sort
```python
print(mergeSort(A)) #[1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```
* selection_sort
```python
print(selectionSort(A)) # [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```