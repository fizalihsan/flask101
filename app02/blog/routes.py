from app02.blog import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World - v2!"
