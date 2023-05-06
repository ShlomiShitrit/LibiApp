from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel


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

        email_text_field = MDTextField(
            id=id_str,
            hint_text=h_txt,
            mode="rectangle",
            size_hint=(1, None),
            pos_hint={"center_x": pos_txt_xy[0], "center_y": pos_txt_xy[1]},
            password=is_password,
            cursor_color=(57 / 255, 66 / 255, 143 / 255, 1),
            cursor_width="2sp",
            padding=15,
            font_size="18sp",
            error_color=(66 / 255, 135 / 255, 245 / 255, 1),
            required=True,
        )
        self.add_widget(email_text_field)


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


class LoginPage(MDScreen):
    """
    class for screen of login page
    """

    def __init__(self):
        super().__init__()
        self.name = "login"

        main_layout = MDFloatLayout(md_bg_color=(51 / 255, 163 / 255, 152 / 255, 1))
        self.add_widget(main_layout)
        login_image = Image(
            source="../images/login4.png",
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.78},
        )

        sec_layout1 = SecondaryLayout(
            id_str="email",
            h_txt="Email",
            pos_lay_xy=(0.5, 0.52),
            pos_txt_xy=(0.5, 0.6),
            is_password=False,
        )
        sec_layout2 = SecondaryLayout(
            id_str="password",
            h_txt="Password",
            pos_lay_xy=(0.5, 0.41),
            pos_txt_xy=(0.5, 0.5),
            is_password=True,
        )

        login_button = LoginPageBtn(txt="LOGIN", pos_xy=(0.29, 0.3))
        signup_button = LoginPageBtn(txt="SIGNUP", pos_xy=(0.72, 0.3))

        login_button.bind(on_release=lambda x: self.user_login(self))
        signup_button.bind(on_release=lambda x: self.user_signup(self))

        or_label = MDLabel(
            text="OR",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            font_size="16sp",
            halign="center",
        )

        sec_layout3 = MDFloatLayout(pos_hint={"center_x": 0.5, "center_y": 0.1})
        google_btn = MDFillRoundFlatIconButton(
            icon="google",
            text="Sign in with Google",
            size_hint=(0.5, 0.05),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            md_bg_color=(20 / 255, 100 / 255, 105 / 255, 1),
        )

        sec_layout3.add_widget(google_btn)
        main_layout_widgets_tup = (
            login_image,
            sec_layout1,
            sec_layout2,
            login_button,
            signup_button,
            or_label,
            sec_layout3,
        )

        for widget in main_layout_widgets_tup:
            main_layout.add_widget(widget)

    def user_login(self, obj):
        print("Login")

    def user_signup(self, obj):
        print("Sign Up")
