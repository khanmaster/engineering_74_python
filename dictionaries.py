# What is a Dictionary?
# Dictionary (arrays) is another way managing data but more Dynamically
# Key Value pairs to store and manage data
# Syntax : {} bracket
# what type of data can we store/manage
# Let's create one

devops_students_data = {
    "key": "value",
    "name": " james",
    "stream": "tech",
    "completed_lessons": 4,
    "hobbies": ["watching movies", "data types", "variables"]
}

# adding an item in the list inside dictionary
devops_students_data["hobbies"].append("running")
print(devops_students_data)

# removing an item from the list inside dictionary
devops_students_data["hobbies"].remove("data types")
print(devops_students_data)


# # Deleting an item from the list inside dictionary
# devops_students_data["hobbies"].remove("data types")
# print(devops_students_data)
#
# # appending an item in the list inside dictionary
# devops_students_data["hobbies"].append("Golf")
# print(devops_students_data)



# print(devops_students_data.values())
#print(type(devops_students_data))
# display the data by fetching the key name
#print(devops_students_data["completed_lessons"])
#print(devops_students_data["name"])
#print(devops_students_data.keys())

#print(devops_students_data["completed_lesson_names"])


# How can I change the value of specific key
# devops_students_data["completed_lessons"] = 3
# print(devops_students_data["completed_lessons"])
# print(type(devops_students_data.items()))
# How can we fetch the value called "data types"

# Task
# create a New dictionary to store user details

# all the details that you utilised in the last task name, DOB, Address, course, grades,
# methods of dictionary to remove, add, replace, display the type of items
# create a list of hobbies of at least 3 items
# display data in revers order of hobby list
