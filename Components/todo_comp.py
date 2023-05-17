"""
Module for to do screen components
"""

from kivy.uix.popup import Popup

from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout


class AddRowBtn(MDFillRoundFlatButton):
    """
    class for save button for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = "Add Task"
        self.font_size = "18sp"
        self.size_hint = (0.4, 0.08)
        self.pos_hint = {"center_x": 0.72, "center_y": 0.07}
        self.md_bg_color = "#146469"


class TextInputCustom(MDTextField):
    """
    class for custom text input
    """

    def __init__(self, h_txt: str, color: str = "black", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hint_text = h_txt
        self.text_color_focus = color
        self.hint_text_color_focus = color
        self.line_color_focus = color
        self.mode = "rectangle"
        self.size_hint = (1, None)
        self.cursor_color = "red"
        self.cursor_width = "2sp"
        self.padding = 15
        self.font_size = "18sp"
        self.error_color = color
        self.required = True


class AddRowPopup(Popup):
    """
    class for add row popup
    """

    def __init__(self):
        super().__init__()
        self.size_hint = (0.7, 0.7)
        self.title = "Add Task"
        main_layout = MDBoxLayout(
            orientation="vertical",
            spacing=15,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.add_widget(main_layout)

        self.task = TextInputCustom("Task", color="cyan")
        self.date = TextInputCustom("Date", color="cyan")
        self.status = TextInputCustom("Status", color="cyan")
        self.extra_col = TextInputCustom("Extra Col", color="cyan")
        # (0.5, 0.7)
        self.confirm_btn = MDFillRoundFlatButton(
            text="Confirm",
            font_size="18sp",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.75},
        )

        widgets_tup = (
            self.task,
            self.date,
            self.status,
            self.extra_col,
            self.confirm_btn,
        )
        for widget in widgets_tup:
            main_layout.add_widget(widget)
