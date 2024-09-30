Python provides a variety of built-in string methods that allow you to manipulate and interact with strings efficiently. Here’s a list of some commonly used string methods:

### Common String Methods

1. **`str.lower()`**: Converts all characters to lowercase.
   ```python
   "Hello".lower()  # Output: "hello"
   ```

2. **`str.upper()`**: Converts all characters to uppercase.
   ```python
   "Hello".upper()  # Output: "HELLO"
   ```

3. **`str.title()`**: Converts the first character of each word to uppercase.
   ```python
   "hello world".title()  # Output: "Hello World"
   ```

4. **`str.capitalize()`**: Capitalizes the first character of the string.
   ```python
   "hello world".capitalize()  # Output: "Hello world"
   ```

5. **`str.strip()`**: Removes leading and trailing whitespace.
   ```python
   "   Hello   ".strip()  # Output: "Hello"
   ```

6. **`str.split(separator)`**: Splits the string into a list based on a separator.
   ```python
   "a,b,c".split(",")  # Output: ['a', 'b', 'c']
   ```

7. **`str.join(iterable)`**: Joins elements of an iterable (like a list) into a single string with a specified separator.
   ```python
   ",".join(['a', 'b', 'c'])  # Output: "a,b,c"
   ```

8. **`str.replace(old, new)`**: Replaces occurrences of a substring with another substring.
   ```python
   "Hello World".replace("World", "Python")  # Output: "Hello Python"
   ```

9. **`str.find(substring)`**: Returns the lowest index of the substring if found, otherwise -1.
   ```python
   "Hello".find("e")  # Output: 1
   ```

10. **`str.count(substring)`**: Returns the number of occurrences of a substring.
    ```python
    "Hello".count("l")  # Output: 2
    ```

11. **`str.startswith(prefix)`**: Checks if the string starts with the specified prefix.
    ```python
    "Hello".startswith("He")  # Output: True
    ```

12. **`str.endswith(suffix)`**: Checks if the string ends with the specified suffix.
    ```python
    "Hello".endswith("lo")  # Output: True
    ```

13. **`str.isdigit()`**: Returns `True` if all characters in the string are digits.
    ```python
    "123".isdigit()  # Output: True
    ```

14. **`str.isalpha()`**: Returns `True` if all characters in the string are alphabetic.
    ```python
    "abc".isalpha()  # Output: True
    ```

15. **`str.isalnum()`**: Returns `True` if all characters are alphanumeric (letters and numbers).
    ```python
    "abc123".isalnum()  # Output: True
    ```

16. **`str.replace(old, new, count)`**: Replaces `count` occurrences of a substring.
    ```python
    "Hello Hello".replace("Hello", "Hi", 1)  # Output: "Hi Hello"
    ```

17. **`str.splitlines()`**: Splits the string at line breaks and returns a list of lines.
    ```python
    "Hello\nWorld".splitlines()  # Output: ['Hello', 'World']
    ```

### Example Usage

Here’s an example that demonstrates some of these methods:

```python
text = "  Hello, World!  "

# Using various string methods
print(text.lower())          # "  hello, world!  "
print(text.strip())         # "Hello, World!"
print(text.split(", "))     # ["  Hello", "World!  "]
print(text.replace("World", "Python"))  # "  Hello, Python!  "
print(text.count("o"))      # 2
