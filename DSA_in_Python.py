# Python Primer

# The -i flag opens the file in interactive mode. You can continue commands onto the next line via the \ character
# Strings and lists evaluate to False if empty including 0 valued numerals. bool() keyword/constructor also exists
# Conversion of an int to a different base, int(10, 2). int('s') returns the int value of the character 's'
# Scientific notation = 6.022e23
# Tuples are streamlined version of lists
# list('string') or any other iterable type, passed to list works
# A tuple of 1 element needs one comma: (1, )

# Format string by passing number of significant digits into format string like: 
print("This is 3 significant digits: {0:.3}".format(1.11324))

temperature = 5
alias = temperature
temperature += 5   # This doesn't affect the variable "alias"
print(temperature, alias)

# int and float constructors can parse string values
print(float('3.14'))

# There are no orders to sets. We can check if an item exists in a set and this is highly optimized thanks to HashTables
# Only immutables types can be added, so yes to tuples but no to lists. Frozenset = immutable set

# This kind of argument is also accepted by dict()
mappings = [('Conor McGregor', 'UFC'), ('Demetrious Johnson', 'Bellator')]
print(dict(mappings))

# a is b and a == b are different and could provide different results!

# Interesting operators for dictionaries and sets. | -> union, & (set) intersection, - (set) elements in one
new_dict = {'a': 10, 'b': 20}
print(set(dict(mappings)) & set(new_dict))

# var += 5 and var = var + 5 has subtle differences, especially when using aliases
# Operations such as a = b = c and 0 <= x + y <= 20 are valid

# When we pass parameters to functions, Python makes aliases from the actually passed parameters to the formal
# parameters. This has consequences when the parameters are mutable, as the states of the parameters may change.
# We can enforce function parameters to become keyword arguments

# It is customary to check the type of parameter first and then the value
# We can catch more than one type of exception: except (IOError, ValueError). Or we can break it up into 
# multiple except blocks

# Iterables are lazily constructed. range(100000) will not set aside memory for 100000 numbers immediately
# It'll only do that as required. However, list(range(100000)) will. Many python library functions operate
# this way for the sake of efficiency

# Create iterators through generators! A function that yields instead of returning. 

def traditional(n):
    li = []

    for i in range(1, n + 1):
        if n % i == 0:
            li.append(i)

    return li

def generator(n):
    for i in range(1, n+ 1):
        if n % i == 0:
            yield i

# This returns a generator object which can be constructed into a list by the list() constructor. We can have multiple
# yields to a single function

# dir() and vars() are ways to check namespaces and attributes

# Top level commands of a module are executed when you import it, causing the issues you saw several years ago in the
# stock program you wrote. This is the reason why we use if __name__ == "__main__". It is also used while unittesting.

# Object Oriented Programming

# Methods of a class starting with _ are assumed to be protected and __ are private

# We can overload operators in class definitions to make things like Class1 + Class2 make sense through methods like
# __add__ or __mul__. All operators have an equivalent function, even things like indexing

class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Step cannot be 0")
        
        if stop == None:
            start, step = 0, start

        self._start = start
        self._step = step
        self._length = max(0, (stop - start + step - 1 // step))

    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            k += self._length

        if not 0 <= k < self._length:
            raise IndexError("Index not in range")
        
        return self._start + k * self.step
    
# Be careful about creating shallow copies. Use the copy module to create deep copies

# Algorithm Analysis

# We can use time.time() before and after the algorithm finishes running but this is not going to be
# acccurate as it will depend on what other processes are running on the computer at that time. A more
# accurate, but still not perfect metric, would be the use of the clock() function which measures CPU
# cycles. The biggest difficulty of using experimental analysis is that we would need to implement
# various algorithms to analyze their runtimes, which is a significant time waster

# An alogorithm's number of primitive operations is proportional to the runtime
# Since determining average runtime requires a more complicated approach, most runtime analysis focuses
# on worst case and best case behaviors. 

# 7 functions for algorithmic analysis
# Constant function, f(x) = c. It doesn't matter what the input is, the function takes a set amount of
# time

# Logarithmic function, f(x) = log(b)(n) [log n <= n]

# Linear function, f(x) = x

# nLogn function, f(x) = xlog(x) [the fastest possible algorithm for sorting follows this runtime]

# Quadratic function, f(x) = x^2

# Cubic function, f(x) = x^3

# Exponential function. f(x) = b^x

# Big O notation allows us to ignore primitive, constant operations and focus on the things that affect the
# algorithm's runtime the most: higher order operations.

# Big O = less than or equal to
# Big Omega = greater than or equal to
# Big theta = at the same rate

# Even if we're abstracting away the constant factors and lower order terms, it is still important to be mindful
# of them as, in some scenarios, they will make a significant difference.

# The mathematical definition of big O notation is that f(x) <= cg(n) for n >= n0. For a certain input size, g(n)
# is greater than f(x) so f(x) is O(g(n)), big O of g(n), f(x) is guaranteed to be lower than g(x) for that input and
# above

# One algorithm is asymptotically greater than another if we compare runtimes and one runs in the order of n and the
# other log(n) for example

# Be aware of list slicing techniques as they may seem to be more efficient - they certainly take up less space - but
# it also does looping

# N^2 implementation
def prefix1(arr):
    A = [0] * len(arr)

    for i in range(5):
        running_sum = 0

        for j in range(i):
            running_sum += arr[j]   

        A[j] = running_sum / len(A)

    return A

# N implementation
def prefix2(arr):
    A = [0] * len(arr)
    total = 0

    for i in range(len(arr)):
        total += arr[i]
        A[i] = arr[i] / (i + 1)

    return A

# Mathematical statements can be proved by induction, contrapoitve, or contradiction

### Recursion

def facorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * facorial_recursive(num - 1)

# For binary search to work, we need to have the elements saved in sorted order.

def binary_search(data, target, low, high):
    if low > high:
        return False
    
    mid = (high + low) // 2
    
    if data[mid] == target:
        return True
    elif data[mid] < target:
        binary_search(data, target, mid + 1, high)

    elif data[mid] > target:
        binary_search(data, target, low, mid - 1)

# Alright, so recursive algorithms are a great way to solve difficult problems. But how do we measure its
# efficiency? You take a look at how many times the function needs to call itself and what the contents
# of the function body is doing in each activation call. For instance, in the factorial problem, we have
# a constant operation occuring n times, so it is O(n)

#########   DATA STRUCTURES      ######### 

# Arrays 

# In an array, each block of memory for each elements to have the same size. But different numerals or strings
# have different lengths and thus different memory. Python solves this problem by only holding the reference
# addresses to each element of the list. The bit of reference addresses take up the same amount of memory so
# it works out