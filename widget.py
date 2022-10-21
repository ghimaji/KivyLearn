from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
#Config.set('window','resizable',1)

class MyWidget(Widget):
    pass

class WidgetApp(App):
    def build(self):

        return MyWidget()
WidgetApp().run()