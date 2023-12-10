import streamlit as st
import anon_ss
import k_anonymity
import request_data


def main():
    st.title("Privacy Analysis of FHIR Data")
    #st.header("Welcome. To start, select to load data from HAPI FHIR server or to upload FHIR Data in JSON format from your device")

    # User chooses data source
    data_source = st.radio("Welcome. To start, select to load data from HAPI FHIR server or to upload FHIR Data in JSON format from your device", ("HAPI Server", "Local device"))

    if data_source == "Local device":
        st.write("load_data_from_local()")
    elif data_source == "HAPI Server":
        # User inputs Server-URL, http://hapi.fhir.org/baseR4
        server_url = st.text_input("Server-URL", help="(z.B. www.example.com/fhir)", placeholder="http://hapi.fhir.org/baseR4")

        if st.button("Load Data"):
            if server_url:
                st.success("Data loaded.")
                # data = request_data.request_data(server_url)
            else:
                st.warning("Please enter HAPI Server URL.")

    # User multiselect metrics and, when k-anonymity is selected, qi
    st.sidebar.header("Choose privacy metrics, to apply and evaluate privacy (degree of anonymity) of the loaded FHIR data:")
    selected_metrics = st.sidebar.multiselect("Choose 1 or more privacy metrics:", ["k-anonymity", "Anonymity set size",])
    if "k-anonymity" in selected_metrics:
        selected_params = st.sidebar.multiselect("Choose 2 or more quasi identifierss:", ["birthDate", "gender", "postalCode"])

    # User starts evaluation
    if st.button("Evaluate privacy"):
        if not server_url:
            st.error("Error: No server URL defined")
        if "k-anonymity" not in selected_metrics and "Anonymity set size" in selected_metrics:
            data = request_data.request_data(server_url)
            res = anon_ss.anon_ss(data)
            st.write("Anonymity set size of the dataset is: ", res)
            st.write("Privacy metrics successfully applied, see results and evaluation below:")
            
            if anon_ss.anon_ss(data) > 1000:
                st.header("Privacy Score: 100")
            if 100 < anon_ss.anon_ss(data) < 1000:
                st.header("Privacy Score: 50")                
            
        if "k-anonymity" in selected_metrics and "Anonymity set size" not in selected_metrics and selected_params:
            data = request_data.request_data(server_url)
            qi_list = selected_params
            res = k_anonymity.k_anonymity(data, qi_list)
            st.write("k-anonymity of the dataset is: ", res)
            st.success("Privacy metrics successfully applied, see results and evaluation below:")
            
            if res > 10:
                st.write("Privacy Score: 100")
            if 0 < res < 10:
                st.write("Privacy Score: 50")         
        
        if "k-anonymity" in selected_metrics and "Anonymity set size" in selected_metrics and selected_params:
            data = request_data.request_data(server_url)
            qi_list = selected_params
            res_k_anon = k_anonymity.k_anonymity(data, qi_list)
            st.success("Privacy metrics successfully applied, see results and evaluation below:")
            st.write("k-anonymity of the dataset is: ", res_k_anon)
            
            res_ass = anon_ss.anon_ss(data)
            st.write("Anonymity set size of the dataset is: ", res_ass)            
            
            res_combined = res_k_anon + res_ass
            if res_combined > 10:
                st.write("Privacy Score: 100")
            if 0 < res_combined < 10:
                st.write("Privacy Score: 50")         

        else:
            st.warning("Please choose metrics and quasi identifiers.")

if __name__ == "__main__":
    main()