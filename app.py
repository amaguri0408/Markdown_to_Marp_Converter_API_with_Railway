import json
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