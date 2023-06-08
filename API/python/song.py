from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datebase import APIDataBase
import yaml, os

song_blp = Blueprint('song', __name__)
CORS(song_blp)

config = None
if os.path.exists('config.yaml'):
    config = yaml.load(open('config.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
else:
    print('config.yaml not found')
    os._exit(0)

db = APIDataBase(config)

@song_blp.route('/getSong', methods=['GET'])
def getSong():
    id = request.args.get('id')
    return jsonify(db.execSelect(f"SELECT `dept_id`, `dept_name` FROM `degree_dept` WHERE `id` = \'{id}\'"))