"""
Module for login screen
"""
import json
import requests

import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin._auth_utils import EmailAlreadyExistsError

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image

from login_comp import SecondaryLayout, LoginPageBtn, OrLabel, GoogleBtn, LoginDialog


class LoginPage(MDScreen):
    """
    class for screen of login page
    """

    def __init__(self, main_app):
        super().__init__()
        self.name = "login"
        self.main_app = main_app

        self.firebase_sdk = "libiapp-sdk.json"
        cred = credentials.Certificate(self.firebase_sdk)
        firebase_admin.initialize_app(cred)
        self.api_key = "AIzaSyCQMv_9uYn9QI6la9sRJVqL7AyrqanUdLk"
        self.api_auth = (
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        )

        main_layout = MDFloatLayout(md_bg_color=(51 / 255, 163 / 255, 152 / 255, 1))
        self.add_widget(main_layout)
        login_image = Image(
            source="../images/login4.png",
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.78},
        )

        self.email_layout = SecondaryLayout(
            id_str="email",
            h_txt="Email",
            pos_lay_xy=(0.5, 0.52),
            pos_txt_xy=(0.5, 0.6),
            is_password=False,
        )
        self.password_layout = SecondaryLayout(
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

        or_label = OrLabel()
        third_layout = MDFloatLayout(pos_hint={"center_x": 0.5, "center_y": 0.1})
        google_btn = GoogleBtn()

        third_layout.add_widget(google_btn)

        main_layout_widgets_tup = (
            login_image,
            self.email_layout,
            self.password_layout,
            login_button,
            signup_button,
            or_label,
            third_layout,
        )

        for widget in main_layout_widgets_tup:
            main_layout.add_widget(widget)

    def user_login(self, obj):
        """
        func for login user
        """
        payload = json.dumps(
            {
                "email": self.email_layout.text_field.text,
                "password": self.password_layout.text_field.text,
                "returnSecureToken": True,
            }
        )
        try:
            response = requests.post(
                self.api_auth, params={"key": self.api_key}, data=payload, timeout=5
            )
            if response.status_code != 200:
                raise requests.exceptions.RequestException
        except requests.exceptions.RequestException:
            self.login_dialog_box(msg_text="Email or password is incorrect")
        else:
            self.main_app.screen_manager.current = "todo"

    def user_signup(self, obj):
        """
        func for signup user
        """
        try:
            auth.create_user(
                email=self.email_layout.text_field.text,
                password=self.password_layout.text_field.text,
            )
        except EmailAlreadyExistsError:
            self.login_dialog_box(msg_text="Email already exists")
        except ValueError:
            self.login_dialog_box(msg_text="password must be at least 6 characters")
        else:
            self.login_dialog_box(
                msg_text="User created successfully", box_title="Info"
            )

    def login_dialog_box(self, msg_text, box_title="Error"):
        """
        func for login dialog box
        """
        login_box = LoginDialog(msg_text=msg_text, box_title=box_title)
        login_box.open()
