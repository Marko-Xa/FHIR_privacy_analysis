def json_extract(obj, key):
    """
    Extract values from nested JSON by key.

    Parameters:
        obj (dict or list): The nested JSON object to search.
        key (str): The key to search for in the nested JSON.

    Returns:
        list: A list of values corresponding to the specified key.
    """
    # Initialize an empty list to store the extracted values
    result = []

    def extract(obj, key):
        """
        Recursively traverse the nested JSON to extract values by key.

        Parameters:
            obj (dict or list): The current level of the nested JSON.
            key (str): The key to search for in the current level.

        This function modifies the 'result' list.
        """
        if isinstance(obj, dict):
            # If the current object is a dictionary, iterate through its key-value pairs
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    # If the value is a nested dictionary or list, recurse into it
                    extract(v, key)
                elif k == key:
                    # If the key matches the desired key, append the corresponding value to 'result'
                    result.append(v)
        elif isinstance(obj, list):
            # If the current object is a list, iterate through its items
            for item in obj:
                # Recurse into each item in the list
                extract(item, key)

    # Start the extraction process
    extract(obj, key)
    
    # Return the final list of extracted values
    return result