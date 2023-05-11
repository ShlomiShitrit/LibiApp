from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class SecondaryLayout(MDFloatLayout):
    """
    class for secondary layout
    """

    def __init__(
        self,
        id_str: str,
        h_txt: str,
        pos_lay_xy: tuple,
        pos_txt_xy: tuple,
        is_password: bool,
    ):
        super().__init__()
        self.size_hint = (0.85, 0.08)
        self.pos_hint = {"center_x": pos_lay_xy[0], "center_y": pos_lay_xy[1]}

        self.text_field = MDTextField(
            id=id_str,
            hint_text=h_txt,
            text_color_focus="black",
            hint_text_color_focus="black",
            line_color_focus="black",
            mode="rectangle",
            size_hint=(1, None),
            pos_hint={"center_x": pos_txt_xy[0], "center_y": pos_txt_xy[1]},
            password=is_password,
            cursor_color="red",
            cursor_width="2sp",
            padding=15,
            font_size="18sp",
            error_color="black",
            required=True,
        )
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


class DialogContent(MDBoxLayout):
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


class LoginDialog(Popup):
    """
    class for error dialog box in login page
    """

    def __init__(self, msg_text: str, box_title: str):
        super().__init__()
        self.size_hint = (0.7, 0.3)
        self.title = box_title
        self.add_widget(DialogContent(msg_txt=msg_text, login_popup=self))
