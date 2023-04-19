# lovematch

The `lovematch` library is a Python package that allows you to calculate friendship and love match percentages between given names.

## Installation

You can install `lovematch` using pip, the Python package manager:

```bash
pip install lovematch

## Usage
### You can use lovematch in your Python code as follows:

```python
from lovematch.friendship import calculate_frindship_match_percentage
from lovematch.love import calculate_love_match_percentage

# Calculate friendship match percentage
your_name = "Alice"
friend_name = "Bob"
friendship_percentage = calculate_frindship_match_percentage(your_name, friend_name)
print(f"Friendship match percentage between {your_name} and {friend_name}: {friendship_percentage}")

# Calculate love match percentage
your_name = "Alice"
partner_name = "Bob"
love_percentage = calculate_love_match_percentage(your_name, partner_name)
print(f"Love match percentage between {your_name} and {partner_name}: {love_percentage}")
```

