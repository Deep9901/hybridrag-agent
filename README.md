

# HybridRAG Agent

A full-stack RAG (Retrieval-Augmented Generation) application featuring a **FastAPI** backend and a **Streamlit** frontend.


## Key Features

- **Hybrid AI & Intelligent Routing**: Combines internal RAG knowledge with real-time web search, dynamically selecting the best information source for each query.

- **User-Controlled Web Access**: Provides a UI toggle to enable or disable web search, allowing users to choose between internal-only knowledge or broader internet access.

- **Transparent AI Workflow (Agent Trace)**: Offers a detailed, step-by-step trace of the agent's internal thought process, including routing decisions, RAG sufficiency verdicts, and information retrieval summaries.
- **Contextual RAG Sufficiency Judgment**: Employs an LLM to critically assess if retrieved RAG content is sufficient to answer a query, preventing incomplete responses and prompting further search if needed.

- **Dynamic Knowledge Ingestion (PDF Upload)**: Users can upload PDF documents directly, which are automatically processed, embedded, and added to the agent's Pinecone knowledge base.

- **Modular & Extensible Design**: Clean, layered architecture (FastAPI, LangGraph, Streamlit) makes it easy to understand, debug, and expand.

- **Persistent Conversation Memory**: LangGraph's checkpointing maintains conversation context across multiple turns.


##  High-Level Architecture

### Layers Overview:

- **User Interface (UI)**: Streamlit app for interaction.
- **API Layer**: FastAPI backend that receives and handles requests.
- **Agent Core**: LangGraph-powered AI logic with routing and tools.
- **Knowledge Base**: Pinecone vector DB + HuggingFace embeddings.
- **External Tools**: Groq LLM, Tavily Search API.

##  Technology Stack

- **Language**: Python 3.10+
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Agent Orchestration**: LangGraph
- **LLMs & Tools**: LangChain, Groq (Llama 3)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: Pinecone
- **PDF Processing**: PyPDFLoader
- **Search Engine**: Tavily API

---

##  Quick Start with Docker

The easiest way to run the entire system is using Docker Compose.

1. **Clone the repository:**
```bash
git clone <your-repo-link>
cd hybridrag-agent

```


2. **Set up your environment:**
Create a `.env` file in the root directory and add your API keys:
```text
GROQ_API_KEY="your_groq_api_key_here"
PINECONE_API_KEY="your_pinecone_api_key_here"
PINECONE_ENVIRONMENT="your_pinecone_environment"
TAVILY_API_KEY="your_tavily_api_key"
FASTAPI_BASE_URL="http://localhost:8000"

```


3. **Launch the application:**
```bash
docker compose up --build

```


4. **Access the services:**
* **Frontend (UI):** [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)
* **Backend (API Docs):** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)



---

## 🛠 Project Structure

* **`main.py`**: The FastAPI backend handling RAG logic and agent orchestration.
* **`app.py`**: The Streamlit frontend providing the user interface.
* **`Dockerfile`**: Defines the environment for both services.
* **`docker-compose.yml`**: Manages the orchestration and networking between containers.

---

## 💻 Local Development (Without Docker)

If you prefer to run it locally using a virtual environment:

1. **Install dependencies:**
```bash
pip install -r requirements.txt

```


2. **Start Backend:**
```bash
uvicorn main:app --reload

```


3. **Start Frontend:**
```bash
streamlit run app.py

```



