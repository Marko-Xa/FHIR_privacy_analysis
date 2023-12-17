import streamlit as st
import anon_ss
import k_anonymity
import request_data
import json

def main():
    st.set_page_config(
        page_title="Platform for evaluating privacy metrics on FHIR data sets",
        layout="centered",
    )
    st.title("Platform for evaluating privacy metrics on FHIR data sets")
    st.subheader("Welcome! How to use this platfom:")
    st.write("1. Select from loading data from HAPI FHIR server or uploading FHIR Data in JSON format from your device.")
    st.write("2. Select privacy metrics and, if available, parameters on the left sidebar.")
    st.write("3. Start the analysis with the button 'Evaluate privacy' to see the results.")
    st.write("")
    
    # User chooses data source
    data_source = st.radio("Select to load data from HAPI FHIR server or to upload FHIR Data in JSON format from your device", ("HAPI Server", "Local device"))
    st.write("")
    ########################################################
    # Upload JSON
    if data_source == "Local device":
        uploaded_file = st.file_uploader("Upload FHIR Data", help="FHIR Data in JSON Format")

        # User multiselect metrics and, if k-anonymity is selected, qi
        st.sidebar.header("Select privacy metrics, to apply and evaluate privacy (degree of anonymity) of the loaded FHIR data:")
        selected_metrics = st.sidebar.multiselect("Select one or more privacy metrics:", ["k-anonymity", "Anonymity set size",])
        if "k-anonymity" in selected_metrics:
            selected_params = st.sidebar.multiselect("Select one or more quasi identifier:", ["birthDate", "gender", "postalCode"])

        # User starts evaluation
        if st.button("Evaluate privacy"):
            if uploaded_file is not None:
                # User selects anonymity set size
                if "k-anonymity" not in selected_metrics and "Anonymity set size" in selected_metrics:
                    res = anon_ss.anon_ss(json.load(uploaded_file))
                    st.success("Privacy metrics successfully applied.")
                    st.metric(label = "Anonymity set size", value = res)                
                    st.info("The anonymity set for an individual u is the set of users that the adversary cannot distinguish from u. It can be seen as the size of the crowd into which the target u can blend. Thereby the size of the dataset can indicate the privacy level: If the dataset contains more records a target could be harder to identify than in a dataset with less records.")                    
                    # Calculate privacy score                    
                    if res > 1000:
                        score = 100
                    if 0 < res < 1000:
                        score = 50
                    st.success("Privacy score successfully calculated")
                    st.metric(label = "Privacy Score", value = score)    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')
                    
                # User selects k-anonymity
                if "k-anonymity" in selected_metrics and "Anonymity set size" not in selected_metrics:
                    if not selected_params:
                        st.warning("Please choose quasi identifiers for k-anonymity metric.")
                    qi_list = selected_params
                    res = k_anonymity.k_anonymity(json.load(uploaded_file), qi_list)
                    st.success("Privacy metrics successfully applied.")                
                    st.metric(label = "k-anonymity", value = res)
                    st.info("K-anonymity is a property of a dataset that indicates the re-identifiability of its records. A dataset is k-anonymous if quasi-identifiers for each person in the dataset are identical to at least k – 1 other people in the dataset.  Higher k means in general higher privacy.")                    
                    # Calculate privacy score                    
                    if res > 10:
                        score = 100
                    if 0 < res < 10:
                        score = 50
                    st.success("Privacy score successfully calculated")
                    st.metric(label = "Privacy Score", value = score)    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')

                # User selects k-anonymity and anonymity set size                
                if "k-anonymity" in selected_metrics and "Anonymity set size" in selected_metrics:
                    if not selected_params:
                        st.warning("Please choose quasi identifiers for k-anonymity metric.")
                    qi_list = selected_params
                    res_k_anon = k_anonymity.k_anonymity(json.load(uploaded_file), qi_list)
                    st.success("Privacy metrics successfully applied.")
                    st.metric(label = "k-anonymity", value = res_k_anon)
                    st.info("K-anonymity is a property of a dataset that indicates the re-identifiability of its records. A dataset is k-anonymous if quasi-identifiers for each person in the dataset are identical to at least k – 1 other people in the dataset.  Higher k means in general higher privacy.")                    
                    
                    res_ass = anon_ss.anon_ss(uploaded_file)
                    st.metric(label = "Anonymity set size", value = res_ass)                
                    st.info("The anonymity set for an individual u is the set of users that the adversary cannot distinguish from u. It can be seen as the size of the crowd into which the target u can blend. Thereby the size of the dataset can indicate the privacy level: If the dataset contains more records a target could be harder to identify than in a dataset with less records.")                    
                    # Calculate combined privacy score                                        
                    if res_k_anon <= 5:
                        k_score = 0
                    elif res_k_anon == 6:
                        k_score = 60
                    elif res_k_anon == 7:
                        k_score = 70
                    elif res_k_anon == 8:
                        k_score = 80
                    elif res_k_anon <= 9:
                        k_score = 90 
                    else:
                        k_score = 100    

                    if res_ass <= 50:
                        ass_score = 0
                    elif res_ass <= 60:
                        ass_score = 60
                    elif res_ass <= 70:
                        ass_score = 70
                    elif res_ass <= 80:
                        ass_score = 80
                    elif res_ass <= 90:
                        ass_score = 90 
                    else:
                        ass_score = 100    

                    score_combined = ((k_score + ass_score) / 2)

                    st.success("Privacy score successfully calculated.")
                    st.metric(label = "Privacy Score", value = (score_combined))    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')
                
                if not selected_metrics:
                    st.warning("Please choose metrics in the left sidebar.")

            else:
                st.error("Error: No File uploaded")        

    ########################################################
    # HAPI server 

    elif data_source == "HAPI Server":
        # User inputs Server-URL, e.g. http://hapi.fhir.org/baseR4
        server_url = st.text_input("Server-URL", help="(e.g.: http://hapi.fhir.org/baseR4", placeholder="http://hapi.fhir.org/baseR4")
        if st.button("Enter URL"):
            if server_url:
                st.success("Server-URL succesfully defined.")
                # data = request_data.request_data(server_url)
            else:
                st.warning("Please enter HAPI Server URL.")

        # User multiselect metrics and, if k-anonymity is selected, qi
        st.sidebar.header("Select privacy metrics, to apply and evaluate privacy (degree of anonymity) of the loaded FHIR data:")
        selected_metrics = st.sidebar.multiselect("Select one or more privacy metrics:", ["k-anonymity", "Anonymity set size",])
        if "k-anonymity" in selected_metrics:
            selected_params = st.sidebar.multiselect("Select one or more quasi identifier:", ["birthDate", "gender", "postalCode"])

        # User starts evaluation
        if st.button("Evaluate privacy"):
            if server_url:

                # User selected anonymity set size                    
                if "k-anonymity" not in selected_metrics and "Anonymity set size" in selected_metrics:
                    data = request_data.request_data(server_url)
                    res = anon_ss.anon_ss(data)
                    st.success("Privacy metrics successfully applied.")
                    st.metric(label = "Anonymity set size", value = res)                
                    st.info("The anonymity set for an individual u is the set of users that the adversary cannot distinguish from u. It can be seen as the size of the crowd into which the target u can blend. Thereby the size of the dataset can indicate the privacy level: If the dataset contains more records a target could be harder to identify than in a dataset with less records.")                    
                    # Calculate privacy score                                                            
                    if res > 1000:
                        score = 100
                    if 0 < res < 1000:
                        score = 50
                    st.success("Privacy score successfully calculated")
                    st.metric(label = "Privacy Score", value = score)    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')
                    
                # User selects k-anonymity
                if "k-anonymity" in selected_metrics and "Anonymity set size" not in selected_metrics:
                    if not selected_params:
                        st.warning("Please choose quasi identifiers for k-anonymity metric.")
                    data = request_data.request_data(server_url)
                    qi_list = selected_params
                    res = k_anonymity.k_anonymity(data, qi_list)
                    st.success("Privacy metrics successfully applied.")                
                    st.metric(label = "k-anonymity", value = res)
                    st.info("K-anonymity is a property of a dataset that indicates the re-identifiability of its records. A dataset is k-anonymous if quasi-identifiers for each person in the dataset are identical to at least k – 1 other people in the dataset.  Higher k means in general higher privacy.")                    
                    # Calculate privacy score                                                            
                    if res > 10:
                        score = 100
                    if 0 < res <= 10:
                        score = 50
                    st.success("Privacy score successfully calculated")
                    st.metric(label = "Privacy Score", value = score)    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')

                # User selects k-anonymity and anonymity set size
                if "k-anonymity" in selected_metrics and "Anonymity set size" in selected_metrics:
                    if not selected_params:
                        st.warning("Please choose quasi identifiers for k-anonymity metric.")
                    data = request_data.request_data(server_url)
                    qi_list = selected_params
                    res_k_anon = k_anonymity.k_anonymity(data, qi_list)
                    st.success("Privacy metrics successfully applied.")

                    st.metric(label = "k-anonymity", value = res_k_anon)
                    st.info("K-anonymity is a property of a dataset that indicates the re-identifiability of its records. A dataset is k-anonymous if quasi-identifiers for each person in the dataset are identical to at least k – 1 other people in the dataset.  Higher k means in general higher privacy.")                    
                    
                    res_ass = anon_ss.anon_ss(data)
                    st.metric(label = "Anonymity set size", value = res_ass)                
                    st.info("The anonymity set for an individual u is the set of users that the adversary cannot distinguish from u. It can be seen as the size of the crowd into which the target u can blend. Thereby the size of the dataset can indicate the privacy level: If the dataset contains more records a target could be harder to identify than in a dataset with less records.")                    
                    # Calculate combined privacy score                                        
                    if res_k_anon <= 5:
                        k_score = 0
                    elif res_k_anon == 6:
                        k_score = 60
                    elif res_k_anon == 7:
                        k_score = 70
                    elif res_k_anon == 8:
                        k_score = 80
                    elif res_k_anon <= 9:
                        k_score = 90 
                    else:
                        k_score = 100    

                    if res_ass <= 50:
                        ass_score = 0
                    elif res_ass <= 60:
                        ass_score = 60
                    elif res_ass <= 70:
                        ass_score = 70
                    elif res_ass <= 80:
                        ass_score = 80
                    elif res_ass <= 90:
                        ass_score = 90 
                    else:
                        ass_score = 100    

                    score_combined = ((k_score + ass_score) / 2)

                    st.success("Privacy score successfully calculated.")
                    st.metric(label = "Privacy Score", value = (score_combined))    
                    st.info('''
                            To improve the privacy score consider the following anonymization techniques:\n                          
                            Data Aggregation: Combine data into summary statistics or categories, instead of individual records.\n
                            Generalization: Replace specific values with broader categories, like using age groups instead of exact birthdates or ZIP codes instead of precise addresses.\n
                            Adding Noise: Introduce random data or slightly distort values to make it harder to identify individuals.\n
                            Pseudonymization: Replace personally identifiable data with pseudonymous values.''')
                
                if not selected_metrics:
                    st.warning("Please select metrics in the left sidebar.")

            else:
                st.error("Error: No server URL defined")

if __name__ == "__main__":
    main()

    