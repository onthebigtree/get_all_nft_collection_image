import requests
import os

def download_image(url, filepath):
    # 发送GET请求到指定的URL
    response = requests.get(url)
    
    # 检查请求是否成功（状态码为200）
    if response.status_code == 200:
        # 如果目录不存在，则创建所需目录
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以二进制模式打开文件，并将响应内容（图像数据）写入其中
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # 打印成功消息
        print(f"图像下载成功：{filepath}")
    else:
        # 如果请求不成功，则打印错误消息
        print(f"无法下载图像：{filepath}")

base_url = 'https://ipfs.io/ipfs/QmYDvPAXtiJg7s8JdRBSLWdgSphQdac8j1YuQNNxcGE1hg/'
output_dir = 'azuki/'

# 遍历从1到10000的数字范围
for n in range(1, 10001):
    # 根据基本URL和当前数字构建图像的URL
    url = base_url + f"{n}.png"
    
    # 构建图像保存的文件路径
    filepath = os.path.join(output_dir, f"image{n}.png")
    
    # 调用download_image函数，传入URL和文件路径
    download_image(url, filepath)
