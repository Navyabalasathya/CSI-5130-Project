DataInsights - An Explainable Retrieval-Augmented Natural Language to SQL System Using Large Language Model

An intelligent system that allows users to query relational databases using natural language and receive both SQL queries and human-readable explanations.


## Overview

DataInsights is a Natural Language to SQL (NL→SQL) system that enables users to query relational databases using natural language. It is a Large Language Model (LLM) application that converts the Natural Language Questions to SQL query, executes the query over a database and return the results. In addition, DataInsights explains the results back in natural language to the user. The System is incorporated with Retrieval-Augmented Generation (RAG) which is using FAISS-based vector store to improve the SQL accuracy by providing relevant schema and relationships as context to guide generation and reduce hallucinations. The generated SQL query is executed over a real-world E-commerce database named Brazilian Olist E-commerce Dataset. Additionally, a self-correcting mechanism addresses SQL execution errors, and the system generates natural language explanations for the results. The project uses LangChain with FAISS for retrieval-augmented generation and GPT-4.1-mini for SQL generation.


## Features

* Natural Language → SQL generation
* Retrieval-Augmented Generation (RAG) using **FAISS**
* Schema-aware query generation with relationships
* Self-correcting SQL pipeline (handles errors)
* Natural language explanations of results
* Interactive UI built with Streamlit
* Works on real-world e-commerce dataset


## System Architecture

DataInsights follows a multi-stage pipeline:
1.User inputs a natural language question 
2.Relevant context is retrieved using a FAISS vector store 
3.User question and context are passed to the LLM 
4.LLM generates SQL query
5.Query is validated and corrected (if necessary)
6.Query is executed on the database and results obtained 
7.Results passed on to LLM for generation of Natural language explanation
8.Results and explanation are displayed in the application


## Tech Stack

* LLM: gpt-4.1-mini
* Framework: LangChain
* Vector Store: FAISS
* Frontend: Streamlit
* Database: SQLite (Olist dataset)
* Embeddings: OpenAI Embeddings (`text-embedding-3-small`)


## Dataset

This project uses the **Brazilian Olist E-commerce Dataset**, which contains real-world e-commerce transaction data.

## 📁 Project Structure

```text
AI-PROJECT/
│
├── app/
│   ├── database/
│   │   ├── connection.py            # Database connection setup
│   │   ├── query_executor.py        # Executes SQL queries
│   │   ├── schema_extractor.py      # Extracts database schema
│   │
│   ├── rag/
│   │   ├── rag_pipeline.py          # FAISS vector store + embeddings
│   │
│   ├── chains/
│   │   ├── sql_generation_chain.py  # Converts NL → SQL using LLM
│   │   ├── result_explainer.py     # Generates natural language explanations
│   │
│   ├── pipeline/
│   │   ├── self_correcting_pipeline.py  # Handles SQL errors & retries
│   │
│   ├── ui/
│   │   ├── main.py                  # Streamlit UI
│
├── data/
│   ├── olist.sqlite                    # Database file
│
├── DataInsights-Report.pdf       # Project report
│                    
│
├── requirements.txt                 # Dependencies
├── .env                             # API keys (not committed)
├── .gitignore                       # Ignored files
├── README.md                        # Documentation
```



##  How to run

### 1. Clone the repository

```bash
git clone https://github.com/Navyabalasathya/CSI-5130-Project
cd CSI-5130-Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app/ui/main.py
```

## Key Contributions

* RAG-based NL→SQL system
* Schema driven retrieval
* Self-correcting SQL generation
* Explainable AI (natural language explanations)
* End-to-end interactive application


## Future Work

* Semantic correction for incorrect results
* Multi-database support
* Enhanced explanation generation
* Automated evaluation of explanation quality 


## Acknowledgements

* OpenAI
* LangChain
* FAISS
* Olist Dataset (Kaggle)

## Concepts
* Retrieval-Augmented Generation (RAG) 
* Natural Language Processing (NLP) 
* Explainable AI (XAI) 



