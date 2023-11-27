def validate(data):
    
    # Check if data is a list
    isList = isinstance(data, list)

    # Check if all elements in the list are either int or float
    areNumbers = True
    for num in data:
        # set to false if any do not match
        if not isinstance(num, (int, float)):
            areNumbers = False

    # Combine both conditions
    if not (isList and areNumbers):
        # return error if either condition is not met
        return False
    
    # Otherwise return True (valid input)
    return True