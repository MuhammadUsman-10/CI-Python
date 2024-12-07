import gradio as gr
from chatbot1 import chain

def chat(question, chat_history):
    chat_history.append({"role":"user", "content":question})
    if question == "":
        response = "Please Ask A Question:"
        chat_history.append({"role":"assistant", "content":response})
    else:
        # response = chain.stream({"question":question})
        response = chain.stream(question)
        chat_history.append({"role":"assistant", "content":''})
    
    for res in response:
        chat_history[-1]["content"] += res
        # yield res, chat_history
        yield "", chat_history

with gr.Blocks(title="ChatBot") as demo:
    gr.Markdown("Chat with Custom LLM")
    with gr.Row():
        gr.Markdown("")
        with gr.Column(scale=6):
            chatbox = gr.Chatbot(type = "messages")
            with gr.Row():
                textbox = gr.Textbox(label = "Ask a Question", placeholder="Type your query here...", scale=7)
                submit_button = gr.Button(value = "Submit", scale=3, variant="primary")
                # chat_history = gr.Textbox(lines = 10, label = "Chat History")
        gr.Markdown("")
    textbox.submit(chat, inputs=[textbox, chatbox], outputs=[textbox, chatbox])
    submit_button.click(chat, inputs=[textbox, chatbox], outputs=[textbox, chatbox])

demo.launch()

# with gr.Blocks(title="ChatBot") as demo:
#     with gr.Column():
#         chatbox = gr.Chatbot(type = "messages")
#         with gr.Row():
#             question = gr.Textbox(lines = 2, label = "Ask a Question")
#             submit = gr.Button(text = "Submit", scale=3)
#             chat_history = gr.Textbox(lines = 10, label = "Chat History")
#     question.submit(chat, [question, chatbox])
# gr.ChatInterface(
#     fn = chat,
#     type = "messages"
# ).launch(
#     share = True
# )