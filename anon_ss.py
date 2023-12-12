import json_extract

def anon_ss(data):
    """ Calculate Anonymity Set Size of the requested bundle.

    This function extracts the patient ids in the response bundle and counts unique ids.
    """
    ids = []
    ids = json_extract.json_extract(data, "id")
    
    # Remove (longer) bundle id 
    for x in ids:
        if len(x) > 10:
            ids.remove(x)

    # Remove duplicates 
    unique_ids = set(ids)    
    
    print("Anonymity Set Size: ", len(unique_ids))
    return(len(unique_ids))

    # For testing
    # print(ids)