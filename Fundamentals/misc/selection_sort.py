def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example list from the image
example_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
sorted_list = selection_sort(example_list)
print("Sorted list:", sorted_list)
