import streamlit as st
st.set_page_config(page_title="ShipAI 🚢")
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
# from pinecone Pinecone
import os

from huggingface_hub import hf_hub_download
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
import openai

def main():

    hf_api_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    pinecone_api_key = st.secrets["PINECONE_API_KEY"]
    pinecone_env = st.secrets["PINECONE_API_ENV"]

    #setting up UI
    st.header("Ask your AI ship mate 👨‍✈️🚢 ")

    st.write("Website is under maintenance due to Pinecone documentation changes. Thank you for your patience")

if __name__ == '__main__':
     main()
