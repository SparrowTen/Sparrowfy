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
    
'''
```
GET:
  getID
  127.0.0.1:5000/api/song/getID?id=1

  getPlayList
  127.0.0.1:5000/api/song/getPlayList?artist=Ayase / YOASOBI

POST:
  login
  127.0.0.1:5000/api/auth/login
  - name
  - passowrd

  register
  127.0.0.1:5000/api/auth/register
  - name
  - password
```
'''