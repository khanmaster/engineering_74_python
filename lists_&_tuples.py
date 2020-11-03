# collection in python
# Lists?
# Lists are MUTABLE -
# We can add, remove, change an item in the list
# indexing starts with 0
# "hello world!
# Syntax: ["yugert", "apple", "milk"]

# Let's create a list

# shopping_list = ["apple", "milk", "bread"]
# print(shopping_list)
# # print(type(shopping_list))
# #
# # # look at indexing and slicing in the list items
# #
# # print(shopping_list[1])
# # print(shopping_list[2])
# # print(shopping_list[-1])
#
#
# # Managing Lists
# # add an item to this list
#
# shopping_list.append("eggs")
# # append method adds an item at the end of the list
# print(shopping_list)
#
# # how can we remove and item from our list
# shopping_list.remove("apple")
# print(shopping_list)
#
# # how can we remove the last item from our list that we appended earlier
# shopping_list.pop()
# print(shopping_list)
# #
# # # How can I replace an item in my list
# #
# # shopping_list[1] = "fruits"
# # print(shopping_list)
# #
# # can we have mixed data types in the list
#
# mixed_shopping_list = [1, 2, 3, "apple", "milk", "bread"]
# print(mixed_shopping_list)
#
# # Task: create a mixed data type list of 7 items
# # display the type of the data
# # add, delete, replace, pop
# # use indexing to print the list in reverse order
# # 10 minutes to complete and share your github link at 11:52


# # Tuples are IMMUTABLE - CAN'T BE CHANGED
# # Use cases NI number, DOB, place of birth
#
# # Syntax: we use () to declare a Tuple
#
# short_list = ("paracetamol", "eggs", "supermalt")
# print(type(short_list))
# short_list[1] = "fruits" # this line of code throws an error as Tuple does not allow us to change anything

devops_students = {
    "key": "value",
    "name": "James",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data types", "lists"]

}

print(type(devops_students))
