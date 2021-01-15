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

from time import sleep
def  buyStock():
    
    
    param = {
        'code':'06668',
        'num':1000,
        'isCash':False,
        'isCashAll':False,
        'numVal':'3手',
        'isFinancingAll':False,
    }
    # buyZunJia(param)
    # buyFuTu(param)
    buyHuaShengTong(param)
    # buyAiDe('01490',True, 4000)
    # buyFuYuan('01490',True, 4000)
    # buyTiger('01490',True, 4000)
    # buyDongCai('01490',True, 4000)
    # buyYingLi('01490',True, 4000)
    # buyZhangLe('01490',True, 4000)
    # buyJiaTou('01490',True, 4000)
    # buyDongFang('01490',True, 4000)
    # buyYaoCai('01490',True, 4000)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(buyStock())
    # loop.close()
    buyStock()