import os
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone.init(
      api_key=os.getenv('PINECONE_API_KEY'),
      environment=os.getenv("")
)

