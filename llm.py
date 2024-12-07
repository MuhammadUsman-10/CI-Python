from openai_services import call_openai
from chromadb_services import retriever
from my_mongo import save_chat, fetch_chat

PROMPT="""The conversation is related to the project scope and related stuff and you have to answer accordingly like the questions should be in such a way as the committee asks and I'm defending the proposal.If any irrelevant question is asked say i dont have the answer"""


def defense_bot(question, user_id):
    history =  fetch_chat(user_id)
    clean_history = []

    if len(history)>0:
        for item in history:
            clean_history.append(
                {
                    "role":item["role"],
                    "content":item["content"]
                }
            )

    texts =[]
    docs = retriever(question)
    for doc in docs:
        texts.append(doc.page_content)
    combine_text= " ".join(texts)

    messages=[
        {"role": "system", "content": PROMPT},
        {"role": "system", "content": combine_text },
    ]
    messages.extend(clean_history)

    messages.append({"role": "user", "content": question })
    response = call_openai(messages)
    user_chat ={"user_id":user_id, "role":"user", "content":question}
    
    save_chat(user_chat)
    ai_chat = {"user_id":user_id, "role":"assistant", "content":response}
    save_chat(ai_chat)
    return response

while True:
    question = input("Ask a Question:")
    if question == "exit":
        break
    response = defense_bot(question, "usman")
    print(response)
    print("\n")