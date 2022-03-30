from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from pprint import pprint
import time
from search import *
from barcode_analysis import analysis_code

import os
import sys


#  所有基于模块的使用到__file__属性的代码，在源码运行时表示的是当前脚本的绝对路径，但是用pyinstaller打包后就是当前模块的模块名（即文件名xxx.py）
#  因此需要用以下代码来获取exe的绝对路径
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print(bundle_dir)
sys.path.append(bundle_dir)
from kivy_garden.zbarcam.zbarcam import ZBarCam
from kivy_garden.xcamera import XCamera


from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET,Permission.CAMERA])    
    from android.storage import primary_external_storage_path
    appwd=primary_external_storage_path()+'/WicoMag'



KV = '''
<KitchenSinkBottomSheetItemButton@AnchorLayout>
    size_hint_y: None
    height: "32dp"
    anchor_x: "center"
    text: ""
    callback: None
    MDRaisedButton:
        text: root.text
        on_release: root.callback()

<MYLabel@MDLabel>
    size_hint_y: None
    pos_hint: {"center_x": .4, "center_y": .5}
    height: self.texture_size[1]
    font_style: "Body2"
    halign: "left"

<MYDropDownItem@MDDropDownItem>
    text: ""
    font_style: "Body2"
    pos_hint: {"center_x": .5, "center_y": .5}

  
ScreenManager:
    MainScreen:
    CameraScreen:

<MainScreen>:
    name: 'main'
       
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        MDBottomNavigation:
            id: panel

            MDBottomNavigationItem:
                name: "files1"
                text: "客户不良信息录入"
                icon: "language-python"

                BoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "产品条码/标签："
                            
                        MDRectangleFlatButton:
                            id:Lot1
                            text: '点击扫码'  
                            #user_font_size: "15sp"
                            size_hint: None,None
                            size:300,40
                            on_press: root.manager.current = 'camera'
                            on_text: app.decode(self.text)
                            
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "产品类型："

                        MYLabel:
                            id: PartType1



                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "WICO番号："

                        MYLabel:
                            id: WicoPartNumber1



                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "TS-GSK番号："

                        MYLabel:
                            id: TsPartNumber1

                    AsyncImage:
                        source:"https://img95.699pic.com/element/40106/9421.png_300.png"
                        size:self.texture_size

                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "产品名称："

                        MYLabel:
                            id: PartName1

                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "机种："

                        MYDropDownItem:
                            id: CarModel1
                            on_release: app.show_model1()
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "座椅型号："

                        MYDropDownItem:
                            id: SeatModel1
                            on_release: app.show_SeatModel1() 

                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "不良内容："

                        MDTextField:
                            id: NgInfo1
                            hint_text: "选单内没有时手动输入"
                            
                        MDIconButton:
                            pos_hint: {"center_x": .5, "center_y": .5}
                            icon: "language-python"
                            user_font_size: "20sp"
                            on_release: app.show_ng_information1()

                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: "10dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MYLabel:
                            text: "维修方法："

                        MDTextField:
                            id: RepairMethod1
                            text:""
                            hint_text: "选单内没有时手动输入"
                            
                        MDIconButton:
                            pos_hint: {"center_x": .5, "center_y": .5}
                            icon: "language-python"
                            user_font_size: "20sp"
                            on_release: app.show_repair_method1()
                        
                            
                    KitchenSinkBottomSheetItemButton:
                        id: upload1
                        text: "提交"
                        callback: lambda: app.upload()
                        pos_hint: {"center_x": .5, "center_y": .55}



            MDBottomNavigationItem:
                name: "files2"
                text: "已录入信息查询"
                icon: "language-cpp"

                MDLabel:
                    font_style: "Body1"
                    text: "I programming of C++"
                    halign: "center"
<CameraScreen>:
    name: 'camera'
    #:import ZBarCam kivy_garden.zbarcam.zbarcam
    #:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        #code_types: ZBarSymbol.CODE128,ZBarSymbol.QRCODE
        #这里的分辨率必须填写手机摄像头支持的分辨率，随便填会导致在电脑上可以运行，但是手机app闪退
        resolution: 1280,960
    
    MDLabel:
        id:barcode
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
        on_text: app.goback2(self.text)

    MDLabel:
        size: self.texture_size[0], 50
        font_name:"DroidSansFallback.ttf"
        text: "条形码必须水平方向或垂直方向扫描，二维码任意方向均可扫描"

            
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: app.goback()
                    
'''

class MainScreen(Screen):
    pass


class CameraScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(CameraScreen(name='camera'))
sm.current ='main'


class Test(MDApp):

    def build(self):
        screen = Builder.load_string(KV)
        #self.root.manager.current = 'main'
        return screen
        

    def show_model1(self):
        bs_menu_1 = MDListBottomSheet()
        scroll = ScrollView()
        #CarModel=["2FW","2HY","2VH","2VP","2WB","2YC","2YN","2YS","2YT","3BS"]
        WicoPartNumber=self.root.get_screen('main').ids.WicoPartNumber1.text
        print(WicoPartNumber)
        Supplier,PartType,WicoPartNumber,TsPartNumber,PartName,PartPicUrl,CarModel=get_CarModelBybar(WicoPartNumber)
        print(PartType)
        for item in CarModel:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_model1(y))                
        bs_menu_1.open()
    def select_model1(self, *args):
        self.root.get_screen('main').ids.CarModel1.text=args[0]
        self.root.get_screen('main').ids.SeatModel1.text=""
        self.root.get_screen('main').ids.NgInfo1.text=""
        self.root.get_screen('main').ids.RepairMethod1.text=""

    def show_SeatModel1(self):
        bs_menu_1 = MDListBottomSheet()
        scroll = ScrollView()
        WicoPartNumber=self.root.get_screen('main').ids.WicoPartNumber1.text
        CarModel=self.root.get_screen('main').ids.CarModel1.text
        SeatModel=get_SeatModelBybar(WicoPartNumber,CarModel)
        #SeatModel=["手动-前排-左席座椅","手动-前排-右席座椅"]
        for item in SeatModel:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_SeatModel1(y))                
        bs_menu_1.open()
    def select_SeatModel1(self, *args):
        self.root.get_screen('main').ids.SeatModel1.text=args[0]
        self.root.get_screen('main').ids.NgInfo1.text=""
        self.root.get_screen('main').ids.RepairMethod1.text=""

    def show_ng_information1(self):
        bs_menu_1 = MDListBottomSheet()
        PartType=self.root.get_screen('main').ids.PartType1.text
        NgInfo=get_NgInfo(PartType)
        #NgInfo=["异音","震动"]
        for item in NgInfo:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_ng_information1(y))
        bs_menu_1.open()
    def select_ng_information1(self, *args):
        self.root.get_screen('main').ids.NgInfo1.text=args[0]
        self.root.get_screen('main').ids.RepairMethod1.text=""
        
    def show_repair_method1(self):
        bs_menu_1 = MDListBottomSheet()
        PartType=self.root.get_screen('main').ids.PartType1.text
        NgInfo=self.root.get_screen('main').ids.NgInfo1.text
        RepairMethod=get_RepairMethod(PartType,NgInfo)
        #RepairMethod=["涂油","换电机"]
        for item in RepairMethod:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_repair_method1(y))
        bs_menu_1.open()
    def select_repair_method1(self, *args):
        self.root.get_screen('main').ids.RepairMethod1.text=args[0]

        

 

    def show_type(self):
        bs_menu_1 = MDListBottomSheet()
        list1=["手动滑轨","电动滑轨","电动支架","调角器"]
        for item in list1:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_type(y))
        bs_menu_1.open()
    def select_type(self, *args):
        self.root.get_screen('main').ids.PartType1.text=args[0]

        
    def show_wico_number(self):
        bs_menu_1 = MDListBottomSheet()
        list1=["21-3742412-2","21-3742421-2","21-3742431-2","21-3742441-2"]
        for item in list1:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_wico_number(y))
        bs_menu_1.open()
    def select_wico_number(self, *args):
        self.root.get_screen('main').ids.WicoPartNumber1.text=args[0]
        

    def show_ts_number(self):
        bs_menu_1 = MDListBottomSheet()
        list1=["81660-T391-A110-M1-0001","81670-T201-X110-M1-0001"]
        for item in list1:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_ts_number(y))
        bs_menu_1.open()
    def select_ts_number(self, *args):
        self.root.get_screen('main').ids.TsPartNumber1.text=args[0]

        

    def show_part_name(self):
        bs_menu_1 = MDListBottomSheet()
        list1=["SLIDE ADJR OUT L,FR SEAT（HEI）","SLIDE ADJR INN L,FR SEAT（HEI）"]
        for item in list1:
            bs_menu_1.add_item(item,callback=lambda x, y=item: self.select_part_name(y))
        bs_menu_1.open()
    def select_part_name(self, *args):
        self.root.get_screen('main').ids.PartName1.text=args[0]
        


    
    def upload(self):
        if self.root.get_screen('main').ids.RepairMethod1.text !="" and self.root.get_screen('main').ids.RepairMethod1.text !="" and self.root.get_screen('main').ids.SeatModel1.text!="":
            # 格式化成2016-03-20 11:45:39形式
            NgTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            CarModel=self.root.get_screen('main').ids.CarModel1.text
            SeatModel=self.root.get_screen('main').ids.SeatModel1.text
            WicoPartNumber=self.root.get_screen('main').ids.WicoPartNumber1.text
            TsPartNumber=self.root.get_screen('main').ids.TsPartNumber1.text
            PartName=self.root.get_screen('main').ids.PartName1.text
            PartType=self.root.get_screen('main').ids.PartType1.text
            Supplier=self.Supplier1
            NgInfo=self.root.get_screen('main').ids.NgInfo1.text
            RepairMethod=self.root.get_screen('main').ids.RepairMethod1.text
            Lot=self.root.get_screen('main').ids.Lot1.text
            ManufactureDate=self.ManufactureDate1
            Production_Line=self.Production_Line1
            if search_barcode(Lot)==False:
                uploade_ngrecord(NgTime,
                                 CarModel,
                                 SeatModel,
                                 WicoPartNumber,
                                 TsPartNumber,
                                 PartName,
                                 PartType,
                                 Supplier,
                                 NgInfo,
                                 RepairMethod,
                                 Lot,
                                 ManufactureDate,
                                 Production_Line,
                                 0)
                toast("数据上传完成")
            else:
                toast("此批次号的产品此前已经上传过不良信息了，请勿重复上传")
        else:
            toast("请将表单填写完整后再上传")

    def goback2(self,*args):
        r_text=args[0][2:-1]
        if len(r_text)!=0:
            self.root.get_screen('main').ids.Lot1.text=r_text
            self.root.get_screen('camera').ids.zbarcam.stop
            self.root.current = 'main'

    def decode(self,*args):
        barcode=args[0]
        WicoPartNumber,Production_Line,ManufactureDate=analysis_code(barcode)
        Supplier,PartType,WicoPartNumber,TsPartNumber,PartName,PartPicUrl,CarModel=get_CarModelBybar(WicoPartNumber)
        self.root.get_screen('main').ids.PartType1.text=PartType
        self.root.get_screen('main').ids.WicoPartNumber1.text=WicoPartNumber
        self.root.get_screen('main').ids.TsPartNumber1.text=TsPartNumber
        self.root.get_screen('main').ids.PartName1.text=PartName
        self.root.get_screen('main').ids.CarModel1.text=""
        self.root.get_screen('main').ids.SeatModel1.text=""
        self.root.get_screen('main').ids.NgInfo1.text=""
        self.root.get_screen('main').ids.RepairMethod1.text=""
        self.Supplier1=Supplier
        self.Production_Line1=Production_Line
        self.ManufactureDate1=ManufactureDate

    def goback(self):
        self.root.get_screen('camera').ids.zbarcam.stop
        self.root.current = 'main'
        #self.root.get_screen('main').ids.PartType1.text="电动滑轨"
        #self.root.get_screen('main').ids.WicoPartNumber1.text="23-4739141-2"
        #self.root.get_screen('main').ids.Lot1.text="2TLA8E3C33B8W"

            
    def analysis_code(self,*args):
        analysis_code(args[0])

        

Test().run()
