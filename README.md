# **Tabular PDF RAG Application**

This project is a **Retrieval-Augmented Generation (RAG) application** that extracts tabular data from PDF files and uses OpenAI's language models (e.g., GPT-3.5 or GPT-4) to answer natural language queries based on the extracted data. It leverages **Llama Index** for document storage and retrieval, and OpenAI's API for question answering.

## **Features**

- Upload PDF files with tables and automatically extract the tables.
- Query the extracted tables using OpenAI's GPT models.
- Receive natural language answers to your queries based on the ingested tabular data.

---

## **Prerequisites**

- **Python 3.11.9**: Ensure you are using Python version 3.11.9 for compatibility.
- **OpenAI API Key**: You need to sign up at [OpenAI Platform](https://platform.openai.com/signup) to get an API key.

---

## **Setup Instructions**

### **1. Clone the Repository**

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/freak360/rag.git
cd rag
```

2. Create a Python Virtual Environment
Create and activate a virtual environment to keep the dependencies isolated:

```bash

# On macOS/Linux
python3.11 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies
Install the required Python dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

4. Set Up OpenAI API Key
This application uses the OpenAI API to process queries. You need to create a .env file in the root directory of the project and add your OpenAI API key to it.

Create a file named .env in the root directory:

Add the following line to the .env file, replacing your_openai_api_key_here with your actual OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

**How to Run the Application**
After setting up the dependencies and API key, run the Streamlit application with the following command:

```bash
streamlit run app.py
```

This will start the app and open it in your default web browser. You will see an interface where you can upload a PDF file and ask questions about the tabular data it contains.

```bash
Project Structure

├── app.py              # Main application file
├── .env                # Environment file containing the OpenAI API key
├── requirements.txt     # File containing all the Python dependencies
├── README.md            # Project README file

```

**Dependencies**
The required Python packages for this project are listed in the requirements.txt file:

openai: To interact with OpenAI's GPT models.
llama-index: For document storage and retrieval.
streamlit: For building the app's web interface.
camelot-py: For extracting tables from PDFs.
PyPDF2: For reading PDF files.
python-dotenv: To load environment variables from a .env file.
pandas: To manage the extracted tabular data.

**Contributing**
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.

**License**
This project is open-source and available under the MIT License.

**Contact**
If you have any questions or suggestions, feel free to open an issue in the repository.
You can also contact me at: maneebajmal@gmail.com

## **Acknowledgements**
This project uses the following open-source tools and libraries:

1. **Streamlit:** For building interactive web applications.
2. **Llama Index:** For document ingestion and retrieval.
3. **OpenAI:** For the natural language understanding and generation capabilities.
4. **Camelot:** For PDF table extraction.
