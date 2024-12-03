import os
import shutil
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def load_chunks(docs):
    embeddings = OpenAIEmbeddings(
        model = 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory= "./chromadb",
        embedding_function= embeddings,
        collection_name= "test_collection" #text collection name should always be small alphabets and no special characters
    )
    Chroma.add_documents(vectorstore, docs)
    print("document added to chromadb")


def get_retriever():
    embeddings = OpenAIEmbeddings(
        model = 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory= "./chromadb",
        embedding_function= embeddings,
        collection_name= "test_collection" #text collection name should always be small alphabets and no special characters
    )
    return vectorstore.as_retriever()


def format_docs(docs):
    return "\n\n" .join(doc.page_content for doc in docs)

LLM = ChatOpenAI(model='gpt-4o-mini')
retriever = get_retriever()
prompt = ChatPromptTemplate.from_template(
    """You can answer any question from this {data}
    This is the topic:{question}"""
)

chain = ({"data": retriever | format_docs, 
        "question": RunnablePassthrough()} 
        | prompt 
        | LLM 
        | StrOutputParser())
print(chain.invoke("Is the project Useful?"))

# response = chain.stream({"question":"dogs"})
# for r in response:
#     print(r, end=" ", flush=True)