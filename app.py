import streamlit as st
import streamlit_authenticator as sauth
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from htmlTemplates import css, bot_template, user_template

# Authentication imports
import pickle
from pathlib import Path
import streamlit_authenticator as sauth


st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

# --- User authentication ---
names = ["Atharva Herekar", "Kartavya Gore", "Neeraj Gaikwad"]
usernames = ["athrv", "krtvya", "nrj"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with open(file_path, "rb") as f:
    hashed_passwords = pickle.load(f)

authenticator = sauth.Authenticate(names, usernames, hashed_passwords, "Chat","abcdef", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login","main")

if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.error("Please enter your username and password to login")

if authentication_status:



    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

    def get_pdf_text(pdf_docs):
        """Extract text from PDFs, ensuring no NoneType errors."""
        text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += (page.extract_text() or "")  #Prevents NoneType errors
        return text

    def get_text_chunks(text):
        """Split text into chunks for processing."""
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        return text_splitter.split_text(text)

    def get_vectorstore(text_chunks):
        """Convert text chunks into a FAISS vector store."""
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        return FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    def get_conversation_chain(vectorstore):
        """Create a conversation chain with memory."""
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, google_api_key=GOOGLE_API_KEY)
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        return ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )

    def handle_userinput(user_question):
        """Handle user questions by retrieving responses from the conversation chain."""
        if st.session_state.conversation is None:
            st.warning("Please upload and process a PDF first!")
            return

        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            template = user_template if i % 2 == 0 else bot_template
            st.write(template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    # Main app logic (only runs if user is authenticated)
    def main():
        #st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
        st.write(css, unsafe_allow_html=True)

        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

        st.header("Chat with multiple PDFs :books:")
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            handle_userinput(user_question)

        with st.sidebar:
            authenticator.logout("Logout","sidebar")
            st.sidebar.title(f"Welcome {name}")
            st.subheader("Your documents")
            pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)

            if st.button("Process"):
                if not pdf_docs:
                    st.error("Please upload at least one PDF.")   # Prevents errors if no file is uploaded
                else:
                    with st.spinner("Processing..."):
                        raw_text = get_pdf_text(pdf_docs)
                        text_chunks = get_text_chunks(raw_text)
                        vectorstore = get_vectorstore(text_chunks)
                        st.session_state.conversation = get_conversation_chain(vectorstore)
                        st.success("Processing complete! You can now ask questions.")

    if __name__ == "__main__":
        main()
