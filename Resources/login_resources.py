"""
Module for storing login page resources
"""

### login components ###

# TextInputCustom

TEXT_INPUT_MODE = "rectangle"
TEXT_INPUT_CURSOR_COLOR = "red"
TEXT_INPUT_CURSOR_WIDTH = "2sp"
TEXT_INPUT_FONT_SIZE = "18sp"

# LoginPageBtn

LOGIN_BTN_FONT_SIZE = "18sp"

# OrLabel
OR_LABRL_TXT = "OR"
OR_LABEL_FONT_SIZE = "16sp"
OR_LABEL_HALIGN = "center"

# GoogleBtn

GOOGLE_BTN_ICON = "google"
GOOGLE_BTN_TXT = "Sign in with Google"

# PopupContent
POPUP_CONTENT_ORIENTATION = "vertical"
POPUP_CONTENT_CLOSE_BTN_TXT = "Close"
POPUP_CONTENT_CLOSE_BTN_FONT_SIZE = "18sp"

# SignupPopup
SIGNUP_POPUP_TITLE = "Sign Up"
SIGNUP_POPUP_MAIN_LAYOUT_ORIENTATION = "vertical"
SIGNUP_POPUP_FNAME_TXT = "First Name"
SIGNUP_POPUP_LNAME_TXT = "Last Name"
SIGNUP_POPUP_EMAIL_TXT = "Email"
SIGNUP_POPUP_PASSWORD_TXT = "Password"
SIGNUP_POPUP_TEXT_INPUT_COLOR = "cyan"
SIGNUP_POPUP_CONFIRM_BTN_TXT = "Confirm"
SIGNUP_POPUP_CONFIRM_BTN_FONT_SIZE = "18sp"

### login page ###

# __init__

LP_NAME = "login"
LP_USER_NAME_TUP = ("Libi", "Moryosef")
LP_FIREBASE_SDK_PATH = "libiapp-sdk.json"
LP_FIREBASE_DB_URL = "https://libiapp-14bee-default-rtdb.firebaseio.com/"
LP_API_KEY = "AIzaSyCQMv_9uYn9QI6la9sRJVqL7AyrqanUdLk"
LP_API_AUTH = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

LOGIN_IMAGE_PATH = "../images/login4.png"
EMAIL_LAYOUT_HINT_TXT = "Email"
PASSWORD_LAYOUT_HINT_TXT = "Password"
LOGIN_BTN_TXT = "LOGIN"
SIGNUP_BTN_TXT = "SIGN UP"

# func user_login

REQ_EXCEPTION_MSG = "Email or password is incorrect"
DB_REF = "Users"

SCREEN_NAME_SWITCH = "home"


# func user_signup

EMAIL_EXISTS_MSG = "Email already exists"
VALUE_EXCEPTION_MSG = "Password must be at least 6 characters"
SIGNUP_SUCCESS_MSG = "User created successfully"
SIGNUP_SUCCESS_BOX_TITLE = "Info"

# func login_dialog_box
BOX_TITLE_DEFAULT = "Error"











