from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

"""
704. Binary Search

The goal is to write the literal binary search algorithm, meaning, when given a target number in an array,
find it if it exists, otherwise -1. Do it in log time. For this to work, we need the array to be sorted, which it is

Not sure what new approach we can try besides the actual solution. But the time complexity will be O(log N) and space
complexity will be O(1) ----> this is where you push yourself!

My solution notes
-----------------

I didn't think about binary search with an array with only 1 element. What do we do? After my check,
I failed a test case with only two elements. Binary search doesn't really work in the 2 element case because there
are no new places to increment to or decrement.

Question: when do we set low <= high versus low < high? How to think about this?

Consulting notes
----------------

- Always use low <= high because you want to eliminate all possibilities
- Remember that in binary search, we're not incrementing and decrementing the indices by one. Because if we were to do
that, we'd just use a normal loop! Binary search is about halving the search space on every iteration, hence the log time

Actual solution notes
---------------------

- Turns out, the moment we do low <= high, our solution comes up and we can even get rid of the if statement. In the case of 
only having one element [5], low == high so it never entered the loop and returned -1. Ok. But why was it failing in 
the case of [2, 5]; target=5? low = 2, high = 5, mid would be 0. That's lower, so we move low = mid + 1. And this is where
my original code probably failed. low would be equal to high, so the loop would end but that's precisely where
nums[mid] == target -> mid = 1, nums[1] == 5! 

PATTERN RECOGNITION
-------------------

When I see: "sorted array" + "find target" + "O(log n)"
I should think: binary search

VARIATIONS I COULD HANDLE
-------------------------

- Find insertion position if not found
- Find first/last occurrence of target
- Search in rotated sorted array 


COMPLEXITY ANALYSIS
-------------------

- Time: O(log n) - why? We halve search space each iteration
- Space: O(1) - why? Only using 3 variables (low, high, mid)

EDGE CASES HANDLED
------------------

- Empty array: doesn't apply, constraints say n >= 1
- Single element: works because low <= high
- Two elements: works because we jump to mid ± 1
- Target not in array: return -1 at end

MISTAKES I MADE
---------------

- Used low < high instead of low <= high
- Moved pointers by ±1 instead of jumping to mid ± 1
"""


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] > target:
            high = mid - 1

        elif nums[mid] < target:
            low = mid + 1

        else:
            return mid

    return -1


# Review Queue:
# 1. Binary Search (review on Oct 22, Wednesday, 2025)