import asyncio
from src.zunJia import buyZunJia
from src.fuTu import buyFuTu
from src.huaShengTong import buyHuaShengTong
from src.aiDe import buyAiDe
from src.fuYuan import buyFuYuan
from src.tiger import buyTiger
from src.dongCai import buyDongCai
from src.yingLi import buyYingLi
from src.zhangLe import buyZhangLe
from src.jiaTou import buyJiaTou
from src.dongFang import buyDongFang
from src.yaoCai import buyYaoCai
from src.youYu import buyYouYu
from src.aErFa import buyAErFa
from src.changQiao import buyChangQiao
from src.yiSheng import buyYiSheng
from src.hengZhengTong import buyHengZhengTong
from src.guoDu import buyGuoDu
from src.yiTaoJin import buyYiTaoJin
from src.liTongTianXia import buyLiTongTianXia
from src.fangDe import buyFangDe
from src.xueYing import buyXueYing
from src.ruiFeng import buyRuiFeng

from src.test import tryTest
from time import sleep
def  buyStock():
    
    param = {
        'setIndex':0,
        'code':'06668',
        'num':1000,
        'isCash':True,
        'isCashAll':False,
        'numVal':'1手',
        'isFinancingAll':False,
    }
    # buyZunJia(param)
    # buyFuTu(param)
    # buyHuaShengTong(param)
    # buyAiDe(param)
    # buyFuYuan(param)
    # buyTiger(param)
    # buyDongCai(param)
    # buyYingLi(param)
    # buyZhangLe(param)
    # buyJiaTou(param)
    # buyDongFang(param)
    # buyYaoCai(param)
    # buyYouYu(param)
    # buyAErFa(param)
    # buyAErFa(param)
    # buyChangQiao(param)
    # buyYiSheng(param)
    # buyHengZhengTong(param)
    # buyGuoDu(param)
    # buyYiTaoJin(param)
    # buyLiTongTianXia(param)
    # buyFangDe(param)
    # buyXueYing(param)
    # buyRuiFeng(param)


    tryTest(param)
    
    
    

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(buyStock())
    # loop.close()
    buyStock()