import logging
from flask import Flask, request, jsonify, session

USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.secret_key = 'pithy'

# 设置日志级别为 ERROR
app.logger.setLevel(logging.ERROR)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # 获取请求中的 JSON 数据
    username = data.get('username')
    password = data.get('password')

    if username == USERNAME and password == PASSWORD:
        session['logged_in'] = True
        return jsonify({'code': 200, 'msg': '登录成功'})
    else:
        return jsonify({'code': 401, 'msg': '用户名或密码错误'})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()