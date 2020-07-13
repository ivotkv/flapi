from ..app import app


@app.route('/status')
def status():
    return 'OK', 200
