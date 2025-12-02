import os
import sys

"""

This is a custom exception handler that provides detailed error information including the exact file name, line number, 
and error message when something goes wrong in your code.

"""
def error_message_detail(error, error_detail:sys):
    """
    1. Extracts detailed error information from Python's traceback
    2. Returns a formatted string with file name, line number, and error message
    NOTE : Python's traceback is a detailed report that shows you exactly what went wrong when an error occurs in your code, 
    including the complete path the error took through your program. It is "breadcrumb trail" that helps you trace back to the source of the error.
    3. Where the error occurred (file name and line number)
    4. What functions were called leading up to the error
    5. Why the error happened (the actual error message)
    
    Why Tracebacks are Useful:
    6. Debugging: Find exactly where errors occur
    7. Understanding flow: See how your program got to the error
    8. Root cause: Identify the original source of problems
    9. Context: Understand what led to the error
    
    For Example:
    def divide_numbers(a, b):
        return a / b
        
    def calculate():
        result = divide_numbers(10, 0)  # This will cause an error
        return result
    calculate()
    
    How to Read a Traceback:
    1. "most recent call last" - Shows the chain of function calls
    2. File and line info - Tells you exactly where each step happened
    3. Function names - Shows which functions were involved
    4. Final error - The actual error type and message
    
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        
        1. A custom exception class that inherits from Python's base Exception
        2. Automatically formats error messages with detailed location info
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message