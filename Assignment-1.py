# List
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Sliced list:", numbers[1:4])

numbers.append(60)
print("After append:", numbers)

numbers.remove(30)
print("After remove:", numbers)

# Tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("\nTuple:", fruits)
print("First element:", fruits[0])
print("Sliced tuple:", fruits[1:3])

# Dictionary
student = {
    "Name": "Ira",
    "Roll No": 1,
    "Course": "B.Tech CSE"
}

print("\nDictionary:", student)
print("Name:", student["Name"])

student["Marks"] = 85
print("After adding Marks:", student)

student["Course"] = "CSE"
print("After updating Course:", student)

del student["Marks"]
print("After deleting Marks:", student)
