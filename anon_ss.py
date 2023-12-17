import json_extract

def anon_ss(data):
    """Calculate Anonymity Set Size of the requested bundle.

    This function extracts the patient ids in the response bundle and counts unique ids.

    Parameters:
    - data (dict): The FHIR bundle data.

    Returns:
    - int: Anonymity Set Size, i.e., the count of unique patient ids.
    """
    # Extract patient ids from the response bundle
    ids = json_extract.json_extract(data, "id")

    # Remove duplicates by converting the list to a set
    unique_ids = set(ids)    
    
    # Print and return the Anonymity Set Size
    print("Anonymity Set Size: ", len(unique_ids))
    return len(unique_ids)

    # For testing
    # print(ids)