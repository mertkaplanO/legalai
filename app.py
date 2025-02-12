from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Ollama ile hukuk modeli
def get_legal_answer(question):
    model = "ALIENTELLIGENCE/attorney2"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": question}])
    return response["message"]["content"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Soru boş olamaz!"}), 400

    answer = get_legal_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
