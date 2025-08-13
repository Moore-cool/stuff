from flask import Flask, render_template, request
import base64
import urllib.parse
import html
import json

app = Flask(__name__)

# 编码函数
def encode_text(text, encoding_type):
    try:
        if encoding_type == 'base64':
            return base64.b64encode(text.encode('utf-8')).decode('utf-8')
        elif encoding_type == 'url':
            return urllib.parse.quote(text)
        elif encoding_type == 'html':
            return html.escape(text)
        elif encoding_type == 'json':
            return json.dumps(text)
        else:
            return "不支持的编码类型"
    except Exception as e:
        return f"编码错误: {str(e)}"

# 解码函数
def decode_text(text, decoding_type):
    try:
        if decoding_type == 'base64':
            return base64.b64decode(text).decode('utf-8')
        elif decoding_type == 'url':
            return urllib.parse.unquote(text)
        elif decoding_type == 'html':
            return html.unescape(text)
        elif decoding_type == 'json':
            return json.loads(text)
        else:
            return "不支持的解码类型"
    except Exception as e:
        return f"解码错误: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    action = "encode"  # 默认动作是编码
    encoding_type = "base64"  # 默认编码类型
    decoding_type = "base64"  # 默认解码类型
    input_text = ""
    
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        action = request.form.get('action', 'encode')
        
        if action == 'encode':
            encoding_type = request.form.get('encoding_type', 'base64')
            result = encode_text(input_text, encoding_type)
        else:
            decoding_type = request.form.get('decoding_type', 'base64')
            result = decode_text(input_text, decoding_type)
    
    return render_template('index.html', 
                          result=result, 
                          action=action,
                          encoding_type=encoding_type,
                          decoding_type=decoding_type,
                          input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
