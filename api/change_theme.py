import re


def change_theme(raw_body, theme):
    # 正規表現でtheme: *\nを，theme: theme\nに変換
    theme_pattern = re.compile(r"theme: [a-z0-9]*")
    theme_line = f"theme: {theme}"
    res_raw_body = theme_pattern.sub(theme_line, raw_body)
    return res_raw_body


if __name__ == "__main__":
    # test
    test_list = [
        {
            "raw_body": "theme: default",
            "theme": "gaia",
            "res_raw_body": "theme: gaia"
        },
        {
            "raw_body": "---\ntheme: gaia\n---",
            "theme": "default",
            "res_raw_body": "---\ntheme: default\n---"
        },
        {
            "raw_body": "---\ntheme: uncvoer\n---",
            "theme": "gaia",
            "res_raw_body": "---\ntheme: gaia\n---"
        },
    ]
    for test in test_list:
        res_raw_body = change_theme(test["raw_body"], test["theme"])
        assert res_raw_body == test["res_raw_body"], f"res_raw_body: {res_raw_body}, test['res_raw_body']: {test['res_raw_body']}"