#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
@app.route('/rs', methods=['POST'])
def form_res():
    email = request.form.get('email')
    text = request.form.get('text')
    
    with open('form.txt', 'a',) as f:
        f.write(email+' '+text+'\n')
    return render_template('form_result.html',
                           email=email,
                           text=text
    )

app.run(debug=True)