from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from pprint import pprint
from search import *
import os
import sys
from functools import partial


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



'''
Kv 语言特有的三个关键字：
app：总是指您的应用程序的实例。
root：指当前规则中的基本小部件/模板,root只代表其上层被<>包裹住的类
self：始终引用当前小部件
'''



class ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        #一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        super(ScreenManager, self).__init__(**kwargs)
        self.add_widget(CameraScreen())


class CameraScreen(Screen):
    pass


class DemoApp(MDApp):

    def build(self):
        return ScreenManager()

    
if __name__ == '__main__':
    #如果KV定义了一个Root Widget，它将附加到 App 的root 属性并用作应用程序的根部件，这个根部件附加完成后，再执行__init__中的代码。
    Builder.load_file( 'CameraScreen.kv' )
    DemoApp().run()
