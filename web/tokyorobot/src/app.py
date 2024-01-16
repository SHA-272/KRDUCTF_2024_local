from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/secretpage')
def secret_page():
    flag = os.environ.get('FLAG', 'Флаг не найден')
    return render_template('secretpage.html', flag=flag)

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
