
# Conditional Statements in Python
# Conditional statements are used to make decisions based on certain conditions. Python provides various ways to handle these, using if, elif, else, and the ternary operator.

# 1. if Statement
# Syntax:

# if condition:
#     # code to execute if the condition is true
# Description: Executes a block of code only if the specified condition is True.
# Example:

value_a = 1
if value_a == 1:
    print("value_a is equal to one")
# 2. if-else Statement
# Syntax:

# if condition:
#     # code if condition is true
# else:
#     # code if condition is false
# Description: Executes one block of code if the condition is True, and another if it is False.
# Example:

value_a = 1
if value_a == 1:
    print("value_a is equal to one")
else:
    print("value_a is not equal to one")
# 3. if-elif-else Statement
# Syntax:

# if condition1:
#     # code if condition1 is true
# elif condition2:
#     # code if condition2 is true
# else:
#     # code if all conditions are false



# Description: Checks multiple conditions sequentially. The first True condition's block will execute, and the remaining conditions are skipped.
# Example:

grade = 'B'
if grade == 'A':
    print('grade is A')
elif grade == 'B':
    print('grade is B')
elif grade == 'D':
    print('grade is D')
else:
    print('grade is not A, B, or D')

# 4. Evaluation of Composed Boolean Expressions
# Description: You can combine conditions using logical operators (and, or, not) to create complex expressions.
# Example:

altitude = 0
if altitude > 5 and altitude < 10:
    print('altitude in range 5-10')

# 5. Example of a Grading System
# Description: A grading system using if-elif-else based on score ranges.
# Example:

score = 85
if score >= 80:
    print("First Class")
elif score >= 70:
    print("Second Upper")
elif score >= 60:
    print("Second Lower")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
# 6. Ternary Operator
# Syntax:

# variable = expression1 if condition else expression2
# Description: A compact way of writing if-else statements.
# Example:

a = 9
b = 4
c = 1 if a < b else 5
print(c)  # Output: 5

