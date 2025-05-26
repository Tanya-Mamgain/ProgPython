marks = {"John": 85, "Alice": 90}
marks.pop("Alice")
print(marks)  # Output: {'John': 85}
print(marks.pop("Tanya", "Key not found"))  # Output: Key not found
