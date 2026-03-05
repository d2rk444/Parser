import os
from flask import Flask, Response

app = Flask(__name__)

_DIR  = os.path.dirname(os.path.abspath(__file__))
_HTML = open(os.path.join(_DIR, 'index.html'), encoding='utf-8').read()

@app.route('/')
def index():
    return Response(_HTML, mimetype='text/html; charset=utf-8')

@app.route('/health')
def health():
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
