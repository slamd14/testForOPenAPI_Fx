import requests
import json

# 调用自定义控制器批量创建对象
def batchCreate(appId, corpAccessToken, corpId, openUserId):
    # 参数
    corpAccessToken = corpAccessToken
    corpId = corpId
    currentOpenUserId = openUserId

    # 自定义控制器参数
    parameters = [
        {
            "name": "inputData", # 参数名称
            "type": "Map", # 参数类型,
            "value": {
                "dataList": [
                    {
                        "name": "6.14哈哈100",
                        "owner": openUserId # TODO 在自定义控制器中需要将此openUserId转为FsId
                    }, {
                        "name": "6.14哈哈200",
                        "owner": openUserId
                    }, {
                        "name": "6.14哈哈300",
                        "owner": openUserId
                    }
                ],
                "appId": appId
            }
        }
    ]
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "api_name": "controllerForOpenAPI__c",
            "parameters": parameters
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/v2/special/function", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }