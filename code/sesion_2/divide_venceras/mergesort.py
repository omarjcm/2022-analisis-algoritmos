import numpy as np

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        pivote = len(arr)//2
  
        # Dividing the array elements
        L = arr[:pivote]
        # into 2 halves
        R = arr[pivote:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)

        merge(arr, L, R)
  
def merge(arr, L, R):

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


