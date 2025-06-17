# Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.
# 🔁 Purpose:
# Create a decorator that measures how long a function takes to execute.
import time  # Import time module for timing functions


# ⏱️ Decorator Definition
def timer(func):
    """
    A decorator that measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function with arguments
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate duration
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # Return the function's original output
    return wrapper  # Return the inner wrapper function


# 🎯 Function to be timed (decorated using @timer)
@timer
def function_to_time(n):
    """
    Function that simulates a delay by sleeping for 'n' seconds.
    """
    time.sleep(n)


# 🚀 Call the decorated function
function_to_time(2)  # This will sleep for 2 seconds and show the execution time


# Decorator (@timer)
# Function wrapping with *args, **kwargs
# Measuring execution time using time.time()
# Using func.__name__ to get the function's name
# Clean documentation and structure






