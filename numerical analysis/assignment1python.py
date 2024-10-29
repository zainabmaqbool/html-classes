def skip_elements(elements):
    result = []  # Create an empty list to store the skipped elements
    for index, value in enumerate(elements):
        if index % 2 == 0:  # Check if the index is even
            result.append(value)  # Append the element to the result list
    return result  # Return the list of skipped elements

# Test the function
print(skip_elements(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))