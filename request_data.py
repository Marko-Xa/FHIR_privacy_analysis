import requests
import json

def request_data(server_url):
    """Request FHIR data from server

    Retrieve JSON data with a specific resource type from a server, depending on user input.
    """

    # Server URL will depend on user input - see module streamlit_app.py
    # server_url = "http://hapi.fhir.org/baseR4"
 
    # Resource Type could be modified, but here patient is used for evaluation of the metrics
    resource_type = "Patient"
    
    # ?_count: X limitation for testing
    response = requests.get(f"{server_url}/{resource_type}?gender:missing=false&birthdate:missing=false&address-postalcode:missing=false")

    if response.status_code == 200:
        # Successful request
        fhir_data = response.json()
        # For testing
        # print(type(fhir_data))

        #print(json.dumps(fhir_data, indent=2))
    else:
        print("Error:", response.status_code)


    # For testing: Save json file, to use it in upload function  
    save_file = open("saved_test_data.json", "w")  
    json.dump(fhir_data, save_file, indent=2)  
    save_file.close()  

    return fhir_data


