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

Introduction

The maritime domain is vast and complex, and extracting information from it can be challenging. ShipAI simplifies this process by allowing you to ask questions about plethora of regulations, resulting in saving time and it provides you with relevant answers.
Features

    Ask questions related to the maritime domain.
    Utilize vector databases to search for relevant documents.
    Use embeddings and transformers to understand and analyze text.
    Incorporate OpenAI's capabilities for question answering.

Demo

<div align="center">
  <img src="https://github.com/yugesharma/shipAI/blob/main/shipai.gif" width="1000" height="600"/>
</div>



<a href='https://shipai.streamlit.app'>Link to web app<a>



Getting Started
Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.7 or higher installed.
    A Pinecone API key and environment setup.
    Necessary secrets for Hugging Face and OpenAI APIs.

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/ShipAI.git
cd ShipAI

Create a virtual environment and activate it:

bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:

bash

    pip install -r requirements.txt

    Set up your environment variables for Pinecone, Hugging Face, and OpenAI API keys.

Usage

    Run the application:

    bash

    streamlit run shipai.py

    Access the application in your web browser.

    Enter your questions related to the maritime domain in the provided text input.

    ShipAI will process your question, search the vector database, and provide you with answers and insights.

Contributing

Contributions are welcome! If you want to contribute to ShipAI, please follow these steps:

    Fork the repository.
    Create a new branch: git checkout -b feature/new-feature.
    Make your changes and commit them: git commit -m 'Add new feature'.
    Push to the branch: git push origin feature/new-feature.
    Submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
