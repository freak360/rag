import streamlit as st
import PyPDF2
import camelot
from llama_index.core import VectorStoreIndex, Document
from llama_index.embeddings.openai import OpenAIEmbedding
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to extract tables from the PDF
def extract_tables_from_pdf(pdf_file_path):
    # Using PyPDF2 to get number of pages
    pdf_reader = PyPDF2.PdfReader(open(pdf_file_path, 'rb'))
    num_pages = len(pdf_reader.pages)

    # Using Camelot for table extraction
    tables = []
    for page_num in range(num_pages):
        tables_on_page = camelot.read_pdf(pdf_file_path, pages=str(page_num + 1), flavor='stream')
        tables.extend(tables_on_page)

    return tables

# Function to clean and return the tables as pandas DataFrames
def clean_tables(tables):
    cleaned_tables = []
    for table in tables:
        df = table.df  # Extract table data as pandas DataFrame
        cleaned_tables.append(df)
    return cleaned_tables

# Function to ingest the tables into Llama Index using OpenAI embeddings
def ingest_tables_into_llama_index(tables):
    # Convert each table to a Document object for Llama Index ingestion
    documents = []
    for table in tables:
        table_str = table.to_string(index=False)  # Convert table to string
        documents.append(Document(text=table_str))  # Create Document object

    # Set up OpenAI embeddings
    embed_model = OpenAIEmbedding()

    # Create the index from Document objects using OpenAI embedding model
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    return index

# Function to query the index and get the response text
def query_index(index, query_text):
    # Create a query engine from the index using the specified LLM model
    query_engine = index.as_query_engine()

    # Run the query and return the full response text
    response = query_engine.query(query_text)
    return response.response  # Return the full response text

# Streamlit App
st.title("RAG Application for Tabular PDF Ingestion")

# Upload the PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file
    with open("uploaded_pdf.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing the PDF to extract tables...")
    
    # Extract and clean tables from the PDF
    tables = extract_tables_from_pdf("uploaded_pdf.pdf")
    cleaned_tables = clean_tables(tables)

    # Display the extracted tables
    st.write("Extracted Tables:")
    for idx, table in enumerate(cleaned_tables):
        st.write(f"Table {idx + 1}")
        st.dataframe(table)

    # Ingest the cleaned tables into Llama Index
    index = ingest_tables_into_llama_index(cleaned_tables)
    
    # Provide a query interface for the user
    query_text = st.text_input("Ask a question about the tables:")

    if query_text:
        # Query the index and display the full response text
        response_text = query_index(index, query_text)
        st.write("Response:")
        st.write(response_text)
