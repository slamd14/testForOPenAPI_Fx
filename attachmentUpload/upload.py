import requests
import json

# 上传CRM素材文件(即将文件上传到纷享云)
def uploadAttachment(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    attachment = { # 附件相关信息
        "ext": '',
        "path": '',
        "filename": '',
    }

    url = "https://open.fxiaoke.com/media/upload"
    requestBody0 = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "type": "document",
    }
    filePath = "C:\\Users\\Administrator\\Desktop\\lalala.jpg" # 文件的绝对路径
    with open(filePath, mode="rb") as f:
        resp0 = requests.post(url=url, data=requestBody0, files={
            'media': f
        })
    respMap0 = json.loads(resp0.text)
    print(f"上传CRM素材文件结果: {respMap0['errorMessage']}")
    print(f"该文件的mediaId为: {respMap0['mediaId']}")
    mediaId = respMap0['mediaId']

    attachment["ext"] = filePath.split(".")[1]
    print(f"后缀为: {attachment['ext']}")
    attachment["path"] = mediaId
    attachment["filename"] = filePath.split("\\")[-1]
    print(f"文件名为: {attachment['filename']}")

    return {
        "mediaId": mediaId,
        "attachment": attachment
    }


