Say we have an unsorted list with $n$ elements

The steps of merge sort are:

1. Divide: recursively split the list into half until there is only $n$ one elements lists.
2. Conquer
    - Merge: we merge the lists together
    - Sort: When we sort via merging, we don't use insertion sort. We just compare the values at a certain index and then merge them. E.g. Merging List A: `[2, 7]` and List B: `[3, 8]`:
        1. Compare the first elements: Is A`[0]` (2) smaller than B`[0]`? Yes. Move 2 to the result list. Move Pointer A forward.
            - Result: `[2]`
        2. Compare again: Is A`[1]` (7) smaller than B`[0]` (3)? No. Move 3 to the result list. Move Pointer B forward.
            - Result: `[2, 3]`
        3. Compare again: Is A`[1]` (7) smaller than B`[1]` (8)? Yes. Move 7 to the result list. Pointer A is now at the end.
            - Result: `[2, 3, 7]`
        4. Clean up: One list is empty, but List B still has `[8]`. Since it's already sorted, just "pour" the remainder into the result.
            - Final Result: `[2, 3, 7, 8]`

This is what happens when we sort this list: `[2, 1, 3, 4]` (using the python version as an example)
```python
1. merge(divide([2, 1]), divide(3, 4))
2. merge(merge([2], [1]), merge([3], [4])) # All things divided up now!
3. merge([1, 2], [3, 4])
4. [1, 2, 3, 4] # Output of final function execution
```

There is a intermediate step: `merge(merge(divide([2]), divide([1])), merge(divide([3]), divide([4])))` between step 1 and 2.