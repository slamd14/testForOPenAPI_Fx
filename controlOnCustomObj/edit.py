import requests
import json

from init import getOpenUserId
from attachmentUpload import upload

# 编辑自定义对象
def editCustomObject(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId
    objectData = {
        "_id": "64857b1884a50a0001c4a5fc",
        "name": "OpenAPI修改",
        "dataObjectApiName": "object_E3N2s__c"
    }

    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "object_data": objectData
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/update", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorDescription"]
    }

# 变更自定义对象负责人
def editCustomObjectOwner(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId
    dataObjectApiName = "object_E3N2s__c"
    ownerMobile = input("请输入想要更换的负责人的电话号码: ") # TODO
    ownerMobile = "18772554244"
    ownerId = getOpenUserId(corpAccessToken, corpId, ownerMobile)["openUserId"]
    Data = [
        {
            "objectDataId": "64857b1884a50a0001c4a5fc",
            "ownerId": [
                ownerId
            ]
        }
    ]

    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "dataObjectApiName": dataObjectApiName,
            "Data": Data
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/changeOwner", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorDescription"]
    }

# 编辑对象的附件字段
def editAttachment(corpAccessToken, corpId, openUserId):
    # 将附件上传到纷享云
    resultMap = upload.uploadAttachment(corpAccessToken, corpId, openUserId)
    mediaId = resultMap["mediaId"]
    attachment = resultMap["attachment"]

    # 参数
    currentOpenUserId = openUserId
    dataObjectApiName = "object_2d0jY__c"
    id_ = "649aafcd6961460001482a69"
    attachmentApiName = "field_ts361__c" # 附件字段的apiName

    # 编辑附件
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "object_data": {
                "_id": id_,
                attachmentApiName: [
                    attachment
                ],
                "dataObjectApiName": dataObjectApiName
            }
        }
    }
    requestBody = json.dumps(requestBody)  # Dict -> Json
    print('编辑对象附件字段时，请求数据为: ' + requestBody)
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/update", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorDescription"]
    }
