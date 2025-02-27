'''
Algorithm and other details for selection sort

Algorithm:
    1> Find smallest element from unsorted array and swap it with first element, repeated in each iteration

'''
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
def selection_sort(arr: my_array):
    
    # Finding minimum from the array
    for i in range(len(arr)):
        min_index = i
        n = 1
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                temp = arr[min_index]
                arr[min_index] = arr[j]
                arr[j] = temp
                swap = True
                n += 1
    print(arr)

if __name__ == "__main__":
    selection_sort(my_array)