from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello word'

@app.route('/about')
def about():
    return 'Information about autor'


@app.route('/blog')
def blog():
    return 'This is blog'

@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя {username}"


if __name__ == '__main__':
    app.run(port=8000)





