"""
Module for login screen
"""
import os
import json
import requests

from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials, auth, db
from firebase_admin._auth_utils import EmailAlreadyExistsError

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

from kivy.uix.image import Image


from Components.login_comp import (
    SecondaryLayout,
    LoginPageBtn,
    OrLabel,
    GoogleBtn,
    LoginPopup,
    SignupPopup,
)


from Constants.login_constants import (
    LP_MAIN_LAYOUT_BG_COLOR,
    LP_IMAGE_SIZE_HINT,
    LP_IMAGE_CX,
    LP_IMAGE_CY,
    LP_EMAIL_LAYOUT_POS_LAY,
    LP_EMAIL_LAYOUT_POS_TXT,
    LP_PASSWORD_LAYOUT_POS_LAY,
    LP_PASSWORD_LAYOUT_POS_TXT,
    LP_LOGIN_BTN_POS,
    LP_SIGNUP_BTN_POS,
    LP_THIRD_LAYOUT_CX,
    LP_THIRD_LAYOUT_CY,
    LP_USER_LOGIN_FUNC_TIMEOUT,
    LP_USER_LOGIN_FUNC_CODE,
)

from Resources.login_resources import (
    LP_NAME,
    LP_USER_NAME_TUP,
    LP_FIREBASE_SDK_PATH,
    LOGIN_IMAGE_PATH,
    EMAIL_LAYOUT_HINT_TXT,
    PASSWORD_LAYOUT_HINT_TXT,
    LOGIN_BTN_TXT,
    SIGNUP_BTN_TXT,
    REQ_EXCEPTION_MSG,
    DB_REF,
    SCREEN_NAME_SWITCH,
    EMAIL_EXISTS_MSG,
    VALUE_EXCEPTION_MSG,
    SIGNUP_SUCCESS_MSG,
    SIGNUP_SUCCESS_BOX_TITLE,
    BOX_TITLE_DEFAULT,
)

load_dotenv()


class LoginPage(MDScreen):
    """
    class for screen of login page
    """

    def __init__(self, main_app):
        super().__init__()
        self.name = LP_NAME
        self.main_app = main_app
        self.user = None
        self.signup_popup = None
        self.user_name_tup = LP_USER_NAME_TUP

        self.firebase_sdk = LP_FIREBASE_SDK_PATH
        self.realtime_db = os.getenv("FIREBASE_DB_URL")
        cred = credentials.Certificate(self.firebase_sdk)
        firebase_admin.initialize_app(cred, {"databaseURL": self.realtime_db})
        self.api_key = os.getenv("FIREBASE_API_KEY")
        self.api_auth = os.getenv("FIREBASE_API_AUTH")

        main_layout = MDFloatLayout(md_bg_color=LP_MAIN_LAYOUT_BG_COLOR)
        self.add_widget(main_layout)
        login_image = Image(
            source=LOGIN_IMAGE_PATH,
            size_hint=LP_IMAGE_SIZE_HINT,
            pos_hint={"center_x": LP_IMAGE_CX, "center_y": LP_IMAGE_CY},
        )

        self.email_layout = SecondaryLayout(
            h_txt=EMAIL_LAYOUT_HINT_TXT,
            pos_lay_xy=LP_EMAIL_LAYOUT_POS_LAY,
            pos_txt_xy=LP_EMAIL_LAYOUT_POS_TXT,
            is_password=False,
        )
        self.password_layout = SecondaryLayout(
            h_txt=PASSWORD_LAYOUT_HINT_TXT,
            pos_lay_xy=LP_PASSWORD_LAYOUT_POS_LAY,
            pos_txt_xy=LP_PASSWORD_LAYOUT_POS_TXT,
            is_password=True,
        )

        login_button = LoginPageBtn(txt=LOGIN_BTN_TXT, pos_xy=LP_LOGIN_BTN_POS)
        signup_button = LoginPageBtn(txt=SIGNUP_BTN_TXT, pos_xy=LP_SIGNUP_BTN_POS)

        login_button.bind(on_release=lambda x: self.user_login(self))
        signup_button.bind(on_release=lambda x: self.open_signup_popup(self))

        or_label = OrLabel()
        third_layout = MDFloatLayout(
            pos_hint={"center_x": LP_THIRD_LAYOUT_CX, "center_y": LP_THIRD_LAYOUT_CY}
        )
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
                self.api_auth,
                params={"key": self.api_key},
                data=payload,
                timeout=LP_USER_LOGIN_FUNC_TIMEOUT,
            )
            if response.status_code != LP_USER_LOGIN_FUNC_CODE:
                raise requests.exceptions.RequestException
        except requests.exceptions.RequestException:
            self.login_dialog_box(msg_text=REQ_EXCEPTION_MSG)
        else:
            user_email = self.email_layout.text_field.text
            user = auth.get_user_by_email(user_email)
            user_data = db.reference(DB_REF).child(user.uid).get()
            self.user_name_tup = (user_data["fname"], user_data["lname"])
            self.main_app.screen_manager.get_screen(
                SCREEN_NAME_SWITCH
            ).hello_label.text = (
                f"Hello, {self.user_name_tup[0]} {self.user_name_tup[1]}!"
            )
            self.main_app.screen_manager.current = SCREEN_NAME_SWITCH

    def open_signup_popup(self, obj):
        """
        func for signup user
        """
        self.signup_popup = SignupPopup()
        self.signup_popup.open()
        self.signup_popup.confirm_btn.bind(
            on_release=lambda x: self.user_signup(
                self.signup_popup.email_text,
                self.signup_popup.password_text,
                self.signup_popup.fname_text,
                self.signup_popup.lname_text,
            )
        )

    def user_signup(self, email, password, fname, lname):
        """
        func for create signup user
        """
        try:
            self.user = auth.create_user(
                email=email.text,
                password=password.text,
            )
        except EmailAlreadyExistsError:
            self.login_dialog_box(msg_text=EMAIL_EXISTS_MSG)
        except ValueError:
            self.login_dialog_box(msg_text=VALUE_EXCEPTION_MSG)
        else:
            ref = db.reference(DB_REF)
            user_ref = ref.child(f"{self.user.uid}")
            user_ref.set(
                {
                    "email": email.text,
                    "password": password.text,
                    "fname": fname.text,
                    "lname": lname.text,
                }
            )
            self.signup_popup.dismiss()
            self.login_dialog_box(
                msg_text=SIGNUP_SUCCESS_MSG, box_title=SIGNUP_SUCCESS_BOX_TITLE
            )

    def login_dialog_box(self, msg_text, box_title=BOX_TITLE_DEFAULT):
        """
        func for login dialog box
        """
        login_box = LoginPopup(msg_text=msg_text, box_title=box_title)
        login_box.open()
