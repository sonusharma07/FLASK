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

@app.route('/about')
def about():
    title = 'about us'
    return render_template('about.html' , title=title)

@app.route('/contact')
def contact():
    title = 'contact us'
    return render_template('contact.html' , title=title)

@app.route('/terms')
def terms():
    title = 'Terms of Use'
    return render_template('terms.html' , title=title)

@app.route('/privacy')
def privacy():
    title = 'Privacy policy'
    return render_template('privacy.html' , title=title)