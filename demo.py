from flask import *
import json
import datetime
import openai
import os

# openai.api_key = os.environ["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"]
openai.api_key = "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"



app = Flask(__name__)
app.config["Debug"] = True


def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/output', methods=['GET','POST'])
def output():
    userInput = request.args.get('user-input')
    prompt = f"Generate a program to {userInput}."
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    program = response.choices[0].text.strip()
    # return f"You entered: {userInput}"
    return f"You entered: {program}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)



app.run()