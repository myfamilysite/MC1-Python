# Create the dictionary with the provided data
student_data = {
    "Emma": {"Math": 90, "Science": 85},
    "Liam": {"Math": 78, "Science": 88},
    "Sophia": {"Math": 92, "Science": 95}
}

# Iterate through the dictionary to print in the requested format
for student, scores in student_data.items():
    print(f"{student}'s Scores:")
    print(f"Math: {scores['Math']}")
    print(f"Science: {scores['Science']}")
    print()  # Adds an empty line for readability between students






