def insertionSort(A):
    for j in range(1, len(A)):  
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:  
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

if __name__ == "__main__":
    A = [2, 4, 1, 6, 33, 7, 3, 10, 39]
    insertionSort(A)
    print(A)