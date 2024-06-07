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