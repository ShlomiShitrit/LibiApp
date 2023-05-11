from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label


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
        self.mode = "rectangle"
        self.size_hint = (1, None)
        self.pos_hint = {"center_x": pos_txt_xy[0], "center_y": pos_txt_xy[1]}
        self.password = is_password
        self.cursor_color = "red"
        self.cursor_width = "2sp"
        self.padding = 15
        self.font_size = "18sp"
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
        self.size_hint = (0.85, 0.08)
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
        self.font_size = "18sp"
        self.size_hint = (0.4, 0.08)
        self.pos_hint = {"center_x": pos_xy[0], "center_y": pos_xy[1]}
        self.md_bg_color = (20 / 255, 100 / 255, 105 / 255, 1)


class OrLabel(MDLabel):
    """
    class for label "OR" in login page
    """

    def __init__(self):
        super().__init__()
        self.text = "OR"
        self.pos_hint = {"center_x": 0.5, "center_y": 0.2}
        self.font_size = "16sp"
        self.halign = "center"


class GoogleBtn(MDFillRoundFlatIconButton):
    """
    class for google button
    """

    def __init__(self):
        super().__init__()
        self.icon = "google"
        self.text = "Sign in with Google"
        self.size_hint = (0.5, 0.05)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.md_bg_color = (20 / 255, 100 / 255, 105 / 255, 1)


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
        self.orientation = "vertical"
        self.size_hint = (0.7, 0.7)
        self.spacing = 30
        self.label = PopupLabel(text=msg_txt)
        self.add_widget(self.label)

        self.close_error_button = MDFillRoundFlatButton(
            text="Close",
            font_size="18sp",
            size_hint=(0.4, 0.08),
            pos_hint={"center_x": 0.8, "center_y": 0.2},
        )
        self.add_widget(self.close_error_button)
        self.close_error_button.bind(on_release=login_popup.dismiss)


class LoginPopup(Popup):
    """
    class for error dialog box in login page
    """

    def __init__(self, msg_text: str, box_title: str):
        super().__init__()
        self.size_hint = (0.7, 0.3)
        self.title = box_title
        self.add_widget(PopupContent(msg_txt=msg_text, login_popup=self))


class SignupPopup(Popup):
    """
    class for signup popup
    """

    def __init__(self):
        super().__init__()
        self.size_hint = (0.7, 0.7)
        self.title = "Sign Up"
        main_layout = MDBoxLayout(orientation="vertical", spacing=15)
        self.add_widget(main_layout)

        self.fname_text = TextInputCustom("First Name", (0.5, 0.7), False, color='cyan')
        self.lname_text = TextInputCustom("Last Name", (0.5, 0.7), False, color='cyan')
        self.email_text = TextInputCustom("Email", (0.5, 0.7), False, color='cyan')
        self.password_text = TextInputCustom("Password", (0.5, 0.7), True, color='cyan')
        self.confirm_btn = MDFillRoundFlatButton(
            text="Confirm",
            font_size="18sp",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.75},
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
