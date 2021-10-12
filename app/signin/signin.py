from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class SigninWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/or password required[/color]'
        else:
            if username == 'admin' and password == 'admin':
                info.text = '[color=#00FF00]Logged In Successfully!!![/color]'
                self.parent.current = "OperatorWindow"
            else:
                info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'
