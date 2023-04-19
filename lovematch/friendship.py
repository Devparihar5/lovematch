import collections

def calculate_frindship_match_percentage(your_name, friend_name):
    """
    Calculate friendship match percentage between given names.
    
    Args:
        your_name (str): Your name.
        friend_name (str): Friend's name.
    
    Returns:
        str: Friendship match percentage as a string.
    """
    # Concatenate the names with "friendship" in between
    thestring = your_name + "friendship" + friend_name

    # Create a dictionary to store letter occurrences
    d = collections.defaultdict(int)

    # Count occurrences of each letter in the combined string
    for c in thestring:
        d[c] += 1

    # Extract the values (letter occurrences) from the dictionary and convert them to a list
    a = list(d.values())

    # Loop until there are only two values in the list
    while len(a) > 2:
        b = []  # Create a new list to store updated values

        # Iterate through the list and calculate updated values
        for x, y in enumerate(a):
            b = b + list(map(int, str(a[len(a) - 1 - x] + y)))  # Add updated value to the new list
            if x + 1 == int(len(a) / 2):  # Break loop when halfway through the list
                if len(a) % 2 != 0:  # If the list length is odd, add the second-to-last value
                    b.append(a[len(a) - 2 - x])
                break

        a = b  # Update the list with the new values

    result = (map(str, a))
    return "".join(result) + '%'  # Return the final friendship match percentage as a string