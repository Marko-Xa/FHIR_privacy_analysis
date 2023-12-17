import json_extract

def k_anonymity(data, qi_list):
    """
    Calculate k-anonymity for a given dataset based on quasi-identifiers.

    Parameters:
    - data (dict): The dataset, assumed to be in FHIR format.
    - qi_list (list): List of quasi-identifiers (qi) for k-anonymity calculation.
    - Quasi-identifiers depend on user selection in the streamlit dashboard 

    Returns:
    - k (int): The k-anonymity value for the dataset.

    Example:
    k_anonymity(fhir_data, ["birthDate", "gender", "postalCode"])
    """

    # Extract values from fhir_data with keys in qi_list
    qi_data = {}
    for qi_key in qi_list:
        qi_data[qi_key] = json_extract.json_extract(data, qi_key)
    # Create tuples that contain lists of the qi values
    qi_tuples = []
    # Check for each quasi-identifier in qi_list and append its values to qi_tuples
    for qi_key in qi_list:
        if qi_key in qi_data:
            qi_tuples.append(qi_data[qi_key])
    # Ensure there is at least one quasi-identifier in qi_list
    if qi_tuples:
        # Transpose the list of tuples to get a list of records
        qi_tuples = list(zip(*qi_tuples))
    # Count the frequency of each unique tuple (record)
    record_counts = {}
    # Iterate through each record in qi_tuples
    for record in qi_tuples:
        if record in record_counts:
            # If the record is already in the dictionary, increment its count
            record_counts[record] += 1
        else:
            # If the record is not in the dictionary, add it with a count of 1
            record_counts[record] = 1


    # Convert the counts to a list for further analysis
    records_counts_list = list(record_counts.values())
    
    # Calculate k-anonymity as the minimum frequency of a unique tuple
    k = min(records_counts_list)
    print("k-anonymity:", k)
    return k


    # For testing
    # print(qi_data)
    # print(qi_tuples)
    # print(records_counts_list)
    # print(record_counts)
