import requests
import json

# 查询自定义对象列表
def selectCustomObjectList(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId
    search_query_info = {
        "offset": 0.0,
        "limit": 30.0,
        "filters": [] # 过滤条件
    }
    dataObjectApiName = "object_E3N2s__c"

    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "search_query_info": search_query_info,
            "dataObjectApiName": dataObjectApiName
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/query", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text) # Json -> Dict
    # print(f"respMap: {respMap}")
    return {
        "result": respMap
    }

# 查询自定义对象详情
def selectCustomObject(corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId
    data = {
        "objectDataId": "64857b1884a50a0001c4a5fc",
        "dataObjectApiName": "object_E3N2s__c"
    }

    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": data
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/get", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }