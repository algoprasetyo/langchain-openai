// chatbot.js

const chatForm = document.getElementById('chat-form');
const userMessageInput = document.getElementById('user-message');
const chatOutput = document.getElementById('chat-output');

chatForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const userMessage = userMessageInput.value;
    userMessageInput.value = '';

// Sending the user message to the server
fetch('/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json', // Set the Content-Type to JSON
    },
    body: JSON.stringify({ user_message: userMessage })
})
.then(response => response.json())
.then(data => {
    const chatbotResponse = data.chatbot_response;
    chatOutput.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatOutput.innerHTML += `<p><strong>Chatbot:</strong> ${chatbotResponse}</p>`;
})
.catch(error => console.error(error));
});
