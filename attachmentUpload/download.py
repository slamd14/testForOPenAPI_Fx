import requests
import json

def downloadAttachment(corpAccessToken, corpId, npath):
    url = "https://open.fxiaoke.com/media/download"
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "mediaTypeDesc": "DOCUMENT", # 使用igonreMediaIdConvert参数时需传DOCUMENT
        "igonreMediaIdConvert": True, # 传入是否忽略mediaId代替npath；true：传入的mediaId值为npath；false or null 传入的mediaId值为mediaId
        "mediaId": "N_202306_27_f4fd33bf7b3a4e75bb38d0dd0a9be2bd.webp.jpg" # npath
    }
    filePath = "C:\\Users\\Administrator\\Desktop\\tt\\"  # 文件的绝对路径
    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post(url=url, data=requestBody, headers={
        "Content-Type": "application/json"
    })
    print(resp.headers)
    contentDisposition = resp.headers["Content-Disposition"]
    filename = contentDisposition.split(";")[-1]
    filePath += filename
    # 写入磁盘
    with open (filePath, "wb") as f:
        f.write(resp.content)
    return {
        "result": "成功下载附件"
    }