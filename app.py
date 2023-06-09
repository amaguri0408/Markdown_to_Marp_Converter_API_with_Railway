from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API is running'

@app.route('/api/v1/marp', methods=['POST'])
def convert_to_marp():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']

    # Marpへの変換処理を実装

    # レスポンスの作成
    response = {
        'raw_body': raw_body  # 変換後のMarpデータを設定
    }
    return jsonify(response), 200

@app.route('/api/v1/markdown', methods=['POST'])
def convert_to_markdown():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']

    # Markdownへの変換処理を実装

    # レスポンスの作成
    response = {
        'raw_body': raw_body  # 変換後のMarkdownデータを設定
    }
    return jsonify(response), 200

@app.route('/api/v1/theme', methods=['POST'])
def change_theme():
    # リクエストボディの取得
    data = request.json
    raw_body = data['raw_body']

    # テーマ変更処理を実装

    # レスポンスの作成
    response = {
        'raw_body': raw_body  # テーマ変更後のMarpデータを設定
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)