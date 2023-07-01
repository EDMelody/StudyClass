import requests

# 定义登录接口的 URL
url = 'http://localhost:5000/login'

# 定义请求体数据
data = {
    'username': 'admin',
    'password': '123456'
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 解析响应的 JSON 数据
result = response.json()

# 打印响应结果
print(result)