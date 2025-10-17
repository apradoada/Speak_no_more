import time
import sys

def type_text(text, delay=0.025):
    """Prints text one character at a time with a specified delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures the character is printed immediately
        time.sleep(delay)
    print()