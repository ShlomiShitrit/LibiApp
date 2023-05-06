from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager

from login_page import LoginPage
from todo_page import ToDoScreen


class LibiApp(MDApp):
    """
    class for Main app
    """
    def __init__(self):
        super().__init__()
        Window.size = (350, 600)
        self.firebase_url = (
            "https://libiapp-14bee-default-rtdb.firebaseio.com/Users/.json"
        )
        self.screen_manager = MDScreenManager()

    def build(self):
        login_screen = LoginPage()
        todo_screen = ToDoScreen()

        self.sm.add_widget(login_screen)

        return self.screen_manager
    


LibiApp().run()
