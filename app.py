from flask import Flask, render_template, request, jsonify
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#initializing flask and OpenAI keys
app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = "PLACE YOUR OPENAI KEY HERE"
API_Key = os.environ.get("OPENAI_API_KEY")
chatmodel = ChatOpenAI(openai_api_key=API_Key)

# Route to render the html page
@app.route('/') 
def chatbot_interface():
    return render_template('chatbot.html')

# Route to post the responses that the chatbot gives based on the user messages.
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    sys_message = SystemMessage(content="You're a polite chatbot, keep your responses below 30 words.") #dictates the chatbot's personality
    conversation_history = [sys_message, HumanMessage(content=user_message)] #stores all the conversation history between the user and chatbot
    prediction_message = chatmodel.predict_messages(conversation_history) #initializes the chatbot's response by looking at the conversation history
    chatbot_response = prediction_message.content 
    return jsonify({"chatbot_response": chatbot_response}) #returns the chatbot's response

@app.route('/chat_history', methods=['GET'])
def chat_history():
    # Implement logic to retrieve and return chat history
    pass

if __name__ == '__main__':
    app.run(debug=True)
