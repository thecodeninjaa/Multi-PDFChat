# Chat with Multiple PDFs

## Description

This project is a Streamlit application that allows users to interact with multiple PDF documents through a chat interface. It leverages Google Generative AI for conversational capabilities and includes user authentication.

## Features

- User authentication with hashed passwords.
- Upload and process multiple PDF documents.
- Extract text from PDFs and split it into manageable chunks.
- Engage in a conversation with the AI based on the content of the uploaded PDFs.

## Installation Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables in a `.env` file as needed (e.g., Google API keys).

## Usage

- Run the application:
  ```
  streamlit run app.py
  ```
- Log in using your credentials.
- Upload PDF documents and ask questions related to their content.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and submit a pull request.
