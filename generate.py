from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
]

CORS(app, resources={r"/*": {"origins": origins}})

@app.route("/suggest/", methods=["POST"])
def suggest_next_word():
    try:
        prompt = request.json.get('text', '').lower().strip()

        with open('shakespeare_set.txt', 'r', encoding='utf-8') as file:
            data = file.read().lower()

        def get_suggestions(data, prompt, max_suggestions=5):
            words = data.split()
            prompt_words = prompt.split()
            suggestions = {}

            for i in range(len(words) - len(prompt_words)):
                if words[i:i+len(prompt_words)] == prompt_words:
                    next_word = words[i + len(prompt_words)]
                    if next_word not in prompt_words:  # Avoid suggesting words already in the prompt
                        if next_word in suggestions:
                            suggestions[next_word] += 1
                        else:
                            suggestions[next_word] = 1

            sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
            return [word for word, _ in sorted_suggestions[:max_suggestions]]

        suggestions = get_suggestions(data, prompt)
        return jsonify({"suggestions": suggestions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000)
