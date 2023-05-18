"""
Module for to do screen components
"""

from kivy.uix.popup import Popup

from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dropdownitem import MDDropDownItem  
from kivymd.uix.menu import MDDropdownMenu


from Resources.todo_resources import (
    ADD_ROW_BTN_TXT,
    ADD_ROW_FONT_SIZE,
    ADD_ROW_BG_COLOR,
    TEXT_INPUT_MODE,
    TEXT_INPUT_CURSOR_COLOR,
    TEXT_INPUT_CURSOR_WIDTH,
    TEXT_INPUT_FONT_SIZE,
    TEXT_INPUT_COLOR_DEFAULT,
    POPUP_TITLE,
    POPUP_MAIN_LAYOUT_ORIENTATION,
    TEXT_INPUT_COLOR,
    TASK_TEXT,
    DATE_TEXT,
    STATUS_TEXT,
    EXTRA_TEXT,
    COMFIRM_BTN_TXT,
    CONFIRM_FONT_SIZE,
)

from Constants.todo_constants import (
    ADD_ROW_BTN_SIZE_HINT,
    ADD_ROW_BTN_CX,
    ADD_ROW_BTN_CY,
    TEXT_INPUT_SIZE_HINT,
    TEXT_INPUT_PADDING,
    POPUP_SIZE_HINT,
    POPUP_MAIN_LAYOUT_SPACING,
    POPUP_MAIN_LAYOUT_CX,
    POPUP_MAIN_LAYOUT_CY,
    POPUP_CONFIRM_BTN_SIZE,
    POPUP_CONFIRM_BTN_CX,
)


class AddRowBtn(MDFillRoundFlatButton):
    """
    class for save button for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ADD_ROW_BTN_TXT
        self.font_size = ADD_ROW_FONT_SIZE
        self.size_hint = ADD_ROW_BTN_SIZE_HINT
        self.pos_hint = {"center_x": ADD_ROW_BTN_CX, "center_y": ADD_ROW_BTN_CY}
        self.md_bg_color = ADD_ROW_BG_COLOR


class TextInputCustom(MDTextField):
    """
    class for custom text input
    """

    def __init__(
        self, h_txt: str, color: str = TEXT_INPUT_COLOR_DEFAULT, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.hint_text = h_txt
        self.text_color_focus = color
        self.hint_text_color_focus = color
        self.line_color_focus = color
        self.mode = TEXT_INPUT_MODE
        self.size_hint = TEXT_INPUT_SIZE_HINT
        self.cursor_color = TEXT_INPUT_CURSOR_COLOR
        self.cursor_width = TEXT_INPUT_CURSOR_WIDTH
        self.padding = TEXT_INPUT_PADDING
        self.font_size = TEXT_INPUT_FONT_SIZE
        self.error_color = color
        self.required = True


class AddRowPopup(Popup):
    """
    class for add row popup
    """

    def __init__(self):
        super().__init__()
        self.size_hint = POPUP_SIZE_HINT
        self.title = POPUP_TITLE
        main_layout = MDBoxLayout(
            orientation=POPUP_MAIN_LAYOUT_ORIENTATION,
            spacing=POPUP_MAIN_LAYOUT_SPACING,
            pos_hint={
                "center_x": POPUP_MAIN_LAYOUT_CX,
                "center_y": POPUP_MAIN_LAYOUT_CY,
            },
        )
        self.add_widget(main_layout)

        self.task = TextInputCustom(TASK_TEXT, color=TEXT_INPUT_COLOR)
        self.date = TextInputCustom(DATE_TEXT, color=TEXT_INPUT_COLOR)
        self.status = TextInputCustom(STATUS_TEXT, color=TEXT_INPUT_COLOR)
        self.extra_col = TextInputCustom(EXTRA_TEXT, color=TEXT_INPUT_COLOR)
        self.confirm_btn = MDFillRoundFlatButton(
            text=COMFIRM_BTN_TXT,
            font_size=CONFIRM_FONT_SIZE,
            size_hint=(None, None),
            size=POPUP_CONFIRM_BTN_SIZE,
            pos_hint={"center_x": POPUP_CONFIRM_BTN_CX},
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

class StatusDropDownItem(MDDropDownItem):
    """
    class for status drop down item
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.text = 'Status'



class StatusDropDownMenu(MDDropdownMenu):

    """
    class for status drop down menu
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.drop_down_item = MDDropDownItem()
        # self.caller = self.drop_down_item
        self.items = (

            [
                {"text": "Done", "viewclass": "OneLineListItem", "on_release": lambda x: self.set_item(x)},
                {"text": "In Progress", "viewclass": "OneLineListItem", "on_release": lambda x: self.set_item(x)},
                {"text": "Not Started", "viewclass": "OneLineListItem", "on_release": lambda x: self.set_item(x)},
            ],
        )
        # self.width_mult = 4
        # self.menu.bind(on_release=lambda x: self.set_item(x))

    def set_item(self, text_item):
        """
        set item for drop down
        """
        self.drop_down_item.set_item(text_item)
        self.menu.dismiss()
