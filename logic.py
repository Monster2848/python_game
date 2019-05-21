from static_file.monster_info import name_list
from static_file.print_info import  start_info


class Monster():
    def __init__(self,类别,名称):
        # print('名称：',名称)
        attr = name_list.get(类别).get(名称)
        self.名称 = 名称
        self.等级 = 0
        self.攻击成长 = attr.get('攻击成长')
        self.防御成长 = attr.get('防御成长')
        self.血量成长 = attr.get('血量成长')
        self.攻击 = attr.get('攻击')
        self.防御 = attr.get('防御')
        self.血量 = attr.get('血量')
        self.战斗力 = 0

    def 计算属性(self,等级):
        self.等级 = 等级
        self.攻击 = self.攻击*(1+self.攻击成长)**等级
        self.防御 = self.防御*(1+self.防御成长)**等级
        self.血量 = self.血量*(1+self.血量成长)**等级
        self.战斗力 = self.攻击 + self.血量 + self.防御

    def 扣血(self,扣除血量):
        self.血量 = self.血量 - 扣除血量

    def 回血(self,回复血量):
        self.血量 = self.血量 + 回复血量

    def 扣攻(self, 攻击力):
        self.血量 = self.血量 - 攻击力

    def 加攻(self, 攻击力):
        self.血量 = self.血量 + 攻击力

    def 扣防(self, 防御):
        self.血量 = self.血量 - 防御

    def 加防(self, 防御):
        self.血量 = self.血量 + 防御

class Hero(Monster):
    pass

class GameLogic():
    def __init__(self):
        self.玩家等级 = 3
        print(start_info)
        print()

    def 显示玩家信息(self):
        史莱姆 = Hero("史莱姆","玩家·史莱姆")
        史莱姆.计算属性(self.玩家等级)
        print('【 名称：',史莱姆.名称,'| 等级：',史莱姆.等级,'| 战斗力：',史莱姆.战斗力,'】')
        print('*'*50)
        pass

    def 显示决斗战况(self,攻击对象,防守对象):
        print("{}对{}发起了攻击，造成了{}点伤害".format(攻击对象.名称,防守对象.名称,攻击对象.攻击))
        print("{}剩余血量{}".format(防守对象.名称,防守对象.血量))


    def 生成生物(self,monster_info:[]):
        生物 = Hero(monster_info[0], monster_info[1])
        生物.计算属性(monster_info[2])
        return 生物

    def 决斗(self,玩家对象,怪物对象):
        print('---',玩家对象.名称,'vs',怪物对象.名称,'---')
        while 玩家对象.血量>0 and 怪物对象.血量>0:
            玩家对象.扣血(怪物对象.攻击 - 玩家对象.防御)
            self.显示决斗战况(怪物对象,玩家对象)
            怪物对象.扣血(玩家对象.攻击 - 怪物对象.防御)
            self.显示决斗战况(玩家对象,怪物对象)

        if 玩家对象.血量>0:
            print('战斗结果：胜利')
        elif 怪物对象.血量>0:
            print('战斗结果：失败')


    def run(self):
        self.显示玩家信息()
        史莱姆 = self.生成生物(["史莱姆","玩家·史莱姆",3])
        青蛇 = self.生成生物(["蛇","凡·青蛇",5])
        self.决斗(史莱姆,青蛇)

a = GameLogic()
a.run()

