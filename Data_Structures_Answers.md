Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
This is O(1). There is no way to call this in a way that will change its runtime.

2. What is the space complexity of your ring buffer's `append` function?
If the list is full, item - 1
If list isn't full, item - self.storage[self.current]
O(n) So, the space complexity is LINEAR and increases with the value of item.

3. What is the runtime complexity of your ring buffer's `get` method?
this is O(n), with n being capacity because length of self.storage is dependant on capacity in the constructor.

4. What is the space complexity of your ring buffer's `get` method?
O(n) This is increases with the size of self.storage

5. What is the runtime complexity of the provided code in `names.py`?
This is O(n^2) as it includes a for loop nested within another

6. What is the space complexity of the provided code in `names.py`?
O(n) This increases linearly with the amount of matches found between two lists.

7. What is the runtime complexity of your optimized code in `names.py`?
This is O(n log n) as we are using equality operators <= and > within insert to sort data into the tree, so that when search is used much less comparisons have to be made.

8. What is the space complexity of your optimized code in `names.py`?
This is O(n) and increases alongside matches found between two binary search trees.