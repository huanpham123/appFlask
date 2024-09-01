from g4f.client import Client
import gradio as gr
from flask import Flask, jsonify, request

app = Flask(__name__)
client = Client()

def chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    return jsonify({'response': chatbot_response(user_input)})

interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Câu hỏi cho chat", label="Câu hỏi của bạn", elem_id="input_box"),
    outputs=gr.Textbox(label="Chat AI", elem_id="output_box"),
    title="ChatBot AI",
    css="""
    #input_box {
        border: 2px solid #4CAF50;
    }
    #output_box {
        border: 2px solid #2196F3;
    }
    """
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=8080)


















