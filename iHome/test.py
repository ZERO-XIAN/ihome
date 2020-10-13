import random
import os


a_key1 = 'VYVxIxLPNHBWByIMDAUCszi8rz3JTTOSk5dDPCKj'
s_key1 = 'cxVFcRumpXPerEM4NkCOA7mcvk-bOGmj3iF2hHzd'

a_key2 = '1n4HEJVeVn7DyzfkJ3464xsolSEz9OW8uMaOZES9'
s_key2 = 'fnt6qDbjSbI8pTPU3xodcAetfVUnM7phnJDZSfbD'

keylist = [(a_key1, s_key1), (a_key2, s_key2)]
key = random.choice(keylist)

access_key = key[0]
secret_key = key[1]

print(access_key, secret_key)




app_private_key_path=os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem"),  # 私钥
alipay_public_key_path=os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"),  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
print(alipay_public_key_path[0])