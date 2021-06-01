from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

# Bundling src/main.css files into dist/main.css'
css = Bundle('src/main.css', output='dist/main.css', filters='postcss')

assets = Environment(app)
assets.register(css)



news = [
    {
        'title': 'Getting started with Flask',
        'author': 'Fridolin',
        'category': 'Flask'
    },
    {
        'title': 'Django Started',
        'author': 'Andrea',
        'category': 'Django'
    },
]


@app.route('/')
def landing():
    return render_template('home.html', data=news)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()
