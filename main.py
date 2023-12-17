import k_anonymity
import anon_ss
import request_data

def main():
    # For testing
    data = request_data.request_data("http://hapi.fhir.org/baseR4")
    qi_list = ["birthDate", "gender", "postalCode"]
    k_anonymity.k_anonymity(data, qi_list)
    anon_ss.anon_ss(data)
    print("Calculations done.")
    
if __name__ == "__main__":
    main()