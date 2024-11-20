# Code Uploaded in Classroom
import logging

logging.basicConfig(
    #filename='app.log', # Uncomment this line to write logs to a file
    level=logging.DEBUG, 
    format='[%(asctime)s] - %(levelname)s - %(message)s'
)

# Logging messages at different levels
logging.debug("This is a debug message, useful for diagnosing problems.")
logging.info("This is an info message, for general information.")
logging.warning("This is a warning, something unexpected happened but not critical.")
logging.error("This is an error, something went wrong.")
logging.critical("This is a critical error, the program might shut down.")
# Output:
# [2022-01-30 12:00:00,000] - DEBUG - This is a debug message, useful for diagnosing problems.
# [2022-01-30 12:00:00,000] - INFO - This is an info message, for general information.
# [2022-01-30 12:00:00,000] - WARNING - This is a warning, something unexpected happened but not critical.
# [2022-01-30 12:00:00,000] - ERROR - This is an error, something went wrong.
# [2022-01-30 12:00:00,000] - CRITICAL - This is a critical error, the program might shut down.
# The logging module provides a way to configure the logging system from a configuration file.
# The configuration file is a Python file that specifies how settings are defined in the logging module.
# The configuration file can be used to set the log level, format, and output destination.



# Code Done in Class
import logging
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

logging.basicConfig(level=logging.INFO)

loader = PyPDFLoader("./defense questions.pdf")

logging.info("Loading PDF file...")

docs = loader.load()

logging.info(f"Loaded {len(docs)} documents.")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    length_function=len,
    is_separator_regex=False,
)

logging.info("Splitting documents into chunks...")

chunks = []

for item in docs:
    text = item.page_content
    pieces = splitter.create_documents({text})
    chunks.extend(pieces)

logging.info(f"Created {len(chunks)} chunks.")

logging.info("Printing first chunk and total chunk count...")

print(chunks[0])
print(len(chunks))
