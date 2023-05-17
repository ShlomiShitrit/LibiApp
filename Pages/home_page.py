"""
Module for the home page of the application
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout


from Components.home_comp import HelloLabel
from Components.general_comp import NavLayout

from Resources.home_resources import (
    HOME_PAGE_NAME,
    HP_MAIN_LAYOUT_ORIENTATION,
    HP_MAIN_LAYOUT_PADDING,
    HP_MAIN_LAYOUT_SPACING,
    TOP_BAR_TITLE,
)

from Constants.home_constants import HP_BG_COLOR


class HomePage(MDScreen):
    """
    Home page of the application
    """

    def __init__(self, user_name_tup, main_app, **kwargs):
        super().__init__(**kwargs)
        self.name = HOME_PAGE_NAME
        self.user_name_tup = user_name_tup
        self.md_bg_color = HP_BG_COLOR
        main_layout = MDBoxLayout(
            orientation=HP_MAIN_LAYOUT_ORIENTATION,
            padding=HP_MAIN_LAYOUT_PADDING,
            spacing=HP_MAIN_LAYOUT_SPACING,
        )
        sec_layout = MDFloatLayout()
        main_layout.add_widget(sec_layout)
        self.add_widget(main_layout)

        self.hello_label = HelloLabel(name_tup=self.user_name_tup)
        self.nav_layout = NavLayout(main_app=main_app, title_txt=TOP_BAR_TITLE)
        self.add_widget(self.hello_label)
        self.add_widget(self.nav_layout)
