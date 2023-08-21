import requests
import json

# 调用自定义控制器批量更新对象
def batchUpdate(corpAccessToken, corpId, openUserId):
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
                        "_id": "648948c2a1f7b70001b7eda8",
                        "name": "6.14批量修改1"
                    }, {
                        "_id": "648948c256b6200001226bdf",
                        "name": "6.14批量修改2"
                    }, {
                        "_id": "648948c205d38c00018376e7",
                        "name": "6.14批量修改3"
                    }
                ],
            }
        }
    ]
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": currentOpenUserId,
        "data": {
            "api_name": "BatchUpdateObj__c",
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