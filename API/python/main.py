from flask import Flask
from flask_cors import CORS

from song import song_blp
from auth import auth_blp

app = Flask(__name__)
CORS(app)

app.register_blueprint(song_blp, url_prefix = '/api/song/')
app.register_blueprint(auth_blp, url_prefix = '/api/auth/')

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port=5000)