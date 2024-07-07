"""Palindrome checker"""
from collections import deque

def is_palindrome(word: str) -> bool:
    """Checks if word is palindrome.
    
    Args:
        word: String that must be checked for palindrome.

    Returns:
        Boolean value that indicates either word is palindrome or not.
    """
    if not word:
        return False
    
    d = deque(word.lower())
    is_palindrome = False
    deque_length = len(d)

    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        is_palindrome = left == right

    return is_palindrome

print(is_palindrome('Pop'))
print(is_palindrome('Kayak'))
print(is_palindrome('Low'))
print(is_palindrome('Nano'))
print(is_palindrome('Peep'))
print(is_palindrome(''))
