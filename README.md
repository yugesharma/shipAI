ShipAI 🚢
<div align="center">
 <a href="https://shipai.streamlit.app">
  <img src="https://github.com/yugesharma/shipAI/blob/main/shipai.png" />
 </a>
</div>


ShipAI is an advanced AI-driven solution designed to empower you with maritime knowledge. Whether you have questions about SOLAS, MARPOL, or any topic within the maritime domain, ShipAI harnesses the capabilities of vector databases, embeddings, transformers, and Google Gemini to deliver accurate and insightful answers, making maritime exploration more accessible and efficient.

   Introduction
   Demo
   Features
   Getting Started
       Prerequisites
       Installation
   Usage
   Contributing
   License

# Introduction

The maritime domain is vast and complex, and extracting information from it can be challenging. ShipAI simplifies this process by allowing you to ask questions about plethora of regulations, resulting in saving time and it provides you with relevant answers.


# Demo

<div align="center">
  <img src="https://github.com/yugesharma/shipAI/blob/main/shipai.gif" width="1000" height="600"/>
</div>


<a href='https://shipai.streamlit.app'>Link to web app<a>



# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

   Python 3.10 or higher installed.
   A Pinecone API key and environment setup.
   Necessary secrets for Hugging Face and Google Gemini APIs.

## Installation

Follow these steps to set up ShipAI on your local machine:

  1. Clone the repository:

   ```bash
git clone https://github.com/yourusername/ShipAI.git
cd ShipAI
```

 2. Create a virtual environment and activate it:

```python

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

 3. Install the required packages:

```python

pip install -r requirements.txt
```

 4. Set environment variables for local runs:

Create a `.env` file in the project root with:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token
GOOGLE_API_KEY=your_google_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_API_ENV=your_pinecone_environment
SHIPAI_INDEX_NAME=shipdata
```

For deployed runs on Streamlit Cloud, set the same keys in app secrets (`.streamlit/secrets.toml` in the app settings).
    

# Usage

   1. Run the application:

  ```python

  streamlit run app.py
  ```

   2. Access the application in your web browser.

   3. Enter your questions related to the maritime domain in the provided text input.

   4. ShipAI will process your question, search the vector database, and provide you with answers and insights.

# Local + Deployment Consistency

Use this checklist to keep behavior identical in both environments:

1. Use the same Python version locally and in deployment (recommended: 3.10).
2. Keep one dependency source of truth: `requirements.txt`.
3. Keep one app entrypoint everywhere: `streamlit run app.py`.
4. Use the same config keys in both places:
   `HUGGINGFACEHUB_API_TOKEN`, `GOOGLE_API_KEY`, `PINECONE_API_KEY`, `PINECONE_API_ENV`, `SHIPAI_INDEX_NAME`.
5. Point both environments to the same Pinecone index name unless you intentionally isolate environments.

# Contributing

Contributions are welcome! If you want to contribute to ShipAI, please follow these steps:

  1.  Fork the repository.
  2.  Create a new branch: git checkout -b feature/new-feature.
  3.  Make your changes and commit them: git commit -m 'Add new feature'.
  4.  Push to the branch: git push origin feature/new-feature.
  5.  Submit a pull request.

# License

This project is licensed under the MIT License
