"""
The main module
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from login_page import LoginPage
from todo_page import ToDoScreen
from home_page import HomePage


class LibiApp(MDApp):
    """
    class for Main app
    """

    def __init__(self):
        super().__init__()
        Window.size = (350, 600)
        self.screen_manager = MDScreenManager()
        self.home_screen = None

    def build(self):
        login_screen = LoginPage(self)
        todo_screen = ToDoScreen()
        self.home_screen = HomePage(login_screen.user_name_tup)
        self.screen_manager.add_widget(login_screen)
        self.screen_manager.add_widget(todo_screen)
        self.screen_manager.add_widget(self.home_screen)
        return self.screen_manager


def main():
    """
    The main function
    """
    LibiApp().run()


if __name__ == "__main__":
    main()
