"""
Module for general components
"""

from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer,
    MDNavigationDrawerItem,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
)

from Resources.general_resources import (
    H6_FONT_STYLE,
    NAV_DRAWER_TYPE,
    NAV_DRAWER_BG_COLOR,
    HOME_DRAWER_TEXT,
    HOME_DRAWER_ICON,
    TODO_DRAWER_TEXT,
    TODO_DRAWER_ICON,
    NAV_ITEM_THEME_TEXT_COLOR,
    NAV_ITEM_BG_COLOR,
    NAV_HEADER_TITLE,
    NAV_HEADER_TEXT,
    NAV_HEADER_SPACING,
    NAV_HEADER_PADDING_12,
    NAV_HEADER_PADDING_36,
)

from Constants.general_constants import (
    TOP_BAR_ELEVATION,
    TOP_BAR_BG_COLOR,
    TOP_BAR_POS_TOP,
    NAV_DRAWER_ELEVATION,
    NAV_ITEM_TXT_COLOR,
    NAV_ITEM_ELEVATION,
    NAV_HEADER_PADDING,
)


class NavItem(MDNavigationDrawerItem):
    """
    class for navigation drawer item
    dest: NavDrawer
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_color = NAV_ITEM_TXT_COLOR
        self.theme_text_color = NAV_ITEM_THEME_TEXT_COLOR
        self.font_style = H6_FONT_STYLE
        self.md_bg_color = NAV_ITEM_BG_COLOR
        self.elevation = NAV_ITEM_ELEVATION


class NavHeader(MDNavigationDrawerHeader):
    """
    class for navigation drawer header
    dest: NavDrawer
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = NAV_HEADER_TITLE
        self.text = NAV_HEADER_TEXT
        self.spacing = NAV_HEADER_SPACING
        self.padding = (
            NAV_HEADER_PADDING_12,
            NAV_HEADER_PADDING,
            NAV_HEADER_PADDING,
            NAV_HEADER_PADDING_36,
        )


class NavDrawer(MDNavigationDrawer):
    """
    class for navigation drawer
    dest: NavLayout
    """

    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.type = NAV_DRAWER_TYPE
        self.md_bg_color = NAV_DRAWER_BG_COLOR
        self.elevation = NAV_DRAWER_ELEVATION
        self.menu = MDNavigationDrawerMenu()
        self.add_widget(self.menu)
        self.header = NavHeader()
        self.menu.add_widget(self.header)
        self.home_drawer = NavItem(text=HOME_DRAWER_TEXT, icon=HOME_DRAWER_ICON)
        self.home_drawer.bind(on_release=lambda x: self.switch_screen(main_app, "home"))
        self.menu.add_widget(self.home_drawer)
        self.todo_drawer = NavItem(text=TODO_DRAWER_TEXT, icon=TODO_DRAWER_ICON)
        self.todo_drawer.bind(on_release=lambda x: self.switch_screen(main_app, "todo"))
        self.menu.add_widget(self.todo_drawer)

    def switch_screen(self, main_app, screen_name):
        """
        Switches the screen to the screen name passed
        """
        main_app.screen_manager.current = screen_name
        self.set_state("close")


class SmTopAppBar(MDTopAppBar):
    """
    class for top app bar
    dest: NavLayout
    """

    def __init__(self, title_txt, **kwargs):
        super().__init__(**kwargs)
        self.title = title_txt
        self.elevation = TOP_BAR_ELEVATION
        self.md_bg_color = TOP_BAR_BG_COLOR
        self.pos_hint = {"top": TOP_BAR_POS_TOP}


class NavLayout(MDNavigationLayout):
    """
    class for navigation layout
    dest: home page
    """

    def __init__(self, main_app, title_txt, **kwargs):
        super().__init__(**kwargs)
        self.top_bar = SmTopAppBar(
            title_txt=title_txt,
            left_action_items=[
                [
                    "menu",
                    lambda x: self.nav_drawer.set_state("toggle"),
                ]
            ],
        )

        self.nav_drawer = NavDrawer(main_app)
        self.screen = MDScreen()
        self.sm = MDScreenManager()

        self.screen.add_widget(self.top_bar)
        self.sm.add_widget(self.screen)
        self.add_widget(self.sm)
        self.add_widget(self.nav_drawer)
