def json_extract(data, key):
    """
    Extract values from a FHIR Bundle for a specified key.

    This function iterates through each record in the FHIR Bundle and extracts values associated with the specified key.
    If the key is "postalCode," it navigates through nested structures to retrieve the postal code.
    The extracted values are returned as a list.

    Parameters:
    - data (dict): The FHIR Bundle or dictionary containing patient records.
    - key (str): The key for which values need to be extracted.

    Returns:
    - list: A list containing extracted values associated with the specified key.
    """
    # Initialize an empty list to store the extracted values
    result = []

    # Iterate through each record in the data dictionary (assuming it represents a FHIR Bundle)
    for record in data.get("entry", []):  # Iterate through each record in the Bundle
        # Check if the current record is a dictionary
        if isinstance(record, dict):  # Check if record is a dictionary 
            # Check if the key is "postalCode" (special handling for this key)
            if key == "postalCode":
                # Extract the value associated with the "postalCode" key from the nested structure
        
                # Navigate through the nested structure:
                #   1. Get the "resource" dictionary from the current record
                #   2. From the "resource" dictionary, get the "address" list (default to [{}] if not present)
                #   3. Take the first element [0] from the "address" list (if it exists)
                #   4. Finally, get the value associated with the "postalCode" key
                result.append(record.get("resource", {}).get("address", [{}])[0].get(key))
            else:
                # For other keys, extract the value directly from the "resource" dictionary
                
                # Navigate through the nested structure:
                #   1. Get the "resource" dictionary from the current record
                #   2. Finally, get the value associated with the specified key
                result.append(record.get("resource", {}).get(key))
    
    # Return the list of extracted values
    return result

    # For testing
    # print(result)