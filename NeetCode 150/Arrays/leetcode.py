from typing import List
from collections import defaultdict
from heapq import heappush, heappop


"""
347. Top K Frequent Elements


Okay, so the problem is straightforward: given an array, find the top K most frequent numbers. An immediate impulse with 
these kind of problems is to use a dictionary or a Counter. Keep track of everything in the array. An OrderedDict.
But then I thought, could sorting be used here? Nah. Not the best thing. How about a minimum heap? Maybe not the use
case. I am proceeding with the hashmap solution. I mean, normal hashmap plus sorting by values works!

I am using slicing and all kinds of things, just focusing on brute force and getting the solution for now, because I 
know I can get it


My solution notes 
-----------------

Had to do some debugging because I didn't realize that Python sorting is by default in ascending order. To build the 
dictionary, this is O(N). To sort, it is O(N log N), which is the term that dominates. So to make this more efficient,
we need to attack the part that's sorting. Space complexity is O(N)

Two appraoches to learn about: the heap solution and bucket sort


Consulting notes
----------------

Mixed in with other notes


Actual solution notes
---------------------

Following actual solutions besides my own: heap and bucket sort


The heap solution is very intuitive too


The bucket sort is just initializing a 2D list where every inner list represents the frequency of different numbers.
And inside will be the numbers themselves. To use this, we need a character count dictionary again. It seems for this
problem, there's no way around it, every solution uses this much. The bucket sorted array will have mostly empty lists,
but the ones that are filled, the index will represent the frequency. So, when returning the needed value, we have a very
clean structure that we can just return whatever bucket who's length is k


PATTERN RECOGNITION
-------------------


Core Pattern: "Bucket Sort / Counting Sort with Bounded Range"

Recognition Signals:
- "Top K frequent" → heap OR bucket if frequency range is bounded
- Values/frequencies have LIMITED RANGE (0 to n, 1 to 100, etc.) → bucket sort
- Need O(n) instead of O(n log n) sorting → consider bucket/counting sort
- "Frequency" problems → count first, then use frequencies as indices

This bucket sort pattern appears in:
- Sort Characters By Frequency (LC 451) - exact same bucket approach
- Sort Array By Parity (LC 905) - 2 buckets (even/odd)
- Sort Colors (LC 75) - 3 buckets (0, 1, 2)
- Maximum Gap (LC 164) - bucket sort with gap calculation
- H-Index (LC 274) - bucket by citation counts

When to use bucket sort:
✓ Values are in small range [0, k] where k is reasonable
✓ Can use values as array indices
✓ Need linear time O(n) instead of O(n log n)
✗ Values are unbounded (like all integers) - use comparison sort
✗ Need stable sort with specific ordering - use merge sort
✗ Value range is huge (like 10^9) - bucket array too large

Bucket sort vs other approaches:
- Bucket: O(n) but only when range is bounded
- Heap: O(n log k) works for any values
- Sort: O(n log n) general purpose

The "frequency as index" trick:
- Frequencies range from 1 to n (can't exceed array length)
- Use this bounded range to create n+1 buckets
- Place elements in bucket[frequency]
- Collect from back to front = sorted by frequency

Related patterns:
- Counting sort: similar but for sorting by value, not frequency
- Radix sort: bucket sort digit by digit
- Histogram/frequency array: when you need to count occurrences


VARIATIONS I COULD HANDLE
-------------------------

Easy modifications:
1. Return in ascending frequency order (least to most)
   → Iterate buckets from front: for i in range(len(bucket))
   
2. Top K least frequent
   → Same iteration direction (front to back)
   
3. Group elements by exact frequency
   → Return bucket structure: {freq: [elements]}
   
4. Count how many elements have frequency > threshold
   → Sum lengths of buckets above threshold

Medium modifications:
5. Sort Colors (LC 75) - Dutch National Flag
   → 3 buckets for values 0, 1, 2
   → Can do in-place with three pointers
   
6. Sort Characters By Frequency (LC 451)
   → Same exact bucket approach but with characters
   → Build string from buckets: repeat each char freq times
   
7. First Unique Number (frequency = 1)
   → Just return first element from bucket[1]
   
8. Custom Comparator Sort (LC 1636)
   → "Sort by frequency, ties broken by value"
   → Within each bucket, sort by value

Hard modifications:
9. Top K in multiple categories
   → "Top K by frequency AND top K by value"
   → Need multiple bucket arrays or combined sorting
   
10. Bucket sort with range mapping
    → Values in range [1, 10^9] but only 1000 values
    → Map values to buckets: bucket_index = value % num_buckets
    → Handle collisions within buckets
    
11. Dynamic top K (elements added/removed)
    → Maintain bucket structure as data changes
    → Update buckets when frequencies change
    → Track which bucket each element is in

12. 2D bucket sort
    → Sort by two criteria simultaneously
    → bucket[freq1][freq2] = elements
    → Useful for "sort by X, then by Y"

Follow-up questions specific to bucket sort:

- "What if frequencies could be larger than n?"
  → Can't happen in this problem (can't exceed array length)
  → If possible, need different approach or larger bucket array
  
- "What if we can't afford O(n) space for buckets?"
  → Must use heap O(k) or sorting O(1) auxiliary space
  → Trade-off: time vs space
  
- "Does bucket sort work with negative numbers?"
  → Need offset: if values in [-100, 100], use bucket[value + 100]
  → Or separate buckets for negative/positive
  
- "Why not just use a max-heap?"
  → Heap is O(n log k), bucket is O(n)
  → Bucket works because frequency range is bounded
  → For general "top K" without bounded range, heap is better

Comparison table for "top K" problems:

| Input Constraint | Best Approach | Time | Why |
|-----------------|---------------|------|-----|
| Bounded frequencies (1 to n) | Bucket sort | O(n) | Can use as indices |
| Small k (k << n) | Min-heap | O(n log k) | Only track k elements |
| Large k (k ≈ n) | Sort or quickselect | O(n log n) or O(n) | Need most elements anyway |
| Streaming data | Heap | O(n log k) | Can update dynamically |
| Need stable order | Sort | O(n log n) | Maintains relative order |


COMPLEXITY ANALYSIS
-------------------

The initial approach was O(N log N), which was the dominating factor due to sorting. But the heapified versin:


Inside the O(n) loop, you do:

heappush → O(log k) (heap size is at most k)
heappop → O(log k) (heap size is at most k)
Total: O(n) iterations x O(log k) per iteration = O(n log k)

Space complexity is O(N) due to the dictionary and O(K) because the heap will only hold K elements, which will be dominated
by O(N) factor!


EDGE CASES HANDLED
------------------



**Bucket Sort Specific:**
- All elements same frequency: 
  → All go in same bucket, return first k from that bucket ✓
  → Example: [1,2,3], k=2 → bucket[1] = [1,2,3] → return [1,2]

- k equals number of unique elements:
  → Return all elements (collect entire bucket array) ✓
  → Example: [1,1,2,2,3,3], k=3 → return [1,2,3]

- Most buckets empty:
  → Skip empty buckets efficiently in loop ✓
  → Example: [1,1,1,1,1], k=1 → only bucket[5] has data

- Multiple elements with same frequency:
  → All stored in same bucket, order doesn't matter ✓
  → Example: [1,1,2,2], k=1 → bucket[2] = [1,2], return [1] (or [2])

**General Edge Cases:**
- Empty array: [] → Not in constraints (1 ≤ nums.length)
  
- Single element: [5], k=1 → bucket[1] = [5] → [5] ✓

- k = 1 (only most frequent):
  → Find highest non-empty bucket, return first element ✓
  → Could optimize: don't need full bucket iteration
  
- k = n (all elements):
  → Collect from all buckets, returns entire array ✓
  
- All unique elements (worst case for space):
  → Each element in bucket[1], return first k ✓
  → Example: [1,2,3,4,5], k=3 → [1,2,3] (any 3)
  
- Duplicate values don't matter:
  → [1,1,1,2,2,3], k=2 → frequencies are [3,2,1]
  → bucket[3]=[1], bucket[2]=[2], bucket[1]=[3]
  → Return [1,2] ✓

**Tricky Cases:**
- Ties at kth position:
  → Problem allows "any order", so return any k elements ✓
  → Example: [1,1,2,2,3], k=2, both 1 and 2 have freq=2
  → Can return [1,2] or [2,3] depending on iteration
  
- Negative numbers:
  → Frequencies are always positive, so bucket indices valid ✓
  → Example: [-1,-1,5], k=1 → bucket[2]=[-1] → [-1]

- Very large array (n = 10^5):
  → Bucket array size n+1 = 100,001 elements
  → Still O(n) space, acceptable ✓
  → Mostly empty but doesn't matter

**What Could Break Bucket Sort:**
✗ If frequencies could exceed n (impossible here)
✗ If we needed stable sort (doesn't matter for this problem)
✗ If n was 10^9 (bucket array too large) - use heap instead
✗ If we needed exact ordering within same frequency (problem says "any order")

**Testing Strategy:**
Test with:
1. All same value: [1,1,1,1]
2. All unique: [1,2,3,4]
3. Mixed frequencies: [1,1,1,2,2,3]
4. k=1, k=n, k=n/2
5. Negative numbers: [-1,-1,0,0,1]


MISTAKES I MADE
---------------

Trust your instincts more. The moment you see TOP or LEAST, you gotta be thinking min-max heaps!

"""

def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    frequent = sorted(d.items(), key=lambda k: k[1], reverse=True)
    res = frequent[:k]
    return list(map(lambda tup: tup[0], res))


# Heap version

def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = []
    character_count = defaultdict(int)

    for n in nums:
        character_count[n] += 1

    for number, freq in character_count.items():
        heappush(res, (freq, number))  # The first element will be used while pushing

        if len(res) > k:
            heappop(res)

    return [num for _, num in res]



# Bucket sort version

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int)
            
    for n in nums:
        count[n] += 1

    
    bucket = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        bucket[freq].append(num)


    result = []

    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)

            if len(result) == k:
                return result

    return result


# Review Queue:
# 1. Top K Frequent Elements (review on Oct 24, Friday, 2025)