import sys
import json
import pytest
from pathlib import Path

# path追加
sys.path.append(str(Path(__file__).parent.parent))

from app import app


@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    yield client


def check_response(client, method, url, request_body, expected_status_code, expected_response):
    if method == 'post':
        response = client.post(url, json=request_body)
    elif method == 'get':
        response = client.get(url)
    elif method == 'put':
        response = client.put(url, json=request_body)
    elif method == 'delete':
        response = client.delete(url)
    else:
        raise ValueError(f'Invalid method: {method}')

    assert response.status_code == expected_status_code
    assert response.json == expected_response


def test_api(client):
    with open('test_data.json') as f:
        test_data = json.load(f)
    
    print()
    for urls in test_data.values():
        for url, methods in urls.items():
            for method, test_list in methods.items():
                for test in test_list:
                    print(f'[{method}] {url}: ', end='')
                    check_response(client, method, url, test['request_body'], test['expected_status_code'], test['expected_response'])
                    print('OK')
