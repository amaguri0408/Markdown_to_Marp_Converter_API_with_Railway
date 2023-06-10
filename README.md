# HackU 2023 Team07 backend

Deployed: https://markdown-to-marp-converter-api.herokuapp.com

## Overview

This API provides functionality to convert Markdown and Marp data back and forth. It includes the following endpoints:

- `/api/v1/marp`: Convert Markdown to Marp data.
- `/api/v1/markdown`: Convert Marp data to Markdown.
- `/api/v1/theme`: Change the theme of Marp data.

## Installation

```bash
git clone https://github.com/kaneko1102/Markdown_to_Marp_Converter_API.git
cd Markdown_to_Marp_Converter_API
```

install requirements

```bash
pip install -r requirements.txt
```

## Usage

1. Start the application.

```bash
python app.py
```

2. Send requests to the following endpoints using a browser or an API development tool.

## Testing

This API can be tested with the following command.

```bash
pytest -s
```

The test is managed by `tests/test_data.json` and test cases can be modified and added.
