import streamlit as st
st.set_page_config(page_title="ShipAI")
import os
from typing import Optional
from streamlit.errors import StreamlitSecretNotFoundError
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI


def _get_setting(key: str, default: Optional[str] = None) -> Optional[str]:
    try:
        if key in st.secrets:
            return st.secrets[key]
    except StreamlitSecretNotFoundError:
        pass
    return os.getenv(key, default)

def main():

    load_dotenv()

    hf_api_token = _get_setting("HUGGINGFACEHUB_API_TOKEN")
    google_api_key = _get_setting("GOOGLE_API_KEY")
    pinecone_api_key = _get_setting("PINECONE_API_KEY")
    pinecone_env = _get_setting("PINECONE_API_ENV")
    index = _get_setting("SHIPAI_INDEX_NAME", "shipdata")

    required_settings = {
        "HUGGINGFACEHUB_API_TOKEN": hf_api_token,
        "GOOGLE_API_KEY": google_api_key,
        "PINECONE_API_KEY": pinecone_api_key,
        "PINECONE_API_ENV": pinecone_env,
    }
    missing = [name for name, value in required_settings.items() if not value]

    if missing:
        st.error(
            "Missing required configuration: "
            + ", ".join(missing)
            + ". Add them in Streamlit secrets for deployment or in a local .env file."
        )
        st.stop()

    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_token
    os.environ["PINECONE_API_KEY"] = pinecone_api_key
    os.environ["PINECONE_API_ENV"] = pinecone_env
    os.environ["PINECONE_ENVIRONMENT"] = pinecone_env

    #setting up UI
    st.header("Ask your AI ship mate")

    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    docsearch = PineconeVectorStore.from_existing_index(index_name=index, embedding=embeddings)

    #processing user query
    try:
        query = st.text_input("Ask a question here:")
        if query:
            docs=docsearch.similarity_search(query)

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=google_api_key,
                temperature=0.2,
            )
            context = "\n\n".join(doc.page_content for doc in docs[:4])
            prompt = (
                "You are a maritime assistant. Answer using only the context below. Do not add non-relevant information"
                "If the answer is not in the context, say you don't know.\n\n"
                f"Context:\n{context}\n\n"
                f"Question: {query}\n\n"
                "Answer:"
            )
            with st.spinner("Analyzing maritime records..."):
                response = llm.invoke(prompt)
                st.markdown(response.content)
    


    except Exception as e:
        st.error("An error occurred while processing your request. Please try again later.")
        st.write(f"Error details: {str(e)}")

if __name__ == '__main__':
     main()
