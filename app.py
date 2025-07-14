from flask import Flask, render_template, request, jsonify
import google.generativeai as ai

app = Flask(__name__)

# Configure Gemini API
my_key = "AIzaSyAXGULUi8q9m-RTopo2Tf88Dm9grq7peDY"
ai.configure(api_key=my_key)
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_input = request.json['msg']
    if user_input.lower() == "bye":
        return jsonify({"response": "Goodbye!"})
    result = chat.send_message(user_input)
    return jsonify({"response": result.text})

if __name__ == "__main__":
    app.run(debug=True)
