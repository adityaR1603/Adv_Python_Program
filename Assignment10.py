import numpy as np

arr = np.arange(1, 11)
print("Original array:", arr)

print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5
print("After adding 5:", arr)

arr = arr * 2
print("After multiplying by 2:", arr)
