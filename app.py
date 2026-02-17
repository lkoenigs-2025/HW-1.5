from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('home.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
