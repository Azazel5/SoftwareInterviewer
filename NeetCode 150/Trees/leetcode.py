from typing import Optional

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

"""
226. Invert Binary Tree

A classic problem. Here, except the root, every node's must be flipped; we're taking the entire tree's mirror image

An approach I could take is a recursive solution. We do BFS on the tree, while flipping all subtree root nodes. That's
one approach; but how would we know where to place the node or do the switch? The furthest outside nodes and the 
"neighbors" on the inside switch position. What's the pattern here? 



My solution notes
-----------------

I try to call the function recursively just passing root.left and root.right (switching it). Proof that I saw it
somewhere lies in the fact that my function doesn't even take two arguments. And to resolve that, I hastily, without
thinking, split the recursive calls into two and added them together. Which doesn't even make sense because two
None Types cannot be added at the end (the error right now). Plus, the problem requires us to modify the tree-inplace and
return the root, the + operator doesn't make sense.

Okay, doing this results in nothing changing. 


Consulting notes
----------------

You have to do a swap, how do you swap things in Python? Ask yourself: What should the function do to ONE node?
Not "process the whole tree" - just "what do I do at THIS node before recursing?"

We're utilizing a classic post-order traversal: root.left/root.right -> root

Okay, I see. The final swap happens at the root.
So right before the root, the tree in example 1 will be looking like:

    4
   / \
  2   7
 / \ / \
3  1 9  6

which isn't the solution obviously. But then the root does the swap on ITS left and right children giving us

    4
   / \
  7   2
 / \ / \
9  6 3  1


Actual solution notes
---------------------

The actual solution is the same from my solution. So, we'll check out the other solutions. So, yes, as for my question in
"Mistakes I made" section, the iterative way is an approach too. For this, we'd do BFS. 



PATTERN RECOGNITION
-------------------

Core Pattern: "Recursive Tree Transformation" (DFS post-order)

Recognition Signals:
- "Invert/mirror/flip tree" → swap children recursively
- "Transform entire tree" → DFS (recursive or iterative)
- "Modify in-place" → change pointers, return root

This pattern appears in:
- Symmetric Tree (check if tree mirrors itself)
- Flatten Binary Tree to Linked List (transform structure)
- Convert BST to Greater Tree (transform values)
- Maximum Depth of Binary Tree (aggregate property)

Key insight: When you need to modify ALL nodes in a tree,
recursion lets you apply the same operation at every level.

Tree traversal types:
- DFS Recursive (this problem): Clean, uses call stack
- BFS Iterative: Use queue, level-by-level
- DFS Iterative: Use stack, same as recursive but explicit

DFS = recursive, BFS = iterative


VARIATIONS I COULD HANDLE
-------------------------

Easy modifications:
1. Check if tree is symmetric (mirror of itself)
   → Invert left subtree, compare with right
   
2. Invert only nodes at odd levels
   → Add depth parameter, swap only when depth % 2 == 1
   
3. Return inverted tree without modifying original
   → Create new nodes instead of swapping

Medium modifications:
4. Invert tree iteratively (BFS approach)
   → Use queue: dequeue node, swap children, enqueue children
   → Time O(n), Space O(w) where w = max width of tree
   
5. Invert only subtree rooted at given node
   → Find node first (DFS), then invert from there
   
6. Invert N-ary tree (nodes have multiple children)
   → Reverse the list of children instead of swapping two

Hard modifications:
7. Invert tree with parent pointers
   → Must update parent pointers too (more complex)
   
8. Partial inversion based on condition
   → "Invert subtrees where root value > X"
   → Add conditional logic before swapping

Follow-up questions you might get:
- "Can you do this iteratively?"
  → Yes, BFS with queue or DFS with stack
  
- "What's the space complexity?"
  → O(h) for recursion due to call stack
  → O(w) for BFS where w = max width
  
- "What if tree has millions of nodes?"
  → Recursion might overflow stack, use iterative
  → Or increase recursion limit (not ideal)


COMPLEXITY ANALYSIS
-------------------

Time: O(n) where n = number of nodes (we visit each once)
Space: O(h) where h = height of tree (recursion call stack)


EDGE CASES HANDLED
------------------

An obvious edge case is when we have an empty tree. The problem set is pretty small: 100 nodes ranging from -100 to 100


MISTAKES I MADE
---------------


Confusion in thinking. Is BFS only done iteratively or at least it's preferred to be done that way? Why, what does 
the recursive version look like? How does it underperform or is complex? 


BFS is typically iterative (using a queue). You CAN do it recursively but it's awkward and not idiomatic. DFS is naturally
recursive. For THIS problem, both work fine.
"""


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
   if not root:
      return root


   root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
   return root


"""

104. Maximum Depth of Binary Tree

Okay, this problem is another of the classic tree problems. Given a root node, we want to find the longest root to 
leaf node depth. Multiple paths may exist, we want the absolute value of how large the largest one would be. This
naturally supports a DFS solution. I like post-order for this one too because we don't care much about processing
the actual node; most of our work will be in the recursing bit and counting what depth value we're at.


My solution notes 
-----------------

I made a helper function to do the actual DFS, so tracking its return statement and the depth variable would become easy.
I thought: since the helper is returning the depth, and we just want to recurse down subtrees as deeply as we can, 
something like this would make sense return self.dfs(node.left, depth + 1) or self.dfs(node.right, depth + 1). If we
can recurse down any subtree, we do it while incrementing depth. If no further recursion can happen, we return whatever
depth has been stored. 

Failing test case. Off by one. Instead of starting at 0, the root node will be level 1, right? This passes the test 
case. Hit by an empty tree edge case. 

I thought I would handle the one node tree edge case with an explicit if statement, but clearly there's something off
with my logic with the test case [1, 2] returning 3 instead of 1. 

return self.dfs(node.left, depth + 1) or self.dfs(node.right, depth + 1), maybe we need an exclusive OR?

Question: is the height of the tree and the depth of the tree the same?


Consulting notes
----------------

What Does "Maximum Depth" Mean?
For ANY node, its depth is: itself + maximum of its left and right subtree

Are you sure you need a helper function? You did it mindlessly, be honest

As my solution stands right now, returning 

return self.dfs(node.left, depth + 1) or self.dfs(node.right, depth + 1)

returns the first truthy value, not the maximum depth between two subtrees


Actual solution notes
---------------------

The actual solutions give several versions of this problem. Our solution isn't the most optimal in terms of space
complexity because if the tree becomes large enough, the call stack will be overwhelmed. Tail recursion is the solution!



PATTERN RECOGNITION
-------------------

Core Pattern: "Recursive Tree Aggregation" (DFS post-order with return value)

Recognition Signals:
- "Maximum/minimum of entire tree" → recurse both subtrees, compare results
- "Depth/height/level" → count as you recurse
- "Find property across whole tree" → aggregate from children upward

This EXACT pattern appears in:
- Minimum Depth of Binary Tree (same logic, use min instead of max)
- Diameter of Binary Tree (max of left + right depths at each node)
- Balanced Binary Tree (check if |left_depth - right_depth| <= 1)
- Binary Tree Maximum Path Sum (aggregate values instead of counts)

Key insight: When aggregating a property from entire tree:
1. Get property from left subtree (recursive call)
2. Get property from right subtree (recursive call)
3. Combine them at current node (max, min, sum, etc.)
4. Return the result upward

Related patterns:
- Tree modification (Invert Tree): swap then recurse
- Tree aggregation (this problem): recurse then combine
- Tree search (Find value): recurse with early termination

VARIATIONS I COULD HANDLE
-------------------------

Easy modifications:
1. Minimum depth (shortest root-to-leaf path)
   → Use min(left, right) but careful: if one child is None, 
     must use the other (can't stop at non-leaf nodes)
   
2. Count total number of nodes
   → return 1 + countNodes(left) + countNodes(right)
   
3. Sum of all node values
   → return root.val + sum(left) + sum(right)

Medium modifications:
4. Check if tree is balanced (LC 110)
   → At each node, check if |left_depth - right_depth| <= 1
   → Must check ALL nodes, not just root
   
5. Diameter of tree (longest path between any two nodes)
   → At each node: diameter = left_depth + right_depth
   → Track global maximum as you recurse
   
6. Maximum depth with constraint (e.g., path sum equals target)
   → Add condition before counting depth
   
7. Return the actual path, not just depth
   → Track path in parameter, return when depth is max

Hard modifications:
8. Width of tree at each level
   → Need BFS or DFS with level tracking
   → Return max width across all levels
   
9. Maximum depth in N-ary tree
   → return 1 + max(depth of all children)
   → Need to iterate through list of children
   
10. Depth of deepest odd-level leaf
    → Add level parameter, filter for odd levels

Follow-up questions you might get:
- "What if I want minimum depth instead?"
  → Same structure but use min() - BUT watch for None children
  
- "Can you do this iteratively?"
  → Yes, BFS tracking level, or DFS with stack storing (node, depth)
  
- "What's the time/space complexity?"
  → Time O(n) - visit every node once
  → Space O(h) - recursion stack depth = tree height
  
- "What if tree is extremely unbalanced?"
  → Recursion depth could cause stack overflow
  → Use iterative approach with explicit stack


COMPLEXITY ANALYSIS
-------------------

We're doing DFS once more, so the time complexity is O(N) and space complexity is O(H), the height of the tree


EDGE CASES HANDLED
------------------

Empty tree edge case

When there's only one node in the tree, that's a depth of 1 not 2


MISTAKES I MADE
---------------

Creating an unneeded helper function

Using some random logic: return self.dfs(node.left, depth + 1) or self.dfs(node.right, depth + 1)
which would return the first truthy value. We really wanted the maximum depth of any left or right subtree
It seems easier to think about tree recursion problems node by node instead of the entire tree. The line of thinking:
what needs to happen for a certain node. Well its depth will be 1 + whatever is the deepest between its children nodes
really helps

"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
   if not root:
      return 0

   left = self.maxDepth(root.left)
   right = self.maxDepth(root.right)

   return 1 + max(left, right)