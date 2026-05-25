import os
import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient


AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")

# Create Search Client
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX_NAME,
    credential=AzureKeyCredential(AZURE_SEARCH_API_KEY)
)

st.title("Azure Search Portal")

# User Input
search_query = st.text_input("Enter your search query:", "how to start a birth case")

if st.button("Search"):
    if search_query:
        # Execute search query
        results = search_client.search(
            search_text=search_query,
            top=5
        )
        
        st.subheader("Results:")
        
        # Display results
        count = 0
        for result in results:
            count += 1
            with st.expander(f"Result {count}"):
                st.write(result)
    else:
        st.warning("Please enter a search term.")
