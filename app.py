import streamlit as st
st.set_page_config(page_title="ShipAI 🚢")
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.chains.question_answering import load_qa_chain
from pinecone import Pinecone
import os
from langchain_community.chat_models import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
import openai

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

def main():

    hf_api_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    pinecone_api_key = st.secrets["PINECONE_API_KEY"]
    pinecone_env = st.secrets["PINECONE_API_ENV"]

    #setting up UI
    st.header("Ask your AI ship mate 👨‍✈️🚢 ")

    index="shipdata"
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    
    loader = DirectoryLoader(f"content", loader_cls=PyPDFLoader, glob="./*.pdf", show_progress=True, use_multithreading=True)
    data = loader.load()
    text_splitter=CharacterTextSplitter(chunk_size=2000, chunk_overlap=200, separator="\n\n", length_function=len, add_start_index=True)
    docs=text_splitter.split_documents(data)

    # docsearch = PineconeVectorStore.from_texts([t.page_content for t in docs], embeddings, index_name="shipdata")
    # st.write('done')
    
    docsearch = PineconeVectorStore.from_existing_index(index, embeddings)

    #processing user query

    try:
        query = st.text_input("Ask a question here:")
        if query:
            docs=docsearch.similarity_search(query)

            llm=ChatOpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query, max_tokens=3500)          
                st.write(response)


    except openai.error.InvalidRequestError as e:
        st.error("An error occurred while processing your request. Please try again later.")
        st.write(f"Error details: {str(e)}")

if __name__ == '__main__':
     main()
