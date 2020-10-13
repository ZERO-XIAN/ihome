# coding=utf-8

from .CCPRestSDK import REST

# 主帐号
# accountSid = 控制台中的ACCOUNT SID
accountSid = "8aaf0708747ac632017495da36751e58"

# 主帐号Token
# accountToken = 控制台中的AUTH TOKEN
accountToken = "77de4974f92245d0bfa7605f2478b57d"

# 应用Id
# appId = 控制台中的AppID
appId = "8aaf0708747ac632017495da37901e5f"
# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        # 如果有，则将保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_template_sms(self, to, datas, temp_id):
        """"""
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        print('result:\n', result)
        # for k, v in result.items():
            # if k == 'templateSMS':
            #     for k, s in v.items():
            #         print ('%s:%s' % (k, s))
            # else:
            #     print ('%s:%s' % (k, v))
        # smsMessageSid:ff75e0f84f05445ba08efdd0787ad7d0
        # dateCreated:20171125124726
        # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1


if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms("18211273433", ["1234", "5"], 1)
    # print(ret)