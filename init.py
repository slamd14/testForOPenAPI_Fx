import requests
import json
import os
from controlOnCustomObj import create, select, invalid, delete, edit, recover
from customController import batchCreateObj, batchUpdateObj
from peopleInterface import people, department
from attachmentUpload import download
def getCorpAccessTokenAndCorpId(appId, appSecret, permanentCode):
    requestBody = {
        "appId": "FSAID_131c217", # TODO 到时候换成接收的参数 test: FSAID_131c217
        "appSecret": "48815660ad1543cfa2cef610e39aaaa9", # TODO 到时候换成接收的参数 test: 48815660ad1543cfa2cef610e39aaaa9
        "permanentCode": "CF68A09859DD4EB6A141BA06419E67CF" # TODO 到时候换成接收的参数 test: CF68A09859DD4EB6A141BA06419E67CF
    }
    requestBody = json.dumps(requestBody) # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/corpAccessToken/get/V2", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text) # Json -> Dict
    result = {
        "corpAccessToken": respMap["corpAccessToken"],
        "corpId": respMap["corpId"]
    }
    return result

def getOpenUserId(corpAccessToken, corpId, mobile):
    requestBody = {
        "corpAccessToken": corpAccessToken,
        "corpId": corpId,
        "mobile": mobile
    }
    requestBody = json.dumps(requestBody) # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/user/getByMobile", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text) # Json -> Dict
    result = {
        "openUserId": respMap["empList"][0]["openUserId"]
    }
    return result

if __name__ == '__main__':
    appId = input("请输入自建应用的appId: ")
    resp1 = getCorpAccessTokenAndCorpId(appId, appSecret=input("请输入自建应用的appSecret: "), permanentCode=input("请输入自建应用的permanentCode: "))
    corpAccessToken = resp1["corpAccessToken"]
    print(f"corpAccessToken: {corpAccessToken}")
    corpId = resp1["corpId"]
    print(f"corpId: {corpId}")

    mobile = input("请输入你的电话号码: ")
    resp2 = getOpenUserId(corpAccessToken, corpId, "13597929643")
    openUserId = resp2["openUserId"]
    print(f"openUserId: {openUserId}")

    print("选择想要进行的操作: 1.对自定义对象的操作 2.调用APL自定义控制器函数批量创建对象 3.调用APL自定义控制器函数批量更新对象 4.人员接口 5.部门接口")
    choice0 = input()
    if choice0 == '1':
        print("当前为对自定义对象的操作: ")
        print(
            "选择你的操作(输入1、2、3、4...选择): 1.创建自定义对象 2.查询自定义对象列表 3.查询自定义对象详情 4.作废自定义对象 5.恢复自定义对象 6.删除自定义对象 7.编辑自定义对象普通字段 8.变更自定义对象负责人 9.变更对象的附件字段 10.下载对象的附件")
        choice = input()
        match choice:
            case "1":  # 创建自定义对象
                resp3 = create.createCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "2":  # 查询自定义对象列表
                resp3 = select.selectCustomObjectList(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "3":  # 查询自定义对象详情
                resp3 = select.selectCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "4":  # 作废自定义对象
                resp3 = invalid.invalidCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "5":  # 恢复自定义对象
                resp3 = recover.recoverCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "6":  # 删除自定义对象
                resp3 = delete.deleteCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "7":  # 编辑自定义对象
                resp3 = edit.editCustomObject(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "8":  # 变更自定义对象负责人
                resp3 = edit.editCustomObjectOwner(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "9": # 变更对象的附件字段
                resp3 = edit.editAttachment(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case "10": # 下载对象的附件字段
                resp3 = download.downloadAttachment(corpAccessToken, corpId, "npath")
                print(resp3["result"])
    elif choice0 == '2':
        print("当前为调用APL自定义控制器函数批量创建对象：")
        resp3 = batchCreateObj.batchCreate("FSAID_131c217", corpAccessToken, corpId, openUserId)
        print(resp3["result"])
    elif choice0 == '3':
        print("当前为调用APL自定义控制器函数批量更新对象：")
        resp3 = batchUpdateObj.batchUpdate(corpAccessToken, corpId, openUserId)
        print(resp3["result"])
    elif choice0 == '4':
        print("当前为人员接口：")
        print("选择你的操作(输入1、2、3、4...选择): 1.手机号查询员工 2.添加员工 3.编辑员工 4.修改员工状态 5.批量修改员工状态 6.查询员工信息 7.增量查询员工列表")
        choice = input()
        match choice:
            case '1':
                resp3 = people.selectPeopleByMobile(corpAccessToken, corpId, "13597929643")
                print(resp3["result"])
            case '2':
                resp3 = people.addPeople(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case '3':
                resp3 = people.edit(corpAccessToken, corpId)
                print(resp3["result"])
            case '4':
                resp3 = people.setStatus(corpAccessToken, corpId)
                print(resp3["result"])
            case '5':
                resp3 = people.batchSetStatus(corpAccessToken, corpId)
                print(resp3["result"])
            case '6':
                resp3 = people.selectPeopleById(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case '7':
                resp3 = people.selectPeopleOnPage(corpAccessToken, corpId)
                print(resp3["result"])
    elif choice0 == '5':
        print("当前为部门接口: ")
        print("选择你的操作(输入1、2、3、4...选择): 1.获取部门列表 2.获取部门详情 3.添加部门 4.修改部门 5.设置部门状态")
        choice = input()
        match choice:
            case '1':
                resp3 = department.getDepartmentList(corpAccessToken, corpId)
                print(resp3["result"])
            case '2':
                resp3 = department.getDepartmentDetail(corpAccessToken, corpId, 1003)
                print(resp3["result"])
            case '3':
                resp3 = department.addDepartment(corpAccessToken, corpId, openUserId)
                print(resp3["result"])
            case '4':
                resp3 = department.updateDepartment(corpAccessToken, corpId)
                print(resp3["result"])
            case '5':
                resp3 = department.setStatus(corpAccessToken, corpId)
                print(resp3["result"])
    os.system("pause") # 防止程序运行结束后自动关闭控制台
