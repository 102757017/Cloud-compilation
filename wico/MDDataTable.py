from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from search import *
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen




class Nginfo_tables(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        #一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        super().__init__(**kwargs)
        self.title="已录入NG信息"
        self.name="inputed_ng_info"
        info=query_nginfo()
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
            row_data=info,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)

    
    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''
        print(instance_table, current_row)

    #更新表格中的数据
    def update(self):
        self.remove_widget(self.data_tables)
        info=query_nginfo()
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
            row_data=info,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)        
 

class DemoApp(MDApp):

    def build(self):
        scn=Screen()
        scn.add_widget(Nginfo_tables())
        return scn



if __name__=="__main__":
    #Builder.load_file( '' )
    DemoApp().run()
