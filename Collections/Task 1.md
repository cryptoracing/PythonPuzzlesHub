**Task:**

Write a function `check_list` that takes a variable `var` as input and checks if it is a list.

**Theory:**

To solve this task, you'll need to understand the basics of Python data types and specifically how to check the type of a variable. The `type()` function can be used to determine the type of a given variable.

**Solutions:**

**Solution 1:**
```python
def check_list(var):
    return type(var) == list
```
**Solution 2:**

```python
def check_list(var):
    return isinstance(var, list)
```
**Comparison:**

Both solutions achieve the same result, but there's a slight difference in implementation.

Solution 1 uses the `type()` function to directly compare the type of var with list.
Solution 2 utilizes `isinstance()` which not only checks if the variable is a list but also considers subclasses. In general, Solution 2 `(isinstance())` is considered more flexible as it allows for potential future changes in the class hierarchy.

**Additional Task:**

Write a function get_list_length that takes a list as input and returns the length of the list. Additionally, handle the case if the input is not a list by returning an appropriate message.
<details>
  <summary><b>Implementation:</b></summary>
	
```python
def get_list_length(input_list):
    if isinstance(input_list, list):
        return len(input_list)
    else:
        return "Input is not a list."
```
</details>
