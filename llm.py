from openai_services import call_openai
from chromadb_services import retriver

PROMPT="""I will ask questions related to the project scope and related stuff and you have to answer accordingly."""


def defense_bot(question):
    texts =[]
    docs = retriver(question)
    for doc in docs:
        texts.append(doc.page_content)
    combine_text= "".join(texts)

    messages=[
        {"role": "system", "content": PROMPT},
        {"role": "system", "content": combine_text },
        {"role": "user", "content": question }
    ]
    response = call_openai(messages)
    return response

while True:
    question = input("Ask a Question:")
    if question == "exit":
        break
    response = defense_bot(question)
    print(response)
    print("\n")