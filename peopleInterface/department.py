import requests
import json

# 获取部门列表
def getDepartmentList(corpAccessToken, corpId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/department/list", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }

# 获取部门详情
def getDepartmentDetail(corpAccessToken, corpId, departmentId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "departmentId": departmentId
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/department/detail", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }

# 添加部门
def addDepartment(corpAccessToken, corpId, openUserId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "currentOpenUserId": openUserId,
        "includeDetailIds": True,
        "data": {
            "object_data": {
                "dataObjectApiName": "DepartmentObj",
                "name": "测试OpenAPI部门",
                "parent_id": ["999999"]
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

# 修改部门
def updateDepartment(corpAccessToken, corpId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "department": {
            "id": 1010,
            "name": "OpenAPI修改后的测试部门"
        }
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/department/update", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }

# 设置部门状态
def setStatus(corpAccessToken, corpId):
    # 请求参数
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "departmentId": 1010,
        "status": 1
    }

    requestBody = json.dumps(requestBody)  # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/department/setStatus", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text)  # Json -> Dict
    return {
        "result": respMap
    }