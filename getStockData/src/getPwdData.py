def getPwd(name):
    initData = {
        'huaShengTong':{
            'account':'10408453',
            'logInPwd':'Wef19910926',
            'tradePwd':'324872',
        },
        'dongFang':{
            'account':'100285572',
            # 'logInPwd':'Wef19910926',
            'tradePwd':'Wef19919',
        },
        'yaoCai':{
            'account':'M396811P',
            'logInPwd':'Wef1991926',
            # 'tradePwd':'Wef19919',
        },
        
        
    }
    result = initData[(name)]

    return result