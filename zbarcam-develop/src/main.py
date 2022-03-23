#!/usr/bin/env python
"""
This demo can be ran from the project root directory via:
```sh
python src/main.py
```
It can also be ran via p4a/buildozer.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
import sys
import os


#  所有基于模块的使用到__file__属性的代码，在源码运行时表示的是当前脚本的绝对路径，但是用pyinstaller打包后就是当前模块的模块名（即文件名xxx.py）
#  因此需要用以下代码来获取exe的绝对路径
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print(bundle_dir)
sys.path.append(bundle_dir)
from kivy_garden.zbarcam.zbarcam import ZBarCam





if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET,Permission.CAMERA])    
    from android.storage import primary_external_storage_path
    appwd=primary_external_storage_path()+'/kivydemo'



DEMO_APP_KV_LANG = """
#:import ZBarCam kivy_garden.zbarcam.zbarcam
BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        code_types: 'QRCODE', 'EAN13'
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])

    Label:
        size_hint: None, None
        text: "中文"
"""


class DemoApp(App):

    def build(self):
        return Builder.load_string(DEMO_APP_KV_LANG)


if __name__ == '__main__':
    DemoApp().run()
