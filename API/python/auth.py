from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datebase import APIDataBase
import yaml, os
import base64

auth_blp = Blueprint('login', __name__)
CORS(auth_blp)

config = None
workspace = os.path.dirname(os.path.abspath(__file__)).split('python')[0]
if os.path.exists(workspace + 'config.yaml'):
    config = yaml.load(open(workspace + 'config.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
else:
    print('config.yaml not found')
    os._exit(0)

db = APIDataBase(config)

@auth_blp.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    if name == None or password == None:
        return jsonify({'error': '參數錯誤'})
    data = db.execSelect(f'SELECT * FROM `user` WHERE `name` = `{name}` AND `password` = `{password}`')
    if data == []:
        return jsonify({'error': '無此帳號或密碼錯誤'})
    return jsonify(data)

@auth_blp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    password = request.form.get('password')
    password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    if id == None or name == None or password == None:
        return jsonify({'error': '參數錯誤'})
    if db.execSelect(f'SELECT * FROM `user` WHERE `name` = "{name}"') == []:
        db.exec(f'INSERT INTO `user` (`name`, `password`) VALUES ("{name}", "{password}")')
        return jsonify({'success': '註冊成功'})
    else:
        return jsonify({'error': '此帳號已存在'})

