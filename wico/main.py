from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from pprint import pprint
from search import *
import os
import sys
from functools import partial
from synch import sync_all
from kivy.logger import Logger
from pathlib import Path


#  所有基于模块的使用到__file__属性的代码，在源码运行时表示的是当前脚本的绝对路径，但是用pyinstaller打包后就是当前模块的模块名（即文件名xxx.py）
#  因此需要用以下代码来获取exe的绝对路径


if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["WICO_ROOT"] = sys._MEIPASS
else:
    os.environ["WICO_ROOT"] = str(Path(__file__).parent)

KV_DIR = f"{os.environ['WICO_ROOT']}"
sys.path.append(KV_DIR)
Logger.info("Main_KV_DIR:"+KV_DIR)


from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET,Permission.CAMERA])    
    from android.storage import primary_external_storage_path
    appwd=primary_external_storage_path()+'/WicoMag'



'''
Kv 语言特有的三个关键字：
app：总是指您的应用程序的实例。
root：指当前规则中的基本小部件/模板,root只代表其上层被<>包裹住的类
self：始终引用当前小部件
'''

from MainScreen import MainScreen
from CameraScreen import CameraScreen
from OutPutInfo import OutPutInfo
from EnterNgIfo import EnterNgIfo
from Manual_input import Manual_input
from MDDataTable import Nginfo_tables
from Others import Others

class ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        #一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        super(ScreenManager, self).__init__(**kwargs)
        #self.EnterNgIfo=EnterNgIfo()
        #self.Manual_input=Manual_input()
        #self.OutPutInfo=OutPutInfo()
        self.Nginfo_tables=Nginfo_tables()
        #电脑必须连接摄像头，否则会报错
        #self.CameraScreen=CameraScreen()
        #self.Others=Others()
        
        self.scn=MainScreen()
        #self.scn.ids.tab.add_widget(self.EnterNgIfo)
        #self.scn.ids.tab.add_widget(self.Manual_input)
        #self.scn.ids.tab.add_widget(self.OutPutInfo)
        self.scn.ids.tab.add_widget(self.Nginfo_tables)
        #self.scn.ids.tab.add_widget(self.Others)
        
        self.add_widget(self.scn)
        #self.add_widget(self.CameraScreen)
        f=sync_all()
        if f==True:
            toast("数据已上传到服务器")
        else:
            toast("数据上传到服务器失败，稍后重新启动app将再次尝试上传")

class DemoApp(MDApp):

    def build(self):
        return ScreenManager()

    def start_cam(self):
        self.root.current = 'camera'
        self.root.CameraScreen.ids.zbarcam.ids.xcamera.play=True

    def goback(self):       
        self.root.CameraScreen.ids.zbarcam.stop
        self.root.CameraScreen.ids.zbarcam.ids.xcamera.play=False
        self.root.current = 'main'

        #self.root.EnterNgIfo.ids.PartType1.text="电动滑轨"
        #self.root.EnterNgIfo.ids.WicoPartNumber1.text="23-4739141-2"
        #self.root.EnterNgIfo.ids.Lot1.text="2TLA8E3C33B8W"

    def goback2(self,*args):
        r_text=args[0][2:-1]
        if len(r_text)!=0:
            self.root.EnterNgIfo.ids.Lot1.text=r_text
            self.root.CameraScreen.ids.zbarcam.stop
            self.root.CameraScreen.ids.zbarcam.ids.xcamera.play=False
            self.root.current = 'main'

        
    
if __name__ == '__main__':
    Builder.load_file( f"{os.environ['WICO_ROOT']}/mainscreen.kv" )
    Builder.load_file( f"{os.environ['WICO_ROOT']}/CameraScreen.kv" )
    DemoApp().run()
