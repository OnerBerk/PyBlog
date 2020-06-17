from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY']='674bad2b681ff4b8d50dc40c7f158b7d'
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
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Le compte de {form.username.data} est crée ! ', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('vous etes connecté', 'success')
            return redirect(url_for('home'))
        else:
            flash('non connecté. Veuillez verifié votre mail et password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)