"""
Module for the component of the home page of the application
"""

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel


class HelloLabel(MDLabel):
    """
    Label with hello message
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Hello, world!" # enter name of user here
        self.halign = "center"