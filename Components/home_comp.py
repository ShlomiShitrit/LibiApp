"""
Module for the component of the home page of the application
"""

from kivymd.uix.label import MDLabel
from Resources.home_resources import HELLO_LABEL_HALIGN, H3_FONT_STYLE
from Constants.home_constants import HELLO_LABEL_POS_CX, HELLO_LABEL_POS_CY


class HelloLabel(MDLabel):
    """
    Label with hello message
    dest: home page
    """

    def __init__(self, name_tup: tuple, **kwargs):
        super().__init__(**kwargs)
        self.halign = HELLO_LABEL_HALIGN
        self.text = f"Welcome {name_tup[0]} {name_tup[1]}!"
        self.pos_hint = {"center_x": HELLO_LABEL_POS_CX, "center_y": HELLO_LABEL_POS_CY}
        self.font_style = H3_FONT_STYLE
