from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    title='Learn Flask'
    programming_languages = [
        'python',
        'JAVA',
        'JavaScript'
    ]
    return render_template('index.html' , title=title, programming_languages=programming_languages)

