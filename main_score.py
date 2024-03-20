from flask import Flask, render_template, request
from utils.score import read_scores
from utils.utils import BAD_RETURN_CODE, SCORES_HTML_FILE, ERROR_HTML_FILE

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def score_server():
    username = None
    if request.method == 'POST':
        username = request.form['username']
    username = None if not username else username.strip()
    scores = read_scores(username)
    if list(scores.keys())[0] == BAD_RETURN_CODE:
        return render_template(ERROR_HTML_FILE, ERROR=scores[BAD_RETURN_CODE])
    else:
        return render_template(SCORES_HTML_FILE, SCORES=scores)


app.run(debug=True, host='0.0.0.0', port=5000)
