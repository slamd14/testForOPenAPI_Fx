import os
from init import getCorpAccessTokenAndCorpId, getOpenUserId

if __name__ == '__main__':
    resp1 = getCorpAccessTokenAndCorpId(appId=input("请输入自建应用的appId: "),
                                        appSecret=input("请输入自建应用的appSecret: "),
                                        permanentCode=input("请输入自建应用的permanentCode: "))
    corpAccessToken = resp1["corpAccessToken"]
    print(f"corpAccessToken: {corpAccessToken}")
    corpId = resp1["corpId"]
    print(f"corpId: {corpId}")

    mobile = input("请输入你的电话号码: ")
    resp2 = getOpenUserId(corpAccessToken, corpId, "13597929643")
    openUserId = resp2["openUserId"]
    print(f"openUserId: {openUserId}")
    os.system("pause")  # 防止程序运行结束后自动关闭控制台