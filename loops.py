# Loops in Python

# `for` Loops
# - `for` loops are used to iterate over sequences (e.g., lists, tuples, strings).
# - The `for` loop goes through each item in the sequence, performing operations defined within the loop block.

# Example Syntax:
# for item in sequence:
#     # Perform actions with each `item`

# Range Function
# - The `range()` function generates a sequence of numbers, useful for iterating a set number of times.
# - `range(start, stop, step)` defines the start, end, and step size of the sequence.
#   - `start` is the first number (inclusive).
#   - `stop` is the end of the sequence (exclusive).
#   - `step` is the amount by which to increment (default is 1).

# `while` Loops
# - `while` loops are used when the number of iterations isn’t known in advance.
# - The loop will continue running as long as the specified condition evaluates to `True`.
# - Be cautious with `while` loops, as improper conditions can lead to infinite loops.

# Example Syntax:
# while condition:
#     # Code to execute as long as `condition` is True

# Flow Control: `break` and `continue`
# - `break`: Immediately exits the loop, skipping the remaining code and preventing further iterations.
# - `continue`: Skips the current iteration and proceeds to the next iteration without exiting the loop.

# Example Use Case:
# - `break` can be used to exit a loop after a specific condition is met.
# - `continue` can be used to skip unwanted values and continue with the next loop iteration.

# Nested Loop Example: Password Attempts
# - This setup allows repeated password attempts, breaking the loop if the correct password is entered or a maximum number of tries is reached.
# - `True` creates an infinite loop, which will break when certain conditions are met.

# Looping and Conditionals Summary
# - `for` loops and `while` loops allow repetitive tasks until a condition changes.
# - Control statements like `break` and `continue` give flexibility in managing the flow within loops.
