# Python Coding Standard

## 1. Naming Conventions

### 1.1 General Naming Rules

- Use clear, descriptive names that convey the purpose of the variable, function, or class
- Prefer readability over brevity
- Avoid single-letter variable names except for very short loop counters or mathematical contexts

### 1.2 Variable Names

- Use lowercase with underscores for variable names (snake_case)
- Examples:

  ```python
  user_name = "John Doe"
  total_count = 42
  ```

### 1.3 Function Names

- Use lowercase with underscores (snake_case)
- Verb or verb phrase describing the action
- Prefix with underscore for private/internal functions
- Examples:

  ```python
  def calculate_total_price(items):
      pass
  
  def validate_user_input(input_string):
      pass
  ```

### 1.4 Class Names

- Use CamelCase (CapWords)
- Nouns or noun phrases
- Examples:

  ```python
  class UserAuthentication:
      pass
  
  class DatabaseConnection:
      pass
  ```

### 1.5 Constants

- Use uppercase with underscores
- Examples:

  ```python
  MAX_CONNECTIONS = 100
  DEFAULT_TIMEOUT = 30
  ```

### 1.6 Private/Internal Variables and Methods

- Prefix with single underscore for internal use
- Examples:

  ```python
  class DataProcessor:
      def __init__(self):
          self._internal_cache = {}
      
      def _prepare_data(self):
          pass
  ```

## 2. Formatting Standards

### 2.1 Indentation

- Use 4 spaces per indentation level
- Never use tabs
- Consistent indentation throughout the project

### 2.2 Line Length

- Maximum line length: 88 characters (follows Black formatter recommendation)
- Use line breaks and parentheses for long lines
- Example:

  ```python
  long_function_call = some_function(
      argument1, 
      argument2, 
      argument3
  )
  ```

### 2.3 Whitespace

- Two blank lines between top-level classes and functions
- One blank line between methods in a class
- No extra whitespace inside parentheses, brackets, or braces
- Example:

  ```python
  def function1():
      pass


  def function2():
      pass
  ```

### 2.4 Imports

- Imports at the top of the file
- Grouped in order:
  1. Standard library imports
  2. Third-party library imports
  3. Local application/library specific imports
- Alphabetically ordered within each group
- Example:

  ```python
  import os
  import sys

  import numpy as np
  import pandas as pd

  from myproject import custom_module
  ```

## 3. Code Structure Standards

### 3.1 Function Design

- Each function should do one thing well
- Keep functions short (preferably under 20-25 lines)
- Use docstrings for all public functions
- Example:

  ```python
  def calculate_average(numbers):
      """
      Calculate the arithmetic mean of a list of numbers.
      
      Args:
          numbers (list): A list of numeric values
      
      Returns:
          float: The arithmetic mean of the input list
      """
      if not numbers:
          return 0
      return sum(numbers) / len(numbers)
  ```

### 3.2 Error Handling

- Use specific exceptions
- Provide meaningful error messages
- Use context managers for resource handling
- Example:

  ```python
  try:
      with open('file.txt', 'r') as file:
          content = file.read()
  except FileNotFoundError:
      logging.error("File not found")
  except PermissionError:
      logging.error("Permission denied")
  ```

### 3.3 Type Hinting

- Use type hints for function parameters and return values
- Example:

  ```python
  def process_data(input_list: List[int]) -> Dict[str, int]:
      result = {}
      for item in input_list:
          # Processing logic
      return result
  ```

### 3.4 Comments and Documentation

- Use comments to explain complex logic
- Prefer self-documenting code over excessive comments
- Use docstrings for modules, classes, and functions
- Avoid commented-out code

### 3.5 Class Design

- Prefer composition over inheritance
- Follow SOLID principles
- Keep classes focused and cohesive
- Example:

  ```python
  class UserManager:
      def __init__(self, database):
          self.database = database
      
      def create_user(self, username, password):
          # Implementation
          pass
  ```

## 4. Best Practices

### 4.1 Performance and Efficiency

- Use list comprehensions over explicit loops when possible
- Prefer generator expressions for large datasets
- Use `__slots__` for classes with many instances

### 4.2 Security

- Avoid using `eval()` and `exec()`
- Sanitize and validate all user inputs
- Use environment variables for sensitive information

### 4.3 Testing

- Write unit tests for all functions and classes
- Aim for high test coverage
- Use pytest or unittest framework

## 5. Ordering Conventions

### 5.1 Module-Level Ordering

Organize the contents of Python modules in the following order:

1. Module docstring
2. Encoding declaration (if applicable)
3. Future imports
4. Standard library imports
5. Third-party library imports
6. Local application/library specific imports
7. Global constants
8. Module-level configurations
9. Main code (functions, classes)

Example:

```python
"""Module documentation describing the purpose of this module."""

# Encoding declaration (if needed)
# -*- coding: utf-8 -*-

# Future imports
from __future__ import annotations

# Standard library imports
import os
import sys
from typing import List, Dict

# Third-party imports
import numpy as np
import pandas as pd

# Local application imports
from myproject.utils import helper_functions

# Global constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Module-level configurations
logger = logging.getLogger(__name__)

# Main code
def main_function():
    pass

class PrimaryClass:
    pass
```

### 5.2 Class Attribute and Method Ordering

Within a class, organize members in the following sequence:

1. Class-level docstring
2. Class variables
3. Magic/Dunder methods (in a specific order)
4. `__init__` method
5. Class methods
6. Static methods
7. Instance methods
8. Private methods (prefixed with underscore)

Example:

```python
class DataProcessor:
    """Class documentation explaining the purpose of the class."""
    
    # Class variables
    MAX_BUFFER_SIZE = 1024
    _internal_config = {}
    
    # Magic/Dunder methods (in recommended order)
    def __new__(cls):
        # Object creation logic
        pass
    
    def __init__(self, config=None):
        self.config = config or {}
    
    def __str__(self):
        return f"DataProcessor({self.config})"
    
    def __repr__(self):
        return self.__str__()
    
    # Class methods
    @classmethod
    def from_config(cls, config):
        return cls(config)
    
    # Static methods
    @staticmethod
    def validate_data(data):
        # Validation logic
        pass
    
    # Public instance methods
    def process_data(self, data):
        # Processing logic
        pass
    
    def transform_data(self, data):
        # Transformation logic
        pass
    
    # Private methods
    def _prepare_data(self, data):
        # Internal preparation logic
        pass
```

### 5.3 Function Parameter Ordering

When defining functions, use the following parameter order:

1. Positional parameters
2. Positional-only parameters
3. Keyword parameters
4. Keyword-only parameters
5. Variable-length positional arguments (`*args`)
6. Variable-length keyword arguments (`**kwargs`)

Example:

```python
def complex_function(
    standard_param,            # Positional/keyword parameter
    /,                         # Positional-only marker
    positional_only,           # Positional-only parameter
    *,                         # Keyword-only marker
    keyword_only=None,         # Keyword-only parameter
    *args,                     # Variable positional arguments
    **kwargs                   # Variable keyword arguments
):
    pass
```

### 5.4 Import Ordering Within Groups

When organizing imports within each group (standard library, third-party, local), follow these guidelines:

- Alphabetical order
- Case-insensitive sorting
- Shorter import paths before longer ones

Example:

```python
# Standard library imports (alphabetical)
import abc
import collections
import datetime
import os
import sys

# Third-party imports (alphabetical)
import numpy as np
import pandas as pd
import scipy.stats as stats

# Local imports (alphabetical)
from myproject.data import processors
from myproject.utils import helpers
```

### 5.5 Dictionary and List Ordering

- For configuration dictionaries, place required or most frequently used items first
- For lists used as configuration, order by importance or frequency of use

Example:

```python
# Configuration dictionary with most critical items first
config = {
    'database': {
        'host': 'localhost',     # Most critical configuration
        'port': 5432,             # Secondary configuration
        'username': 'admin',      # Less critical
        'optional_settings': {}   # Optional settings last
    }
}

# List ordered by priority or frequency
processing_steps = [
    'validate_input',     # Always first
    'clean_data',         # High priority
    'transform_data',     # Medium priority
    'log_results'         # Lower priority
]
```

### 5.6 Exception Handling Order

When handling multiple exceptions, order them from most specific to most general:

```python
try:
    # Some potentially risky operation
    result = perform_operation()
except ValueError:           # Most specific exception
    handle_value_error()
except TypeError:            # Next most specific
    handle_type_error()
except RuntimeError:         # More general exception
    handle_runtime_error()
except Exception as e:       # Most general exception (catch-all)
    handle_generic_error(e)
```

## Appendix: Rationale for Ordering Conventions

The recommended ordering helps improve:

- Code readability
- Consistency across projects
- Easier navigation and understanding
- Predictable code structure
- Simplified maintenance
