ShipAI 🚢
<div align="center">
 <a href="https://shipai.streamlit.app">
  <img src="https://github.com/yugesharma/shipAI/blob/main/shipai.png" />
 </a>
</div>


ShipAI is an advanced AI-driven solution designed to empower you with maritime knowledge. Whether you have questions about SOLAS, MARPOL, or any topic within the maritime domain, ShipAI harnesses the capabilities of vector databases, embeddings, transformers, and OpenAI to deliver accurate and insightful answers, making maritime exploration more accessible and efficient.

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
  <img src="https://github.com/yugesharma/shipAI/blob/main/shipai.gif" width="2000" height="600"/>
</div>


<a href='https://shipai.streamlit.app'>Link to web app<a>



# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

   Python 3.7 or higher installed.
   A Pinecone API key and environment setup.
   Necessary secrets for Hugging Face and OpenAI APIs.

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

 4. Set Environment Variables:

 Ensure you set up the necessary environment variables for Pinecone, Hugging Face, and OpenAI API keys
    

# Usage

   1. Run the application:

  ```python

  streamlit run shipai.py
  ```

   2. Access the application in your web browser.

   3. Enter your questions related to the maritime domain in the provided text input.

   4. ShipAI will process your question, search the vector database, and provide you with answers and insights.

# Contributing

Contributions are welcome! If you want to contribute to ShipAI, please follow these steps:

  1.  Fork the repository.
  2.  Create a new branch: git checkout -b feature/new-feature.
  3.  Make your changes and commit them: git commit -m 'Add new feature'.
  4.  Push to the branch: git push origin feature/new-feature.
  5.  Submit a pull request.

# License

This project is licensed under the MIT License
