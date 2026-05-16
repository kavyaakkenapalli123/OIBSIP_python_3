// static/script.js

const chatBox = document.getElementById("chatBox");

function addMessage(message, sender) {

    const div = document.createElement("div");

    div.classList.add("message");
    div.classList.add(sender);

    div.innerText = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const input = document.getElementById("userInput");

    const message = input.value;

    if (!message) return;

    addMessage(message, "user");

    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    addMessage(data.response, "bot");

    speakText(data.response);
}

function speakText(text) {

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";

    window.speechSynthesis.speak(speech);
}

function startListening() {

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.onresult = function(event) {

        const text = event.results[0][0].transcript;

        document.getElementById("userInput").value = text;

        sendMessage();
    };

    recognition.start();
}