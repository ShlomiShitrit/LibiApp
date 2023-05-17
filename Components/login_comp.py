from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from Constants.login_constants import (
    TEXT_INPUT_SIZE_HINT,
    TEXT_INPUT_PADDING,
    SEC_LAYOUT_SIZE_HINT,
    LOGIN_BTN_SIZE_HINT,
    LOGIN_BTN_BG_COLOR,
    OR_LABEL_CX,
    OR_LABEL_CY,
    GOOGLE_BTN_SIZE_HINT,
    GOOGLE_BTN_BG_COLOR,
    GOOGLE_BTN_CX,
    GOOGLE_BTN_CY,
    POPUP_CONTENT_SIZE_HINT,
    POPUP_CONTENT_SPACING,
    POPUP_CONTENT_CLOSE_BTN_SIZE_HINT,
    POPUP_CONTENT_CLOSE_BTN_CX,
    POPUP_CONTENT_CLOSE_BTN_CY,
    LOGIN_POPUP_SIZE_HINT,
    SIGNUP_POPUP_SIZE_HINT,
    SIGNUP_POPUP_MAIN_LAYOUT_SPACING,
    SIGNUP_POPUP_TXT_INPUT_SIZE_HINT,
    SIGNUP_POPUP_CONFIRM_BTN_SIZE,
    SIGNUP_POPUP_CONFIRM_BTN_CX,
)

from Resources.login_resources import (
    TEXT_INPUT_MODE,
    TEXT_INPUT_CURSOR_COLOR,
    TEXT_INPUT_CURSOR_WIDTH,
    TEXT_INPUT_FONT_SIZE,
    LOGIN_BTN_FONT_SIZE,
    OR_LABRL_TXT,
    OR_LABEL_FONT_SIZE,
    OR_LABEL_HALIGN,
    GOOGLE_BTN_ICON,
    GOOGLE_BTN_TXT,
    POPUP_CONTENT_ORIENTATION,
    POPUP_CONTENT_CLOSE_BTN_TXT,
    POPUP_CONTENT_CLOSE_BTN_FONT_SIZE,
    SIGNUP_POPUP_TITLE,
    SIGNUP_POPUP_MAIN_LAYOUT_ORIENTATION,
    SIGNUP_POPUP_FNAME_TXT,
    SIGNUP_POPUP_LNAME_TXT,
    SIGNUP_POPUP_EMAIL_TXT,
    SIGNUP_POPUP_PASSWORD_TXT,
    SIGNUP_POPUP_TEXT_INPUT_COLOR,
    SIGNUP_POPUP_CONFIRM_BTN_TXT,
    SIGNUP_POPUP_CONFIRM_BTN_FONT_SIZE,
)


class TextInputCustom(MDTextField):
    """
    class for custom text input
    """

    def __init__(self, h_txt: str, pos_txt_xy: tuple, is_password: bool, color="black"):
        super().__init__()

        self.hint_text = h_txt
        self.text_color_focus = color
        self.hint_text_color_focus = color
        self.line_color_focus = color
        self.mode = TEXT_INPUT_MODE
        self.size_hint = TEXT_INPUT_SIZE_HINT
        self.pos_hint = {"center_x": pos_txt_xy[0], "center_y": pos_txt_xy[1]}
        self.password = is_password
        self.cursor_color = TEXT_INPUT_CURSOR_COLOR
        self.cursor_width = TEXT_INPUT_CURSOR_WIDTH
        self.padding = TEXT_INPUT_PADDING
        self.font_size = TEXT_INPUT_FONT_SIZE
        self.error_color = color
        self.required = True


class SecondaryLayout(MDFloatLayout):
    """
    class for secondary layout
    """

    def __init__(
        self,
        h_txt: str,
        pos_lay_xy: tuple,
        pos_txt_xy: tuple,
        is_password: bool,
    ):
        super().__init__()
        self.size_hint = SEC_LAYOUT_SIZE_HINT
        self.pos_hint = {"center_x": pos_lay_xy[0], "center_y": pos_lay_xy[1]}

        self.text_field = TextInputCustom(h_txt, pos_txt_xy, is_password)
        self.add_widget(self.text_field)


class LoginPageBtn(MDFillRoundFlatButton):
    """
    class for button for login page
    """

    def __init__(self, txt: str, pos_xy: tuple):
        super().__init__()

        self.text = txt
        self.font_size = LOGIN_BTN_FONT_SIZE
        self.size_hint = LOGIN_BTN_SIZE_HINT
        self.pos_hint = {"center_x": pos_xy[0], "center_y": pos_xy[1]}
        self.md_bg_color = LOGIN_BTN_BG_COLOR


class OrLabel(MDLabel):
    """
    class for label "OR" in login page
    """

    def __init__(self):
        super().__init__()
        self.text = OR_LABRL_TXT
        self.pos_hint = {"center_x": OR_LABEL_CX, "center_y": OR_LABEL_CY}
        self.font_size = OR_LABEL_FONT_SIZE
        self.halign = OR_LABEL_HALIGN


class GoogleBtn(MDFillRoundFlatIconButton):
    """
    class for google button
    """

    def __init__(self):
        super().__init__()
        self.icon = GOOGLE_BTN_ICON
        self.text = GOOGLE_BTN_TXT
        self.size_hint = GOOGLE_BTN_SIZE_HINT
        self.pos_hint = {"center_x": GOOGLE_BTN_CX, "center_y": GOOGLE_BTN_CY}
        self.md_bg_color = GOOGLE_BTN_BG_COLOR


class PopupLabel(Label):
    """
    class for label in popup
    """

    def on_size(self, *args):
        """
        function to set text size
        """
        self.text_size = self.size


class PopupContent(MDBoxLayout):
    """
    class for dialog content
    """

    def __init__(self, msg_txt: str, login_popup: Popup):
        super().__init__()
        self.orientation = POPUP_CONTENT_ORIENTATION
        self.size_hint = POPUP_CONTENT_SIZE_HINT
        self.spacing = POPUP_CONTENT_SPACING
        self.label = PopupLabel(text=msg_txt)
        self.add_widget(self.label)

        self.close_error_button = MDFillRoundFlatButton(
            text=POPUP_CONTENT_CLOSE_BTN_TXT,
            font_size=POPUP_CONTENT_CLOSE_BTN_FONT_SIZE,
            size_hint=POPUP_CONTENT_CLOSE_BTN_SIZE_HINT,
            pos_hint={
                "center_x": POPUP_CONTENT_CLOSE_BTN_CX,
                "center_y": POPUP_CONTENT_CLOSE_BTN_CY,
            },
        )
        self.add_widget(self.close_error_button)
        self.close_error_button.bind(on_release=login_popup.dismiss)


class LoginPopup(Popup):
    """
    class for error dialog box in login page
    """

    def __init__(self, msg_text: str, box_title: str):
        super().__init__()
        self.size_hint = LOGIN_POPUP_SIZE_HINT
        self.title = box_title
        self.add_widget(PopupContent(msg_txt=msg_text, login_popup=self))


class SignupPopup(Popup):
    """
    class for signup popup
    """

    def __init__(self):
        super().__init__()
        self.size_hint = SIGNUP_POPUP_SIZE_HINT
        self.title = SIGNUP_POPUP_TITLE
        main_layout = MDBoxLayout(
            orientation=SIGNUP_POPUP_MAIN_LAYOUT_ORIENTATION,
            spacing=SIGNUP_POPUP_MAIN_LAYOUT_SPACING,
        )
        self.add_widget(main_layout)

        self.fname_text = TextInputCustom(
            SIGNUP_POPUP_FNAME_TXT,
            SIGNUP_POPUP_TXT_INPUT_SIZE_HINT,
            False,
            color=SIGNUP_POPUP_TEXT_INPUT_COLOR,
        )
        self.lname_text = TextInputCustom(
            SIGNUP_POPUP_LNAME_TXT,
            SIGNUP_POPUP_TXT_INPUT_SIZE_HINT,
            False,
            color=SIGNUP_POPUP_TEXT_INPUT_COLOR,
        )
        self.email_text = TextInputCustom(
            SIGNUP_POPUP_EMAIL_TXT,
            SIGNUP_POPUP_TXT_INPUT_SIZE_HINT,
            False,
            color=SIGNUP_POPUP_TEXT_INPUT_COLOR,
        )
        self.password_text = TextInputCustom(
            SIGNUP_POPUP_PASSWORD_TXT,
            SIGNUP_POPUP_TXT_INPUT_SIZE_HINT,
            True,
            color=SIGNUP_POPUP_TEXT_INPUT_COLOR,
        )
        self.confirm_btn = MDFillRoundFlatButton(
            text=SIGNUP_POPUP_CONFIRM_BTN_TXT,
            font_size=SIGNUP_POPUP_CONFIRM_BTN_FONT_SIZE,
            size_hint=(None, None),
            size=SIGNUP_POPUP_CONFIRM_BTN_SIZE,
            pos_hint={"center_x": SIGNUP_POPUP_CONFIRM_BTN_CX},
        )

        widgets_tup = (
            self.fname_text,
            self.lname_text,
            self.email_text,
            self.password_text,
            self.confirm_btn,
        )
        for widget in widgets_tup:
            main_layout.add_widget(widget)
