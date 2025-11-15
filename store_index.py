from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

load_dotenv()


extracted_data = load_pdf_file(data="Data/")
text_chunks = text_split(extracted_data=extracted_data)
embeddings = download_hugging_face_embeddings()


# Initialize Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")


pc = Pinecone(api_key=pinecone_api_key)
index_name = "rxai-index"

# Create Pinecone Index if not exists

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Embed each chunk and upsert the embeddings into your Pinecone index
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)
