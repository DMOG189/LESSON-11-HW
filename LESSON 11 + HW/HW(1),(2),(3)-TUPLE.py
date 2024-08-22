# HOMEWORK 1 , 2 , 3 LESSON 11 TU5645PLE

# TUPPLE:
# 1. Create a tuple containing the number 99.
# 2. Create a tuple containing the numbers 77, 88, 99.
# 3. Write a function that receives a tuple and returns its length.
# 4. Write a function that receives two tuples and returns them concatenated.
# 5. Write a function that receives two tuples and returns a tuple containing only the common elements.
# 6. Write a function that receives two tuples and returns a tuple containing only the unique elements.
# 7. Write a function that receives a tuple and an index,
# and returns the element at that index, or None if out of range.
# 8. Write a function that receives a tuple and returns it in reverse order.
# 9. Write a function that receives a tuple and a number,
# and returns the count of elements in the tuple that are divisible by that number.
# 10. Write a function that receives a tuple and a number,
# and returns the tuple repeated that many times.
# 11. Write a function that receives a tuple and returns a tuple with each element paired with its index.
# 12. Write a function that receives a tuple of numbers and returns a dictionary with statistical analysis.
# 13. Write a function that receives a tuple of letters and returns a string.
# 14. Write a function that receives a string and returns a tuple of its letters.
# 15. Write a function that receives a tuple and a number, and returns the tuple without the number.
# 16. Write a function that receives a tuple and returns a tuple without duplicates.
# 17. Write a function that receives a tuple and a number, and returns the indices of the number in the tuple.
# 18. Collect names and scores from the user until “done” or -999 is entered, then pair them in a tuple.


# START

# TUPPLE:

# 1. Create a tuple containing the number 99:
tup_a = (99,)
print(tup_a)
# Output: (99,)

# 2. Create a tuple containing the numbers 77, 88, 99:
tup_b = (77, 88, 99)
print(tup_b)
# Output: (77, 88, 99)

# 3. Write a function that receives a tuple and returns its length:
def get_tuple_length(tup: tuple) -> int:
    return len(tup)

print(get_tuple_length(tup_b))
# Output: 3

# 4. Write a function that receives two tuples and returns them concatenated:
def concatenate_tuples(tup1: tuple, tup2: tuple) -> tuple:
    return tup1 + tup2

print(concatenate_tuples(tup_a, tup_b))
# Output: (99, 77, 88, 99)

# 5. Write a function that receives two tuples and returns a tuple containing only the common elements:
def common_elements(tup1: tuple, tup2: tuple) -> tuple:
    return tuple(set(tup1) & set(tup2))

tup_e1 = (3, 4, 5, 6)
tup_e2 = (1, 2, 3, 4)
print(common_elements(tup_e1, tup_e2))
# Output: (3, 4)

# 6. Write a function that receives two tuples and returns a tuple containing only the unique elements:
def unique_elements(tup1: tuple, tup2: tuple) -> tuple:
    return tuple(set(tup1) ^ set(tup2))

print(unique_elements(tup_e1, tup_e2))
# Output: (1, 2, 5, 6)

# 7. Write a function that receives a tuple and an index,
# and returns the element at that index, or None if out of range:
def get_element_at_index(tup: tuple, index: int):
    return tup[index] if 0 <= index < len(tup) else None

print(get_element_at_index(tup_b, 1))
# Output: 88
print(get_element_at_index(tup_b, 5))
# Output: None

# 8. Write a function that receives a tuple and returns it in reverse order:
def reverse_tuple(tup: tuple) -> tuple:
    return tup[::-1]

print(reverse_tuple(tup_b))
# Output: (99, 88, 77)

# 9. Write a function that receives a tuple and a number,
# and returns the count of elements in the tuple that are divisible by that number:
def count_divisibles(tup: tuple, num: int) -> int:
    return sum(1 for x in tup if num % x == 0)

tup_i = (10, 5, 3, 5, 8, 10, 50, 30, 40)
print(count_divisibles(tup_i, 10))
# Output: 5

# 10. Write a function that receives a tuple and a number,
# and returns the tuple repeated that many times:
def repeat_tuple(tup: tuple, times: int) -> tuple:
    return tup * times

print(repeat_tuple((1, 2), 3))
# Output: (1, 2, 1, 2, 1, 2)

# 11. Write a function that receives a tuple and returns a tuple with each element paired with its index:
def enumerate_tuple(tup: tuple) -> tuple:
    return tuple(enumerate(tup))

print(enumerate_tuple(('apple', 'banana', 'cherry')))
# Output: ((0, 'apple'), (1, 'banana'), (2, 'cherry'))

# 12. Write a function that receives a tuple of numbers and returns a dictionary with statistical analysis:
def tuple_statistics(tup: tuple) -> dict:
    stats = {
        'max': max(tup),
        'min': min(tup),
        'average': sum(tup) / len(tup),
        'count': len(tup),
        'sorted_desc': sorted(tup, reverse=True),
        'sorted_asc': sorted(tup)
    }
    # Bonus:
    stats['occurrences'] = {num: tup.count(num) for num in tup}
    return stats

tup_l = (10, 5, 3, 5, 8, 10, 50, 30, 40)
print(tuple_statistics(tup_l))

# 13. Write a function that receives a tuple of letters and returns a string:
def tuple_to_string(tup: tuple) -> str:
    return ''.join(tup)

print(tuple_to_string(('H', 'e', 'l', 'l', 'o')))
# Output: Hello

# 14. Write a function that receives a string and returns a tuple of its letters:
def string_to_tuple(s: str) -> tuple:
    return tuple(s)

print(string_to_tuple("Hello"))
# Output: ('H', 'e', 'l', 'l', 'o')

# 15. Write a function that receives a tuple and a number, and returns the tuple without the number:
def remove_number(tup: tuple, num: int) -> tuple:
    return tuple(x for x in tup if x != num)

print(remove_number(tup_l, 10))
# Output: (5, 3, 5, 8, 50, 30, 40)

# 16. Write a function that receives a tuple and returns a tuple without duplicates:
def remove_duplicates(tup: tuple) -> tuple:
    seen = set()
    unique = []
    for item in tup:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return tuple(unique)

print(remove_duplicates(tup_l))
# Output: (10, 5, 3, 8, 50, 30, 40)

# 17. Write a function that receives a tuple and a number, and returns the indices of the number in the tuple:
def find_indices(tup: tuple, num: int) -> tuple:
    return tuple(i for i, x in enumerate(tup) if x == num)

print(find_indices(tup_l, 5))
# Output: (1, 3)

# 18. Collect names and scores from the user until “done” or -999 is entered, then pair them in a tuple:
def collect_names_and_scores():
    names = []
    scores = []
    print("Enter names (type 'done' to finish):")
    while True:
        name = input()
        if name == 'done':
            break
        names.append(name)

    print("Enter scores (type '-999' to finish):")
    while True:
        score = input()
        if score == '-999':
            break
        scores.append(int(score))

    return tuple(zip(names, scores))


# Example :
print(collect_names_and_scores())


# END

# HOMEWORK 2 QUESTIONS ? :

# whats the different between tuple and a list?
# when is best to use each?

# tuple: Immutable, meaning once a tuple is created,
# its elements cannot be changed, added, or removed.

# list: Mutable, meaning you can change,
# add, or remove elements after the list is created.

# When to Use Each:

# Use tuple when:
# You have a fixed collection of items that should not change.
# You want to ensure the integrity of your data by preventing accidental modifications.
# You need to use a sequence as a key in a dictionary (since tuples are hashable).
# You are dealing with data that will be accessed frequently but not modified,
# as tuples are more memory efficient and slightly faster for read-only operations.

# Use list when:
# You need a sequence of items that can change, where elements will be added, removed, or updated.
# You need to frequently modify the sequence, sort it, or perform various operations on the elements.
# You are working with a collection of items where flexibility is required,
# like managing dynamic datasets or user inputs.

# conclusion:
# tuple: Immutable, fixed, faster, and used for read-only operations or where data integrity is crucial.
# list: Mutable, flexible, more feature-rich, and used when you need to modify the sequence of items frequently.


# HOMEWORK 3 GIVEN CODE

# START

# EXPLAIN why is the code does not give an ERROR?

data_tuple = (
{"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0] ["age"] = 31
data_tuple[0] .clear()

# EXPLANATION :
# The code does not cause an error because the operations are modifying the contents of
# the mutable dictionary inside the tuple, not the structure of the tuple itself.
# Tuple Immutability:
# A tuple itself is immutable, meaning the structure of the tuple
# (the number and order of elements) cannot be changed after it is created.


# END
