from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datebase import APIDataBase
import yaml, os

song_blp = Blueprint('song', __name__)
CORS(song_blp)

config = None
workspace = os.path.dirname(os.path.abspath(__file__)).split('python')[0]
if os.path.exists(workspace + 'config.yaml'):
    config = yaml.load(open(workspace + 'config.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
else:
    print('config.yaml not found')
    os._exit(0)

db = APIDataBase(config)

@song_blp.route('/getID', methods=['GET'])
def getSong():
    id = request.args.get('id')
    if id == None:
        return jsonify({'error': '參數錯誤'})
    data = db.execSelect(f'SELECT * FROM `song` WHERE `id` = {id}')
    if data == []:
        return jsonify({'error': '查無資料'})
    return jsonify(data)

@song_blp.route('/getPlayList', methods=['GET'])
def getSongList():
    artist = request.args.get('artist')
    if artist == None:
        return jsonify({'error': '參數錯誤'})
    data = db.execSelect(f'SELECT * FROM `song` WHERE `artist` = "{artist}"')
    if data == []:
        return jsonify({'error': '查無資料'})
    return jsonify(data)