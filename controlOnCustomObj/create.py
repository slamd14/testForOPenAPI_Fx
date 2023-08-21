import requests
import json

def createCustomObject(corpAccessToken, corpId, openUserId):
    # 必填主对象字段
    print("请输入必填字段的内容: ") # TODO 这些必填字段只是系统预置的，更健壮的方法是先根据对象的ApiName查询对象所有的必填字段，再一个个让用户调用OpenAPI的时候填写
    dataObjectApiName = input("对象的apiName: ")
    name = input("对象的主属性: ")
    owners = openUserId # TODO 默认为创建人，对象负责人的填写要用openUserId填写，若想选择其他负责人则需要先知道对方的openUserId

    # 可选配置字段(默认值)
    triggerWorkFlow = "true" # 是否触发工作流
    triggerApprovalFlow = "true" # 是否触发审批流
    includeDetailIds = "false" # 主从对象一起创建时，是否返回从对象id列表
    optionInfo = {
        "skipFuncValidate": "false", # 是否跳过函数前验证
        "useValidationRule": "true", # 是否触发验证规则
        "isDuplicateSearch": "true" # 是否触发查重
    }
    # 可选配置字段的输入
    print("是否需要为对象创建做一些额外配置? 例如强制不触发工作流与审批流")
    print("选择是则输入true，否则输入false")
    choice = input()
    if  choice == 'true':
        triggerWorkFlow = input("是否触发工作流, 是则输入true， 否则输入false")
        triggerApprovalFlow = input("是否触发业务流，是则输入true，否则输入false")
        includeDetailIds = input("主从对象一起创建时，是否返回从对象id列表，是则输入true，否则输入false")
        optionInfo["skipFuncValidate"] = input("是否跳过函数前验证, 是则输入true，否则输入false")
        optionInfo["useValidationRule"] = input("是否触发验证规则, 是则输入true，否则输入false")
        optionInfo["isDuplicateSearch"] = input("是否触发查重，是则输入true，否则输入false")

    # 从对象 TODO OpenAPI返回系统错误, 创建从对象功能暂时不可用
    detailsObjectApiName = ''
    detailObjectNames = []
    # 是否需要同时创建从对象
    # print("是否需要同时创建从对象，是则输入true，否则输入false")
    # detailsChoice = input()
    # if detailsChoice == "true":
    #     loop = input("请输入要创建的从对象的个数: ")
    #     detailsObjectApiName = input("请输入从对象的apiName: ")
    #     for i in range(int(loop)):
    #         detailObjectNames.append(input("请输入该从对象的主属性: "))


    requestBody = {
        "corpAccessToken": corpAccessToken, # 必填
        "corpId": corpId, # 必填
        "currentOpenUserId": openUserId, # 必填
        "triggerWorkFlow": triggerWorkFlow,
        "triggerApprovalFlow": triggerApprovalFlow,
        "includeDetailIds": includeDetailIds,
        "data": {
            "optionInfo": optionInfo,
            "object_data": {
                "dataObjectApiName": dataObjectApiName, # 必填
                "name": name, # 必填
                "owner": [ # 必填
                    owners
                ]
            },
            # "details": {
            #     "dataObjectApiName": "object_XXKbi__c", # 必填
            #     "name": "1", # 必填
            #     "owner": [ # 必填
            #         owners
            #     ],
            #     "field_9EKYf__c": "object_K7hki__c" # 必填，主从关系
            # }
        }
    }
    requestBody = json.dumps(requestBody) # Dict -> Json
    resp = requests.post("https://open.fxiaoke.com/cgi/crm/custom/v2/data/create", data=requestBody, headers={
        "Content-Type": "application/json"
    })
    respMap = json.loads(resp.text) # Json -> Dict
    print(f"respMap: {respMap}")
    result = {
        "result": respMap["errorDescription"]
    }
    return result
