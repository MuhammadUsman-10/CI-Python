# Code Uploaded in Classroom
# import os
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# import shutil

# load_dotenv()

# def loader():
#     embeddings = OpenAIEmbeddings()
#     if os.path.exists("./chromadb"):
#         shutil.rmtree("./chromadb")
#     vectorstore = Chroma(
#         persist_directory="./chromadb",
#         embedding_function=embeddings,
#         collection_name="test-questions"
#         )
#     root_path = './defense questions.pdf'
#     DATASET = []
#     items = os.listdir(root_path)
#     for i in items:
#         with open(f"{root_path}/{i}",'r', encoding='utf-8') as f:
#             DATASET.append(f.read())
#     Chroma.add_texts(vectorstore, DATASET)
#     # print("document added to chromadb")

# def retriever(question:str):
#     embeddings = OpenAIEmbeddings()
#     vectorstore = Chroma(
#         persist_directory="./chromadb",
#         embedding_function=embeddings,
#         collection_name="test-questions" #text collection name should always be small alphabets and no special characters
#         )
#     DOCS = []
#     for i in vectorstore.similarity_search(question, 5):
#         DOCS.append(i.page_content)
#     return DOCS


# Code done in Class
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import shutil
load_dotenv()

def load_chunks(docs):
    embeddings = OpenAIEmbeddings(
        model = 'text-embedding-ada-002'
    )
    if os.path.exists("./chromaDB"):
        shutil.rmtree("./chromaDB")
    vectorstore = Chroma(
        persist_directory= "./chromaDB",
        embedding_function= embeddings,
        collection_name= "defensequestions" #text collection name should always be small alphabets and no special characters
    )
    Chroma.add_documents(vectorstore, docs)
    print("document added to chromDB")

def retriever(question: str):
    embeddings = OpenAIEmbeddings(
        model= 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory= "./chromaDB",
        embedding_function= embeddings,
        collection_name= "defensequestions"
    )
    # docs = vectorstore.similarity_search_with_relevance_scores(question, 3)
    docs = vectorstore.similarity_search(question, 5)
    return docs