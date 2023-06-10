import re 

def markdown_to_marp(markdown_text, page_split=2):
    marp_text = "" 
    lines = markdown_text.split("\n")

    for s in lines:
        heading_tag = 0 # Headingタグを調べる

        for el in s:
            if el == "#":
                heading_tag += 1
            else:
                break

        # ページ区切り
        if heading_tag == page_split: #  heading
            marp_text += '---' + "\n\n" 

        marp_text += s + "\n"
        
    return marp_text

def marp_to_markdown(marp_text):
    output = ""

    lines = marp_text.split("\n")
    new_lines = []

    code_block_content = []
    start_code_block = False # コードブロックが始まるか調べる

    # 各行を確認
    for i in range(len(lines)):
        if "```" in lines[i]: 
            code_block_content.append(lines[i])
            if start_code_block == True:              # コードブロックが終了
                new_lines.append(code_block_content)
                code_block_content = []
                start_code_block = False
            else:                                   # コードブロックが始まる
                start_code_block = True 
                
        else:
            if start_code_block:
                code_block_content.append(lines[i])
            else:
                new_lines.append(lines[i])

    for s in new_lines:   
        if not isinstance(s, str): #コードブロック
            output += "\n".join(s)
        else:
            s = s.strip()
            if not check_marp_style(s) and s != "": # marp styleを消除
                output += s + "\n\n"

    return output

# marpのTweak styleをチェック
def check_marp_style(text):
    page_split_pattern =  re.compile("---")
    theme_pattern = re.compile("^theme:")
    _class_pattern = re.compile("^_class:")
    _header_pattern = re.compile("^_header:")
    paginate_pattern = re.compile("^paginate:")
    size_pattern = re.compile("^size:")
    backgroundColor_pattern = re.compile("^backgroundColor:")
    backgroundImage_pattern = re.compile("^backgroundImage:")
    comment_pattern = re.compile("<!--.*-->")

    if re.match(page_split_pattern, text):
        return True

    if re.match(theme_pattern, text):
        return True

    if re.match(_class_pattern, text):
        return True
    
    if re.match(_header_pattern, text):
        return True

    if re.match(paginate_pattern, text):
        return True
    
    if re.match(size_pattern, text):
        return True
    
    if re.match(backgroundColor_pattern, text):
        return True
    
    if re.match(backgroundImage_pattern, text):
        return True

    if re.match(comment_pattern, text):
        return True
    
    
    return False

# テスト
if __name__=="__main__":

    # markdown to marp
    test_markdown_text = "# Hello, world!\n\n## Marp\n\nMarkdown + Marp = Beautiful slide deck\n"
    output_marp = markdown_to_marp(test_markdown_text)
    # print(output_marp)


    # marp to markdown 
    test_marp_text = """
    ---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---
<!-- Scoped style -->

![bg left:40% 80%](https://marp.app/assets/marp.svg)

# **Marp**

Markdown Presentation Ecosystem

https://marp.app/

---

# How to write slides

Split pages by horizontal ruler (`---`). It's very simple! :satisfied:

```markdown
# Slide 1

foobar

---

# Slide 2

foobar
```
    """

    print(marp_to_markdown(test_marp_text))


