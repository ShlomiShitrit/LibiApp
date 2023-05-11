"""
Module for the home page of the application
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class HomePage(MDScreen):
    """
    Home page of the application
    """

    def __init__(self, user_name_tup, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"
        self.user_name_tup = user_name_tup
        self.md_bg_color = (51 / 255, 163 / 255, 152 / 255, 1)

        self.hello_label = MDLabel(text=f"Hello, {self.user_name_tup[0]} {self.user_name_tup[1]}!", halign="center")
        self.add_widget(self.hello_label)
