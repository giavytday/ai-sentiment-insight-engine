AI Sentiment Insight Engine
A web application that leverages IBM Watson’s BERT-based NLP models to perform real-time sentiment analysis on user-provided text. This project demonstrates full-stack Python development, modular package design, and rigorous automated testing for production-ready AI services.

🚀 Key Features
AI-Powered Analysis: Utilizes the BERT (Bidirectional Encoder Representations from Transformers) workflow to accurately categorize text sentiment as Positive, Negative, or Neutral.
Data Transformation: Implements custom parsing logic to extract and format complex JSON responses from the Watson NLP service into clean, user-facing insights.
Modular Architecture: Structured as a reusable Python package (SentimentAnalysis) with a clear __init__.py entry point, allowing the AI logic to be easily imported into other applications.
Robust Error Handling: Specifically engineered to handle edge cases—such as nonsensical or blank inputs—by monitoring API status codes (500) and returning graceful None values to prevent application crashes.
Code Excellence: Verified with a 10/10 Pylint score, adhering strictly to PEP 8 industry standards for clean, maintainable code.

🛠️ Tech Stack
Backend: Python 3.11, Flask
AI/NLP: IBM Watson NLP (Embedded BERT Workflow)
Frontend: HTML5, CSS3, JavaScript (Asynchronous Fetch API)
Quality Assurance: Unittest Library, Pylint
