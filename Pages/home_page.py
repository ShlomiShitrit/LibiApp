"""
Module for the home page of the application
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationLayout

from Components.home_comp import HelloLabel, SmTopAppBar, NavDrawer


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

        self.hello_label = HelloLabel(name_tup=self.user_name_tup)
        self.add_widget(self.hello_label)
        self.nav_layout = MDNavigationLayout()
        self.nav_drawer = NavDrawer()

        self.top_bar = SmTopAppBar(
            left_action_items=[["menu", lambda x: self.nav_drawer.set_state("open")]]
        )
        self.screen = MDScreen()
        self.sm = MDScreenManager()

        self.screen.add_widget(self.top_bar)
        self.sm.add_widget(self.screen)
        self.nav_layout.add_widget(self.sm)
        self.nav_layout.add_widget(self.nav_drawer)
        self.add_widget(self.nav_layout)


