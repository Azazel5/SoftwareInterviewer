from collections import Counter, defaultdict

# For the Amazon interview, read up on scalability and distributed systems
# For resume bullet points, think of writing them in this format: accomplished X by using Y which led to Z
# Build projects, learn new technologies, read books, take courses, implement DS&A from scratch, and do
# mock interviews

# The behavioral interview grid: challenges, mistakes/failure, enjoyed, leadership, conflicts, what you would do
# differently

# Answer questions by using the nugget - S.A.R protocol (Situation, action, result)

# Self introduction: current role, college, post college, outside the work

### Big O

# No matter how big the constant is or how slow the linear slope is, at some point in time, the linear time 
# complexity will pass the constant time algorithm

# Describe the runtimes of algorithms in three ways: best case, worst case, and expected (big O)

# Space complexity is important in algorithms as well. O(n) is not always better than O(n^2). It depends on the
# inputs

# When a problem halves the number of elements each time, it will be O(log n) because the reverse is true: the
# elements are getting squared each time

def two_recursive(n):
    if n <= 1:
        return n
    
    return two_recursive(n - 1) + two_recursive(n - 1)

# Just because there are two recursive calls doesn't mean this algorithm is O(n^2)
# Calling two_recursive(4) calls two_recurive(3) twice, each of those will call two_recursive(2), twice, so it's
# getting squared each turn. The runtime is O(2^n), space complexity is O(n) because at any given moment, we only
# work with one chain of two_recursive calls

def not_n_squared_runtime(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] > list2[j]:
                print("HAHA")

# This isn't O(N^2) because the number of elements for list1 and list2 are different. Call it O(AB) where A and B
# are the lengths of those arrays

# If there's a loop working with a constant number, it will not change the runtime even if it is embedded within
# another loop. Remember that we're measuring the runtime in terms of input!

# Array of strings. Sorted each string and then the whole array. Depends on the sorting algo. Let's loop thru each
# n times we carry out O(nlog n) which is n^2logn. Then we sort the whole array, which will be O(logn) or
# O(nlogn). Thus the entire complexity is  n^2logn.

# The solution above is incorrect because we treated the length of the strings and length of the array the same
# s is the length of the longest string and a is the length of the array. O(s log s * a) + O(a log a). You are
# fine until now but you need to know that string comparision also takes O(s) time. Each sorting will require
# string comparision so the term becomes O(as log a). So the total is O(s log s * a) + O(as log a)

# A binary tree sum problem may seem like an exponential problem, but it's not! It is O(N)

# Generally speaking, multiple recursive calls means an exponential runtime

# Exercises Chapter 1 

def question_11(string):
    """ Brute force """

    # cnt = Counter(string)

    # for letter, freq in cnt.items():
    #     if freq > 1:
    #         return False
        
    # return True

    """ No additional DS """

    sorted_string = sorted(string)

    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
        
    return True
        
def question_12(str1, str2):
    # We want to know if each letter in str1 or str2 occurs at least once in the other
    return sorted(str1) == sorted(str2)

def question_13(string):
    # strii = []
    char_list = list(string)

    for i in range(len(char_list)):
        if char_list[i] == ' ':
            char_list[i] = '%20'
            # strii.append('%20')
        else:
            pass
            # strii.append(char)

    # return ''.join(strii)
    return ''.join(char_list)

def question_14(string):
    string = string.lower()

    c = Counter(string)
    
    for char, freq in c.items():
        odd_count = 0

        if char != ' ':
            if freq % 2 != 0:
                odd_count += 1

        return odd_count <= 1

def question_15(string1, string2):
    differences = 0

    if len(string1) + 1 == len(string2):
        return helper_15(string1, string2)

    elif len(string1) - 1 == len(string2):
        return helper_15(string2, string1)
    else:
        differences = 0

        for i in range(len(string1)):
            if string1[i] != string2[i]:
                differences += 1

        return differences <= 1

def helper_15(string1, string2):
    added_subtracted_or_updated = False
    i, j = 0, 0

    while i < len(string1) and j < len(string2):

        if string1[i] != string2[j]:
            print(string1[i], string2[j])
            if added_subtracted_or_updated:
                return False
            
            added_subtracted_or_updated = True
            j += 1

        else:
            i += 1
            j += 1

    return True

def question_16(string):
    result = []
    length = len(string)

    counter = 1
    for i in range(length):     
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                counter += 1
            else:
                result.append(string[i] + str(counter))
                counter = 1
        else:
            result.append(string[i] + str(counter))

    res = ''.join(result)

    return res if len(res) < length else string

def question_17(matrix):
    ''' Copied from solution manual. Do not understand this algorithm.. :( '''

    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            print(top)

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top

    return matrix

def question_18(matrix):
    li = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                li.append((i, j))

    for row, _ in li:
        for j in range(len(matrix[row])):
            matrix[row][j] = 0

    for _, col in li:
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix


mat =       [[1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]]

def question_19(string1, string2):
    res = string2 + string2

    return string1 in res

# Linked Lists

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def append_to_tail(self, val):
        cur = self

        while cur.next:
            cur = cur.next

        cur.next = Node(val)

    def remove_duplicates(self):
        tracker = defaultdict(int)
        cur = self
        prev = None

        while cur:
            tracker[cur.val] += 1

            if tracker[cur.val] > 1:
                if cur.next:
                    prev.next = cur.next
                else:
                    prev.next = None

            prev = cur
            cur = cur.next

    def remove_duplicates_constant_space(self):
        if self is None:
            return
        
        cur = self
        while cur:
            runner = cur

            while runner.next:
                if runner.next.val == cur.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            
            cur = cur.next

    def kth_last(self, k):
        turtle, hare = self, self
        turtindex, hareindex = 0, 0

        while turtle.next:
            if not hare.next:
                element_to_reach = hareindex - k

                if turtindex != element_to_reach:
                    turtle = turtle.next
                else:
                    return turtle

            turtle = turtle.next 
            turtindex += 1
            hare = hare.next.next
            hareindex += 2

    def __str__(self):
        st = []
        cur = self

        while cur:
            st.append(str(cur.val))
            cur = cur.next

        return '->'.join(st)

n = Node(5)
n.append_to_tail(7)
n.append_to_tail(7)
n.append_to_tail(9)
n.append_to_tail(11)
n.append_to_tail(9)
print(n.kth_last(2))
