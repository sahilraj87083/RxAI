# 🩺 RxAI – Medical RAG-Based Chatbot

RxAI is an intelligent **medical question-answering system** powered by **Retrieval-Augmented Generation (RAG)**, **Pinecone vector search**, **HuggingFace embeddings**, and **LangChain**.  
Users can ask questions about **symptoms, cures, diseases, medicines, and precautions**, and RxAI provides accurate responses backed by verified medical documents.

---

## 🚑 Problem This Project Solves

Healthcare information online is often:

- Scattered across unreliable sources  
- Confusing or full of outdated information  
- Hard for non-technical users to search  
- Lacking verified medical grounding  
- Overwhelming due to medical jargon  

**RxAI solves this by offering:**

- A centralized, verified, and search-optimized medical knowledge base 
- A simple chat interface where users can ask anything
- AI-generated responses grounded in retrieved medical documents, not hallucinations  
- Quick and easy access to medical information  
- 24/7 availability with accurate, context-driven responses  

---

## 🌟 Advantages of RxAI

✔ **RAG-based accuracy** – No hallucinations, responses come from real medical data  
✔ **Fast & scalable vector search** using Pinecone  
✔ **High-quality embeddings** (Sentence-Transformers)  
✔ **Lightweight architecture** using Flask  
✔ **Easy to extend** (add more PDFs anytime)  
✔ **Secure** via environment variables  
✔ **Clean, modular codebase** suitable for production  

---

# 🚀 Getting Started

## 1 Clone the Repository
```bash
  git clone https://github.com/your-username/RxAI.git
  cd RxAI
```
## 2 Create a Virtual Environment
```bash
  python3 -m venv venv
  source venv/bin/activate      # macOS / Linux
  venv\Scripts\activate         # Windows
```

## 3 Install Dependencies
```bash
  pip install -r requirements.txt
```

If you're using Pinecone with gRPC:

```bash
  pip install "pinecone-client[grpc]"
```

## 4 Set Up Environment Variables

Create a .env file in the project root:

```bash
  PINECONE_API_KEY=your_pinecone_api_key
  OPENAI_API_KEY=your_openai_key  # if using GPT-based models
  INDEX_NAME=rxai-index
```

## 5 Prepare & Store Your Medical Data

Place all your medical PDFs inside:

```bash
  Data/
```



Then run:

```bash
  python store_index.py
```


This will:

- Load PDFs
- Split documents
- Generate embeddings
- Create (if needed) and upload vectors to your Pinecone index

## 6 Run the Backend (Flask App)

```bash
  python app.py
```


You should see:

```bash
  Flask server running on http://127.0.0.1:5000
```

🧪 API Usage (Example)

## POST /ask
```bash
  {
    "query": "What are the symptoms of dengue?"
  }
```

## Response:

``` bash
  {
    "answer": "Common symptoms of dengue include high fever, severe headache, joint pain..."
  }
```

## 🗂️ Project Structure
```bash
    RxAI/
    │── app.py                 # Flask backend
    │── store_index.py         # Creates Pinecone index & stores vectors
    │── requirements.txt
    │── .env
    │── Data/                  # Your medical PDFs
    │── src/
    │     ├── helper.py        # Embeddings, loaders, and utilities
    │── README.md
```

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Pinecone (Serverless)
- HuggingFace Embeddings
- Sentence Transformers
- Any LLM Backend

## 📌 Future Improvements

- UI frontend (React or Next.js)
- Multi-language support
- More medical datasets
- Voice input + voice output
- Patient history tracking
- Drug-to-drug interaction checker

## ❤️ Contributing

- Pull requests are welcome!
- Feel free to open issues for bugs or feature requests.

## 📜 License

    MIT License – Free to use, modify, and distribute.


