from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from app.signin.signin import SigninWindow
from app.admin.admin import AdminWindow
from app.till_operator.till_operator import OperatorWindow
from kivy.core.window import Window

Window.size = (1920, 1080)

Builder.load_file("app/signin/signin.kv")
Builder.load_file("app/admin/admin.kv")
Builder.load_file("app/till_operator/operator.kv")


class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SigninWindow(name="SigninWindow"))
        sm.add_widget(OperatorWindow(name="OperatorWindow"))
        sm.add_widget(AdminWindow(name="AdminWindow"))
        sm.current = 'SigninWindow'
        return sm


if __name__ == '__main__':
    MainApp().run()
