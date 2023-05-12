"""
Module for the component of the home page of the application
"""

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton


class HelloLabel(MDLabel):
    """
    Label with hello message
    """

    def __init__(self, name_tup: tuple, **kwargs):
        super().__init__(**kwargs)
        self.halign = "center"
        self.text = f"Welcome {name_tup[0]} {name_tup[1]}!"
        self.halign = "center"
        self.pos_hint = {"center_x": 0.5, "center_y": 0.8}


class RaisedBtn(MDRaisedButton):
    """
    class for raised button
    """

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = "#87e6d0"
        self.text_color = (0, 0, 0, 1)
        self.font_size = "12sp"
        self.text = text
        self.size_hint = (0.4, 0.18)
