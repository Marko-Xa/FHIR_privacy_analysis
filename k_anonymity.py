import request_data
import json_extract

def k_anonymity():
    """ Calculate k-anonymity with the extracted values, depends on selection of quasi identificators (keys).

    This function extracts the specific quasi-identificators, which are selected by the user and creates a dictionary with them. 
    Then the function returns the k-anonymity degree of the values in the dictionary.
    """

    fhir_data = request_data.request_data()

    # Quasi-identifiers will depend on user input
    qi = ["birthDate", "gender"]

    #extract values from fhir_data with keys qi
    qi_data = {}
    for x in qi:
            qi_data[x] = json_extract.json_extract(fhir_data, x)

    # Create tuples
    qi_tuples = list(zip(qi_data['birthDate'], qi_data['gender']))
    
    # Count the frequency of each unique tuple (record)
    record_counts = {}
    for record in qi_tuples:
        if record in record_counts:
            record_counts[record] += 1
        else:
            record_counts[record] = 1
    #print(record_counts)
    
    k = min(list(record_counts.values()))
    print(k)

    # Check if k-anonymity is satisfied (will depend from user input)



    
    # For testing
    # print(qi_tuples)