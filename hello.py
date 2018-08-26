from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'name': 'Hadimaster',
        'title': 'Hello, World!',
        'content': 'This is my First Web App Using Flask!',
        'date': 'August 26, 2018'
    },
    {
        'name': 'Hadimaster',
        'title': 'Flask 101: Part-1',
        'content': 'This is how we build REST API using flask',
        'date': 'August 26, 2018'
    },
    {
        'name': 'Hadimaster',
        'title': 'Flask 101: Part-2',
        'content': 'This is a second part of Flask 101',
        'date': 'August 26, 2018'
    },
    
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)