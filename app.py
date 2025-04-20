from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message'].lower()
    
    # Enhanced response logic with more interactive patterns
    if any(word in user_message for word in ['hello', 'hi', 'hey', 'greetings']):
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! I'm here to assist you!",
            "Greetings! I'm excited to chat with you!",
            "Hello! It's wonderful to see you!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif 'how are you' in user_message:
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm feeling wonderful! How's your day going?",
            "All systems operational and ready to help! How are you?",
            "I'm fantastic! I love chatting with interesting people like you!",
            "Couldn't be better! Looking forward to our conversation!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif any(word in user_message for word in ['bye', 'goodbye', 'see you', 'later']):
        responses = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye for now! Come back anytime!",
            "Until next time! Stay awesome!",
            "Farewell! Looking forward to our next chat!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif 'thank' in user_message:
        responses = [
            "You're welcome! Is there anything else I can help you with?",
            "Glad I could help! Let me know if you need anything else!",
            "My pleasure! Don't hesitate to ask if you need more assistance!",
            "Anytime! Your satisfaction is my priority!",
            "It's what I'm here for! Ready for more questions!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif any(word in user_message for word in ['help', 'assist', 'support']):
        responses = [
            "I'm here to help! I can chat with you, answer questions, or just keep you company. What would you like to discuss?",
            "Ready to assist! What kind of help do you need today?",
            "Your personal assistant at your service! How can I make your day better?",
            "I'd love to help! Tell me what's on your mind.",
            "Count on me for support! What challenge can I help you with?"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif 'weather' in user_message:
        responses = [
            "I wish I could tell you about the weather, but I'm just a simple chatbot. Maybe we could talk about something else?",
            "While I can't check the weather, I can brighten your day with a nice conversation!",
            "The weather is beyond my capabilities, but I'm great at chatting!",
            "I'm not a weather bot, but I'm a fantastic conversation partner!",
            "Let's focus on things I can help with - I'm great at discussions and problem-solving!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif 'name' in user_message:
        responses = [
            "I'm HEM's AI, your friendly chat companion! Nice to meet you!",
            "You can call me HEM's AI! I'm here to make your day better!",
            "HEM's AI at your service! What shall we talk about?",
            "I'm HEM's AI, your digital friend and helper!",
            "The name's AI - HEM's AI! Pleasure to meet you!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    elif '?' in user_message:
        responses = [
            "That's an interesting question! I'm a simple chatbot, but I'll try my best to help.",
            "Great question! Let me try to assist you with that.",
            "I'm thinking about your question... While I'm a basic AI, I'll do my best to help!",
            "Excellent query! Let's explore this together!",
            "I love questions! They help me understand you better!"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    else:
        responses = [
            f"I understand you said: '{user_message}'. How can I assist you further?",
            f"Interesting! You mentioned '{user_message}'. Would you like to tell me more?",
            f"I heard you say '{user_message}'. What would you like to know about that?",
            f"That's intriguing - '{user_message}'. Let's discuss this further!",
            f"'{user_message}' - that's a fascinating topic! What aspects interest you most?"
        ]
        bot_response = responses[hash(user_message) % len(responses)]
    
    return jsonify({
        'response': bot_response
    })

if __name__ == '__main__':
    app.run(debug=True)