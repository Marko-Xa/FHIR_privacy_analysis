import requests
import json

def request_data(server_url):
    """
    Request FHIR data from the server.

    This function retrieves JSON data with a specific resource type (default: Patient) from a FHIR server.
    The server URL is provided as an input parameter.

    Parameters:
    - server_url (str): The URL of the FHIR server from which to request data.

    Returns:
    - dict: The FHIR data in JSON format.

    Example:
    fhir_data = request_data("http://hapi.fhir.org/baseR4")
    """
    # Server URL will depend on user input - see module streamlit_app.py
    # Example server_url = "http://hapi.fhir.org/baseR4"
 
    # Resource Type could be modified, but here patient is used for evaluation of the metrics
    resource_type = "Patient"
    
    response = requests.get(f"{server_url}/{resource_type}?gender:missing=false&birthdate:missing=false&address-postalcode:missing=false")

    if response.status_code == 200:
        # Successful request
        fhir_data = response.json()
    else:
        print("Error:", response.status_code)

    # For testing: Save json file, to use it in the upload function  
    save_file = open("FHIR_test_data.json", "w")  
    json.dump(fhir_data, save_file, indent=2)  
    save_file.close()  

    return fhir_data

    # For testing
    # print(type(fhir_data))
    # print(json.dumps(fhir_data, indent=2))
    # ?_count=X limitation for testing
