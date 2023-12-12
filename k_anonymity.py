import json_extract

def k_anonymity(data, qi_list):
    """ Calculate k-anonymity with the extracted values, depends on selection of quasi identificators (keys).

    This function extracts the specific quasi-identificators, which are selected by the user and creates a dictionary with them. 
    Then the function calculates k-anonymity by counting the tuples of the values in the dictionary.
    """
    
    # Quasi-identifiers depend on user input
    # Example of qi_list = ["birthDate", "gender", "postalCode"]

    # Extract values from fhir_data with keys qi
    qi_data = {}
    for x in qi_list:
            qi_data[x] = json_extract.json_extract(data, x)
    # For testing
    # print(qi_data)

    # Create tuples of qi values
    qi_tuples = []

    if 'gender' in qi_list:
        qi_tuples.append(qi_data['gender'])

    if 'birthDate' in qi_list:
        qi_tuples.append(qi_data['birthDate'])

    if 'postalCode' in qi_list:
        qi_tuples.append(qi_data['postalCode'])

    # Ensure there is at least one qi in qi_list
    if qi_tuples:
        qi_tuples = list(zip(*qi_tuples))

    # For testing
    # print(qi_tuples)


    # Count the frequency of each unique tuple (record)
    record_counts = {}
    for record in qi_tuples:
        if record in record_counts:
            record_counts[record] += 1
        else:
            record_counts[record] = 1
    print(record_counts)
    records_counts_list  = list(record_counts.values())
    print(records_counts_list)
    k = ((min(records_counts_list)))
    
    print("k-anonymity:", k)

    return k



    
    # For testing
    # print(qi_tuples)