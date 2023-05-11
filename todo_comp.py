"""
Module for to do screen components
"""

from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField


class ListItemWithCheckbox(OneLineIconListItem):
    """
    class for list item for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = "pencil"
        self.add_widget(IconLeftWidget(icon=self.icon))


class SaveBtn(MDFillRoundFlatButton):
    """
    class for save button for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = "Save"
        self.font_size = "18sp"
        self.size_hint = (0.4, 0.08)
        self.pos_hint = {"center_x": 0.72, "center_y": 0.07}
        self.md_bg_color = (20 / 255, 100 / 255, 105 / 255, 1)


class TaskText(MDTextField):
    """
    class for task text field for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hint_text = "Task"
        self.mode = "rectangle"
        self.size_hint = (0.75, 0.75)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.9}
        self.cursor_color = (57 / 255, 66 / 255, 143 / 255, 1)
        self.cursor_width = "2sp"
        self.padding = 15
        self.font_size = "18sp"
        self.error_color = (66 / 255, 135 / 255, 245 / 255, 1)
        self.required = True
