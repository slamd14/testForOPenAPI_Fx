"""
作废
"""
import requests
import json

def invalidCustomObject(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId
    dataObjectApiName = "object_E3N2s__c"
    objectDataId = "6486778e05d38c0001261593"

    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "object_data_id": objectDataId,
            "dataObjectApiName": dataObjectApiName
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/invalid", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorDescription"]
    }