# 爬取图片
import requests
URL = 'https://storage-asset.msi.com/global/picture/image/feature/nb/skylake/killer_shield_left_img.jpg'
res = requests.get(URL)
# 发出请求，并把返回的结果放在变量res中
photo = open('Be careful.jpg','wb')
# 新建了一个文件Be careful.jpg，这里的文件没加路径，会被保存在程序运行的当前目录下。
photo.write(res.content)
# 将 Reponse 对象的内容以 [二进制数据] 的形式写入文件
photo.close()
# 关闭文档
