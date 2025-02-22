my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def bubble_sort(my_array):
    
    # compare each element with next element
    n = len(my_array)

    while(n>0):

        swap = False
        # compare each element with next element by managing 2 pointers
        #def compare_and_track_iterations(n, swap):
        for i in range(n-1):
            
            j = i+1
            if my_array[i]>my_array[j]:
                temp = my_array[i]
                my_array[i] = my_array[j]
                my_array[j] = temp
                swap = True
            

            # Increment left pointer by 1 so 2nd pointer will automatically increase
            i = i+1

        # Decreament number of times algorithm needs to run worst case (n-1 times)
        n = n-1

        # Best case and Average case handler
        if swap == False:
            
            # Handles best case
            if len(my_array)-1== n:
                print("Array is already sorted")
                break

            # Handles average case and return number of operations it took to sort the array
            else:
                print("Array is sorted in ", len(my_array)-n-1, "iterations.")
                print(my_array)
                break
            

if __name__ == "__main__":
    bubble_sort(my_array)