# Pdf handling functions 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./defense questions.pdf")
docs = loader.load()

# print(docs[0])
# print(len(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    length_function=len,
    is_separator_regex=False,
)

chunks = []

for item in docs:
    text = item.page_content
    pieces = splitter.create_documents({text})
    chunks.extend(pieces)

print(chunks[0])
print(len(chunks))


# Pdf handling functions using logging
# import logging
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# logging.basicConfig(level=logging.INFO)

# loader = PyPDFLoader("./defense questions.pdf")

# logging.info("Loading PDF file...")

# docs = loader.load()

# logging.info(f"Loaded {len(docs)} documents.")

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=150,
#     chunk_overlap=30,
#     length_function=len,
#     is_separator_regex=False,
# )

# logging.info("Splitting documents into chunks...")

# chunks = []

# for item in docs:
#     text = item.page_content
#     pieces = splitter.create_documents({text})
#     chunks.extend(pieces)

# logging.info(f"Created {len(chunks)} chunks.")

# logging.info("Printing first chunk and total chunk count...")

# print(chunks[0])
# print(len(chunks))