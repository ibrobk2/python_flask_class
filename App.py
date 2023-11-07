from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def mym():
    family = ["Aisha", "Maryam", "Jamila", "Yusuf"]
    return render_template('index.html', x = "John", family=family)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return redirect(url_for('mym'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True, port=3000)