from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config
import random


# 需要填写你的 Access Key 和 Secret Key
a_key1 = 'VYVxIxLPNHBWByIMDAUCszi8rz3JTTOSk5dDPCKj'
s_key1 = 'cxVFcRumpXPerEM4NkCOA7mcvk-bOGmj3iF2hHzd'

a_key2 = '1n4HEJVeVn7DyzfkJ3464xsolSEz9OW8uMaOZES9'
s_key2 = 'fnt6qDbjSbI8pTPU3xodcAetfVUnM7phnJDZSfbD'

keylist = [(a_key1, s_key1), (a_key2, s_key2)]
key = random.choice(keylist)

access_key = key[0]
secret_key = key[1]

def storage(file_data):
    """
    上传文件到七牛
    :param file_data: 要上传的文件数据
    :return:
    """
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'python3-ihome-flask'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    ret, info = put_data(token, None, file_data)

    # print(info)
    # print("*"*10)
    print(ret)
    if info.status_code == 200:
        # 表示上传成功, 返回文件名
        # print("上传成功")
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传图片到七牛失败")


if __name__ == '__main__':
    with open("./images/04.jpg", "rb") as f:
        file_data = f.read()
        storage(file_data)
