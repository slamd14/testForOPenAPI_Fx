import requests
import json

import init


# 根据手机号查询员工
def selectPeopleByMobile(corpAccessToken, corpId, mobile):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "mobile": mobile
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/getByMobile", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["empList"]
    }

# 添加员工
def addPeople(corpAccessToken, corpId, openUserId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": openUserId,
        "includeDetailIds": True,
        "data": {
            "object_data": {
                "dataObjectApiName": "PersonnelObj",
                "status": "0",
                "is_active": True,
                "sex": "M",
                "password": "123456",
                "full_name": "啊啊啊",
                "phone": "13133333333",
                "name": "啊啊啊",
                "main_department": [
                    "1000"
                ]
            }
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/create", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }

# 修改员工
def edit(corpAccessToken, corpId):
    updateOpenUserId = init.getOpenUserId(corpAccessToken, corpId, "13133333333")["openUserId"]
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "user": {
            "openUserId": updateOpenUserId,
            "name": "姓名更改后"
        }
    }
    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/update", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorMessage"]
    }

# 设置员工状态
def setStatus(corpAccessToken, corpId):
    updateOpenUserId = init.getOpenUserId(corpAccessToken, corpId, "13133333333")["openUserId"]
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "openUserId": updateOpenUserId,
        "status":1
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/setStatus", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorMessage"]
    }

# 批量设置员工状态
def batchSetStatus(corpAccessToken, corpId):
    updateOpenUserId = init.getOpenUserId(corpAccessToken, corpId, "13133333333")["openUserId"]
    updateOpenUserId1 = init.getOpenUserId(corpAccessToken, corpId, "13597929643")["openUserId"]
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "openUserIds": [updateOpenUserId, updateOpenUserId1],
        "status": 1
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/batchSetStatus", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap["errorMessage"]
    }

# 根据openUserId查询员工信息
def selectPeopleById(corpAccessToken, corpId, openUserId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "openUserId": openUserId
    }
    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/get", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }

# 增量查询员工列表
def selectPeopleOnPage(corpAccessToken, corpId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "pageSize": 20,
        "pageNumber": 1
    }
    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/get/batchByUpdTime", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }
