"""
The main module
"""

import os

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from Pages.login_page import LoginPage
from Pages.todo_page import ToDoScreen
from Pages.home_page import HomePage


class LibiApp(MDApp):
    """
    class for Main app
    """

    def __init__(self):
        super().__init__()
        Window.size = (350, 600)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.screen_manager = MDScreenManager()
        self.home_screen = None
        print(os.getenv("FIREBASE_API_KEY"))
        print(os.getenv("FIREBASE_API_AUTH"))
        print(os.getenv("FIREBASE_DB_URL"))

    def build(self):
        login_screen = LoginPage(self)
        todo_screen = ToDoScreen(main_app=self)
        self.home_screen = HomePage(
            user_name_tup=login_screen.user_name_tup, main_app=self
        )
        self.screen_manager.add_widget(login_screen)
        self.screen_manager.add_widget(todo_screen)
        self.screen_manager.add_widget(self.home_screen)
        # self.screen_manager.current = "todo"
        return self.screen_manager


def main():
    """
    The main function
    """
    LibiApp().run()


if __name__ == "__main__":
    main()
