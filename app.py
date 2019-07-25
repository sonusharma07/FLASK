from flask import Flask , render_template


app = Flask(__name__)

data = [
    {
        "title": "Java",
        "bio": "Java is Object Oriented programming language"
    },
    {
        "title": "Python",
        "bio": "Python is scripting programming language"
    },
    {
        "title": "JavaScript",
        "bio": "JavaSript is Web Server programming language"
    }
]

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

@app.route('/lang/<name>')
def lang(name):
    title = name
    lang = next(langinfo for langinfo in data if langinfo['title'].lower() == name.lower())
    print(lang)
    return render_template('lang.html',title=title,lang=lang )