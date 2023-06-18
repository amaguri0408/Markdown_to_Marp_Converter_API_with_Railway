import json
import uuid
import datetime
from pathlib import Path

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from api.converter import markdown_to_marp, marp_to_markdown
from api.change_theme import change_theme

app = Flask(__name__)

# config
with open('config.json') as f:
    config = json.load(f)

CORS(app, **config['cors'])


@app.route('/')
@cross_origin()
def home():
    return 'API is running'


@app.route('/api/v1/upload/image', methods=['POST'])
@cross_origin()
def upload_image_api():
    # リクエストボディの取得
    data = request.files
    image = data['image']

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%y%m%d_%H%M%S")

    # 画像を保存
    save_path = Path(config['image_save_path']) / f'{formatted_datetime}_{image.filename}'
    # すでに存在していたら，数字を足していく
    i = 1
    while save_path.exists():
        save_path = Path(config['image_save_path']) / f'{formatted_datetime}_{i}_{image.filename}'
        i += 1
    image.save(save_path)

    # 画像のURLを作成
    image_url = f"{config['url']}/{config['image_save_path']}/{save_path.name}"

    # レスポンスの作成
    response = {
        'url': image_url  # 画像のURLを設定
    }
    return jsonify(response), 200


@app.route('/api/v1/marp', methods=['POST'])
@cross_origin()
def convert_to_marp_api():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']

    # レスポンスの作成
    response = {
        'raw_body': markdown_to_marp(raw_body)  # 変換後のMarpデータを設定
    }
    return jsonify(response), 200


@app.route('/api/v1/markdown', methods=['POST'])
@cross_origin()
def convert_to_markdown_api():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']

    # レスポンスの作成
    response = {
        'raw_body': marp_to_markdown(raw_body)  # 変換後のMarkdownデータを設定
    }
    return jsonify(response), 200


@app.route('/api/v1/theme', methods=['POST'])
@cross_origin()
def change_theme_api():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']
    theme = data['theme']

    # レスポンスの作成
    response = {
        'raw_body': change_theme(raw_body, theme)  # テーマ変更後のMarpデータを設定
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)