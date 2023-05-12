"""
Module for the home page of the application
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout

from home_comp import HelloLabel


class HomePage(MDScreen):
    """
    Home page of the application
    """

    def __init__(self, user_name_tup, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"
        self.user_name_tup = user_name_tup
        self.md_bg_color = (51 / 255, 163 / 255, 152 / 255, 1)
        main_layout = MDBoxLayout(
            orientation="vertical", padding="10dp", spacing="10dp"
        )
        sec_layout = MDFloatLayout()
        main_layout.add_widget(sec_layout)
        self.add_widget(main_layout)

        self.hello_label = HelloLabel(name_tup=self.user_name_tup, font_style="H2")
        self.add_widget(self.hello_label)
