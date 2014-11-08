from lib import app
import v

@app.route('/')
def index():
    return v.index()

@app.route('/flex')
def flex():
    return v.flex()
