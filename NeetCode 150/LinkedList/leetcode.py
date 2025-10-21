from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


"""
206. Reverse Linked List

Okay this is a classic one I have done in the past, but it is time for a repetition. Given the head of a singly linked
list, we have to reverse the list and return the head of the new list. Imagining an array like [1, 2, 3, 4, 5], we'd
need to return [5, 4, 3, 2, 1].

What approaches would work? We loop through each node, and at any iteration we have two things always, the current and the
next node. Actually using this, we also have the previous node, which will be None first because there is no node
prior to the head of a singly linked list. The approach in my head would be, go through the list

[1, 2, 3, 4, 5]

Look at the constraints. We have [0, 5000] nodes in the list, so this is a constant number. An O(N) solution really is
O(1) here, because we know our input space. Values will range from -5000 to 5000 which doesn't really change our solution!
Good.


My solution notes 
-----------------

Clearly I don't remember the solution because my initial approach was to simply keep switching the current node and the
next node. This doesn't really use the prev pointer though. Also, this results in the wrong answer, a not toally
reversed list. Well, couldn't we just switch next directions? Ok, now I think I remember the answer. On every node,
make node.next = prev. Which in the beginning is None, which is fine because head of the original list will be the tail 
of the reversed list. The tail of LinkedList points to a None!

Remembering to always make a copy of the head node, a curr variable, just in case we ever need the head.
Question: rather than doing this, is making a dummy node preferrable?

Since I got to the solution and was pretty confident of what to do, I did not think about any other approaches, look
at the complexity, or anything. I knew the solution would work and it would be O(N) time and O(1) space complexity

Consulting notes
----------------

There are multiple approaches actually to any problem. Even this one. You didn't think about it, but this could be
done recursively or using a stack. 

Also, fill in the actual solution notes, where you can do a trace walkthrough of the algorithm.


Actual solution notes
---------------------

Iterate through the list. We have a variable pointing to None in the beginning which is the elegant part because
prev will be the new head and the old head will be the new tail. At every point, make curr.next = prev
Before you do that, store a reference to the old curr.next to not lose it because you'll need to advance curr to that
Finally, also update prev to curr (before advancing curr to next)


PATTERN RECOGNITION
-------------------

- "Reverse" + "linked list" = iterate with three pointers (prev, curr, next)
- This is a fundamental linked list manipulation pattern
- Shows up in: reverse sublist, swap nodes in pairs, reorder list
- Use a curr variable for iterating through a LinkedList. Use a dummy node if you need to modify, return a new head, or
are building a new list. If the head may change and you need a stable reference. If you need to handle empty head 
elegantly


VARIATIONS I COULD HANDLE
-------------------------

- Reverse only a portion of the list (m to n)
- Reverse in groups of k
- Reverse every other node


COMPLEXITY ANALYSIS
-------------------
O(N) time
O(1) space


EDGE CASES HANDLED
------------------

As usual, we have the empty list, single node, and two nodes
This logic takes care of all these by default. We return prev = None if list is empty, 
In the case, we have a single element too, this works. Remember that it's fine to access a None node, like
curr.next. It's only a problem if we try to do something with it, like curr.next.val. And it works in the 2 node case

MISTAKES I MADE
---------------
Trying to switch individual elements from the list. Like [1, 2, 3, 4, 5] became [2, 3, 4, 5, 1]. Then I remembered what
to actually do in this problem, just flip the orientation of the next's

"""

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
   curr = head
   prev = None

   while curr:
      next_ = curr.next
      curr.next = prev
      prev = curr
      curr = next_

   return prev


"""

21. Merge Two Sorted Lists

We have the heads of two sorted linked lists that we must merge into one single sorted list. The sorted nature of both
lists are an important fact here. I am envisioning looping through both lists while advancing one while it is smaller
than the current head of the other. Because both are sorted, this is easy to do. Keep doing this until you run out of 
nodes! 

Alternative approach: glue both lists and then sort them? Terrible idea, LinkedLists are not ideal for sorting. Recursive?
Yes, I think we could do it that way. Advance one list recursively if it fits our check. Seems like a good exercise to
do. Time complexity would be the same but the space complexity? We would need O(N) calls on the stack AND we'd need to
return the new LinkedList. What would that be?


My solution notes 
-----------------

The solution I presented above would be O(N), as we'd need to go through every node in both lists once. Space complexity
is also O(N), as we need a new list that contains both the original lists.

Trouble thinking about how I will initialize ListNode and where. Balancing the fact that either or both can be None
so I have to be careful with my if checks. I cannot just say list1.val < list2.val without validating that both are for
sure not None. Maybe it'd be cleaner to handle all those anomaly cases at the very begining and only begin looping when
we have elements in both lists!

Both lists could have unequal elements, so it's important to add the rest of the elements in whatever list is not empty
at the end. For example, list1 = [1, 2] and list2 = [1, 4, 7]
Result = [1, 1, 2, 4, 7]

Consulting notes
----------------

All the items written in "mistakes made"


Actual solution notes
---------------------

while list1 and list2, keep looping while elements in both list. You attach the entire list as the next element of the 
dummy node. You alternate as the values grow smaller than the other list, and at the end you attach the remaining elements.
If the lists are empty, we'll connect them to the next of the dummy; if any one has elements remaining, we'll do the same.
This much logic handles all the edge cases 


PATTERN RECOGNITION
-------------------

Core Pattern: "Two-Pointer Merge" + "Dummy Node Builder"

Recognition Signals:
- "Merge two sorted..." → two pointers, one per input
- "Return new list head" → dummy node pattern
- "Maintain sorted order" → compare and advance smaller

This exact pattern appears in:
- Merge Sort (merge step) - same logic, different structure
- Merge K Sorted Lists - extension with min-heap
- Intersection of Two Linked Lists - two pointers, different goal
- Add Two Numbers - similar structure, different operation

Related patterns:
- Fast/Slow pointers - single list traversal
- Three pointers - reverse linked list

Interview Variants:
- If they say "sorted" → think merge pattern
- If they say "build new list" → think dummy node
- Linked list + "combine" → usually two pointers

VARIATIONS I COULD HANDLE
-------------------------

Easy modifications:
1. Remove duplicates during merge
   → Add: if curr.next.val == curr.val: skip
   
2. Merge in descending order
   → Flip comparison: if list1.val > list2.val
   
3. Merge three sorted lists
   → Add third pointer, three-way comparison

Medium modifications:
4. Merge K sorted lists (LC 23)
   → Use min-heap with K elements
   → Time: O(N log K) where N = total nodes
   
5. Merge alternating nodes from each list
   → Don't compare values, just alternate
   
6. Merge only first K nodes from each
   → Add counter, break early

Hard modifications:
7. Merge in-place without dummy node
   → Track head separately, messier pointer logic
   
8. Merge with weighted priorities (not just values)
   → Compare list1.priority vs list2.priority
   
9. Circular linked lists
   → Need to track when you've completed circle

Follow-up questions you might get:
- "What if lists are very different sizes?" 
  → Still O(n+m), the or statement handles remainder
  
- "Can you do this recursively?"
  → Yes: if list1.val < list2.val: list1.next = merge(list1.next, list2)
  → Space becomes O(n) due to call stack
  
- "What if one list is much longer?"
  → Same complexity, no optimization needed
  → The while loop exits early, or handles it efficiently

Common interview traps:
- Forgetting to advance curr pointer (
- Creating new nodes instead of reusing
- Not handling equal values 
- Forgetting to attach remainder

COMPLEXITY ANALYSIS
-------------------

This is an O(N) time complexity, O(1) space complexity solution. Although we're creating a new ListNode, we keep
attaching our existing LinkedLists to it, so we're not creating anything new


EDGE CASES HANDLED
------------------

Immediately we know the edge cases where one of either or both lists are empty. Important to keep that in mind.

What if we have equal values in both lists? Add both, advance both!


MISTAKES I MADE
---------------

I started making new ListNode's instead of reusing the existing list1 or list2 head nodes. Also, I forgot to make a 
copy of the dummy node; this is good practice!

The biggest issue was: I didn't need to bend over backwards trying to imagine how I could handle edge cases when the
solution very cleanly handles all that. curr.next = list1 or list2 handled attaching the rest of the list at the end
because we know that if either is None, all the other elements in the other list are greater than whatever has become
before.

Also, forgetting to advance the pointer variable. Whatever we have as the iterating variable in the while loop must 
advance! 

In the case that two values are equal, the else statement could handle it, which just picks a value from list2 and 
advances it. In the next iteration, both lists will be compared anyways, making it a clean solution for the edge case!

Also, lack of focus while writing. I made a silly mistake with the else if statement, comparing one value to the same
value

"""


# Review Queue:
# 1. Reverse Linked list (review^)
