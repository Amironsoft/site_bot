from flask import Flask, request

from site_bot import get_answer
app = Flask(__name__)

@app.route("/", methods=['GET'])
def start_bot():
    question = request.args['question']
    print("get question")
    return get_answer(question)

app.run(debug=True)
