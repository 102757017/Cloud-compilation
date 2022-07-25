from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
import random
from functools import partial
from kivy.uix.boxlayout import BoxLayout

'''
Kv 语言特有的三个关键字：
app：总是指您的应用程序的实例。
root：指当前规则中的基本小部件/模板,root只代表其上层被<>包裹住的类
self：始终引用当前小部件
'''


KV='''
<OneScreen>
    BoxLayout:
        id:lay1
        orientation: "vertical"
        spacing: "10dp"
        
        MDFlatButton:
            id: button1
            text:"button1"
            icon: "data/logo/kivy-icon-256.png"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: 
                root.button1_fuc()
                print(app.root.ids.keys())
'''
 

#kv代码中被<>包裹住的是某个class的名字，这个class需在python代码中声明，它们代表同一个class。
class OneScreen(Screen):
    def __init__(self, **kwargs):
        #一定要注意这里要加super，才能把现有的新初始化方法覆盖掉继承来的旧初始化方法
        super(OneScreen, self).__init__(**kwargs)
        self.add_widget(MDFlatButton(text='我是__init__函数追加的按钮', pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        print(self.ids.button1.text)


    def button1_fuc(self):
        self.btn2 = MDFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.ids.lay1.add_widget(self.btn2)
        '''
        #特定的操作背后都绑定了特定的回调函数, 一般有两种类型:
        1.绑定一个是事件(即这个时间发生了,就会进而调用这个回调函数,eg: on_press: ****) .
        事件的回调函数则只需要传入一个参数值(the object).
        2.绑定一个属性(即当属性的value发生变化是,回调函数就会被调用).
        属性的回调函数需要传入两个参数(the object和属性的新值);
        #要在文本更改时运行回调，可以将text属性绑定一个回调函数
        '''
        self.btn2.bind(on_press=self.button2_fuc)

        self.btn3 = MDFlatButton(text='我可以传递参数', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.ids.lay1.add_widget(self.btn3)
        self.btn3.bind(on_press=partial(self.button3_fuc, "我是参数{}".format(random.randint(0,9))))

    
    def button2_fuc(self,*args):
        self.ids.button1.text="I am changed {}".format(random.randint(0,9))
        self.btn2.text="the newest button changed too {}".format(random.randint(0,9))

    def button3_fuc(self,*args):
        self.btn3.text=args[0]
 
class TestApp(MDApp):
    def build(self):
        return OneScreen()
 


if __name__ == '__main__':
    #如果KV定义了一个Root Widget，它将附加到 App 的root 属性并用作应用程序的根部件，这个根部件附加完成后，再执行__init__中的代码。
    Builder.load_string(KV)
    TestApp().run()