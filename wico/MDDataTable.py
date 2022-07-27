from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from search import *
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen
import pprint
from kivy.logger import Logger


class Nginfo_tables(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        #一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        super().__init__(**kwargs)
        self.title="已录入NG信息"
        self.name="inputed_ng_info"

    #更新表格中的数据
    def update(self):
        self.clear_widgets()
        info=query_nginfo()
        info=list(info)
        if len(info)>0:
            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("车型", dp(20)),
                    ("座椅型号", dp(55)),
                    ("WICO番号", dp(25)),
                    ("TS番号", dp(45)),
                    ("零件名称", dp(50)),
                    ("不良信息", dp(50)),
                    ("维修方法", dp(50)),
                    ("批次号", dp(30)),
                    ("生产日期", dp(20)),
                ],
            )
            self.add_widget(self.data_tables) 
            for i in info:
                Logger.info("源数据:"+str(i))
                self.data_tables.add_row(i)
                Logger.info("MDDataTable追加完成1条数据")
 

class DemoApp(MDApp):

    def build(self):
        scn=Screen()
        scn.add_widget(Nginfo_tables())
        return scn



if __name__=="__main__":
    #Builder.load_file( '' )
    DemoApp().run()
