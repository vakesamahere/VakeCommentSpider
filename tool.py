def html_snapshot(html:str,encoding='utf-8'):
    with open('snapshot/html_snapshot.html','w',encoding=encoding) as f:
        f.write(html)

def json_snapshot(json_text:str,encoding='utf-8'):
    with open('snapshot/json_snapshot.json','w',encoding=encoding) as f:
        f.write(json_text)