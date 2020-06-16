from flask import Flask, render_template

app = Flask(__name__)

posts =[
    {
        'author':'Oner berk',
        'title': 'Blog post 1',
        'content': 'first content',
        'date_posted': '15 june 2020'
    },
    {
        'author':'Oner berk',
        'title': 'Blog post 2',
        'content': 'second content',
        'date_posted': '16 june 2020'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()