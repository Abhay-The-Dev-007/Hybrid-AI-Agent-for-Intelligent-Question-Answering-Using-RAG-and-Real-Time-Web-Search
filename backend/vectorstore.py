import os 
from pinecone import Pinecone,ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import PINECONE_API_KEY

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY

pc=Pinecone(api_key=PINECONE_API_KEY)

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

INDEX_NAME = "rag-index"
# retreiver function
def get_retrevier():
    """Initializes and returns the Pinecone vector store retriever"""
    if INDEX_NAME not in pc.list_indexes().names():
        print("Creating new index")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud='aws',region='us-east-1')
        )
        print("Created pinecone index")

    vectorstore=PineconeVectorStore(index_name=INDEX_NAME,embedding=embeddings)
    return vectorstore.as_retriever()


# upload document to vs
def add_document(text_content:str):
    """Add a single text document to the pinecone vector store, splits the text into chunks before embeddings and upserting"""
    if not text_content:
        raise ValueError("Document content cannot be empty")

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )

    # create langchain document objs from tech raw text
    documents=text_splitter.create_documents([text_content])
    print("Splitting document inot chunk for indexing...")


    # get vector store instance to add documents
    vectorstore=PineconeVectorStore(index_name=INDEX_NAME,embedding=embeddings)

    #add documents to vectorstore
    vectorstore.add_documents(documents)
    print("Successfully added chunks to pinecone vector store")




