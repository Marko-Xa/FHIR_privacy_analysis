import requests
import json

def request_data(server_url):
    """Request FHIR data from server

    Retrieve JSON data with a specific resource type from a server, depending on user input.
    """

    # Server URL and Resource Type will depend on user input
    # server_url = "http://hapi.fhir.org/baseR4"
    resource_type = "Patient"
    
    # ?_count: X limitation for testing
    response = requests.get(f"{server_url}/{resource_type}?gender:missing=false&birthdate:missing=false&address-postalcode:missing=false")

    if response.status_code == 200:
        # Successful request
        fhir_data = response.json()
        # For testing
        print(json.dumps(fhir_data, indent=2))
    else:
        print("Error:", response.status_code)

    return fhir_data


