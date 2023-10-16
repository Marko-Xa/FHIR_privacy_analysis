import requests
import json

def request_data():
    """Request FHIR data from server

    Retrieve JSON data with a specific resource type from a server, depending on user input.
    """

    # Server URL and Resource Type will depend on user input
    server_url = "https://mii-agiop-3p.life.uni-leipzig.de/fhir/"
    resource_type = "Patient"
    
    # ?_count: 10 limitation for testing
    response = requests.get(f"{server_url}/{resource_type}?_count=200")

    if response.status_code == 200:
        # Successful request
        fhir_data = response.json()
        # For testing
        #print(json.dumps(fhir_data, indent=2))
    else:
        print("Error:", response.status_code)

    return fhir_data



#params = {
#   "_count": 10,
#    "_elements": "id, gender, birthDate"
#}

#payload = {'id': "Polar-WP1.1-00012","_count": 10}

#record_id = "Polar-WP1.1-00029"

#response = requests.get(f"{server_url}/{resource_type}", params=payload)
#response = requests.get(f"{server_url}/{resource_type}/{record_id}")

