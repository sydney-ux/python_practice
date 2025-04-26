# Function to reverse a string without using [::-1] or built-in methods
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Adds each character in front
    return reversed_str

# Input from user
name = (input("Enter a string: ") )
reversed_name = reverse_string(name)
# Print the reversed string
print("Reversed string:", reversed_name)
