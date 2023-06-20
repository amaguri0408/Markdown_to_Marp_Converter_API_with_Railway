import markdown
# import pdfkit # wkhtmltopdfのインストールが必要 https://wkhtmltopdf.org/downloads.html
import subprocess

# md_text: markdown形式のテキスト
# data_format: エクスポートするデータの形式（html,pdf)
def md_export(md_text,data_format='html'):
    md = markdown.Markdown()
    html_body = md.convert(md_text)
    # print(html_body)
    html_text = '<html lang="ja"><meta charset="utf-8"><body>'
    # html_text += '<style> body { font-size: 8em; } </style>'
    html_text += html_body + '</body></html>'
    if data_format == 'html':
        with open('md_export.html','w') as f:
            f.write(html_text)
        # return html_text
    
    options = {
     'page-size': 'A4',
     'margin-top': '0.75in',
     'margin-right': '0.75in',
     'margin-bottom': '0.75in',
     'margin-left': '0.75in',
     'encoding': "UTF-8"
    }
    if data_format == 'pdf':
        pdfkit.from_string(html_text, "md_export.pdf",options=options)

# Marpからhtml,pdfに変換
# https://www.npmjs.com/package/@marp-team/marp-cli を使用
# marp_text: marp形式のテキスト
# data_format: エクスポートするデータの形式（html,pdf)
# 動作にNode.jsが必要
def marp_export(marp_text,data_format='html'):
    marp_file = 'marp_export.md'
    print(marp_file[:-2]+'html')
    with open(marp_file,'w',encoding='utf-8') as f:
        f.write(marp_text)
    if data_format == 'html':
        
        subprocess.run('npx @marp-team/marp-cli@latest '+ marp_file,shell=True)
        # with open(marp_file[:-2]+'html','r') as f:
            # html_text = f.read()
            # print(marp_file[:-2]+'html')
            # html_text = html_text.encode('cp932', "ignore")
            # return html_text
    if data_format == 'pdf':
        subprocess.run('npx @marp-team/marp-cli@latest '+ marp_file+' --pdf',shell=True)
    


if __name__ == '__main__':
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
    test_md_text = '# export\n- html\n- pdf\n\n## python'
    
    # html = md_export(test_md_text,'html')
    # md_export(test_md_text,'pdf')
    # print(html)
    # marp_file = 'marp_export.md'
    # print(marp_file[:-2]+'html')
    html = marp_export(test_marp_text,'html')
    # marp_export(test_marp_text,'pdf')
    print(html)
    # with open('test.html','w') as f:
        # f.write(html)
