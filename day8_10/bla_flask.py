from flask import Flask, request, jsonify

# 创建Flask应用
app = Flask(__name__)

# 定义接收POST表单数据的API
@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # 从form中获取数据
        # 使用get方法可以提供默认值，防止KeyError
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        
        # 验证必要的字段
        if not username or not email:
            return jsonify({
                'status': 'error',
                'message': '用户名和邮箱为必填项'
            }), 400
        
        # 这里可以添加数据处理逻辑，比如保存到数据库等
        # ...
        
        # 返回成功响应
        return jsonify({
            'status': 'success',
            'message': '表单提交成功',
            'data': {
                'username': username,
                'email': email,
                'message': message
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'处理请求时出错: {str(e)}'
        }), 500

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
