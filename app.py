import streamlit as st
st.set_page_config(page_title="ShipAI 🚢")
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os

from huggingface_hub import hf_hub_download
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub 
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

def main():

    os.environ["HUGGINGFACEHUB_API_TOKEN"]=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
    os.environ["OPENAI_API_KEY"]=st.secrets["OPENAI_API_KEY"]

    #setting up UI
    st.header("Ask your AI ship mate 👨‍✈️🚢 ")


    #set up environment
    PINECONE_API_KEY =  '6844b37a-39b9-4ec6-96c4-94c2d1d1d9ec'
    PINECONE_API_ENV = 'gcp-starter'


    #pinecone for vector database
    pinecone.init(
        api_key=PINECONE_API_KEY,  
        environment=PINECONE_API_ENV  
    )
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    index_name="shipdata"

    #docsearch=Pinecone.from_texts([t.page_content for t in docs], embeddings, index_name=index_name)
    docsearch = Pinecone.from_existing_index(index_name, embeddings)

    #processing user query
    try:
        query = st.text_input("Ask a question here:")
        if query:
            docs=docsearch.similarity_search(query)

            llm=ChatOpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query, max_tokens=4090)          
                st.write(response)


    except openai.error as e:
        st.error("An error occurred while processing your request. Please try again later.")
        st.write(f"Error details: {str(e)}")

if __name__ == '__main__':
     main()
