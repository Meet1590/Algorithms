# Binary search algo

"""
Docstring for binary_search

Inputs: 
    list / collection / iterable
    element which we are looking for
Outputs: 
    index of the element

Operations:
    sort the collection
    compare the element with median element
    if element = median:
        return = index of median
    if element > median:
        collection = collection[median index:last index]
    else:
        collection = collection[first index:median index]

Solution:
2 pointer

"""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
element = 84

def sort_collection(primes:list) -> list:
    return sorted(primes) # sorted() - accpets any iterables and returns a sorted list
# primes.sort() -> Sorts in place and returns none

def binary_search(sorted_primes:list, element:int):
    left = 0
    right = len(sorted_primes)-1
    
    while left <= right:
        median = (left+right)//2
        if sorted_primes[median]==element:
            return median
        if sorted_primes[median]>element:
            right = median-1
        else:
            left = median+1
    return -1

def main(primes:list, element:int):
    sorted_primes = sort_collection(primes)
    index_found = binary_search(sorted_primes, element)
    if index_found != -1:
        print(f"element found on index {index_found}")
        print(sorted_primes[index_found])
    if index_found == -1:
        print("element not found!")

if __name__ == "__main__":
    main(primes, element)