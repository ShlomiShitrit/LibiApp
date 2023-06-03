"""
Module of to do screen
"""
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu


from Components.todo_comp import (
    AddRowBtn,
    AddRowPopup,
    StatusDropDownMenu,
    StatusDropDownItem,
    ActionBtn,
)
from Components.general_comp import NavLayout


from Resources.todo_resources import (
    TOP_BAR_TITLE,
    SCREEN_NAME,
    COLS_NAMES_TUP,
)

from Constants.todo_constants import (
    ROW_COUNTER_START,
    MAIN_LAYOUT_BG_COLOR,
    DATA_TABLE_DP_COLS_TUP,
    DATA_TABLE_CX,
    DATA_TABLE_CY,
    DATA_TABLE_SIZE_HINT,
    ROW_COUNTER_ADDER,
)


class ToDoScreen(MDScreen):
    """
    class for to do screen
    """

    def __init__(self, main_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = SCREEN_NAME
        self.row_counter = ROW_COUNTER_START
        self.row_popup = None
        self.status_item = StatusDropDownItem()
        self.status_menu = StatusDropDownMenu(caller=self.status_item)
        self.status_item = MDDropDownItem(pos_hint={"center_x": 0.5, "center_y": 0.07})
        self.status_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Done",
                "on_release": lambda x="Done": self.menu_callback(x),
            },
            {
                "text": "In Progress",
                "on_release": lambda x="In Progress": self.menu_callback(x),
            },
            {
                "text": "Not Started",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Not Started": self.menu_callback(x),
            },
        ]

        self.status_menu = MDDropdownMenu(
            items=self.status_list,
            caller=self.status_item,
            width_mult=4,
            radius=[
                1,
                1,
                1,
                1,
            ],
        )
        self.status_item.bind(on_release=lambda x: self.status_menu.open())

        main_layout = MDFloatLayout(md_bg_color=MAIN_LAYOUT_BG_COLOR)
        self.add_widget(main_layout)

        self.data_table = MDDataTable(
            column_data=[
                (COLS_NAMES_TUP[0], dp(DATA_TABLE_DP_COLS_TUP[0])),
                (COLS_NAMES_TUP[1], dp(DATA_TABLE_DP_COLS_TUP[1])),
                (COLS_NAMES_TUP[2], dp(DATA_TABLE_DP_COLS_TUP[2])),
                (COLS_NAMES_TUP[3], dp(DATA_TABLE_DP_COLS_TUP[3])),
            ],
            pos_hint={"center_x": DATA_TABLE_CX, "center_y": DATA_TABLE_CY},
            size_hint=DATA_TABLE_SIZE_HINT,
            use_pagination=True,
            check=True,
        )
        self.add_row_btn = AddRowBtn()

        self.add_row_btn.bind(on_release=lambda x: self.open_row_popup(self))

        self.nav_layout = NavLayout(main_app=main_app, title_txt=TOP_BAR_TITLE)
        self.add_widget(self.nav_layout)
        self.action_btn = ActionBtn()
        main_layout.add_widget(self.action_btn)
        # main_layout.add_widget(self.add_row_btn)
        # main_layout.add_widget(self.data_table)
        main_layout.add_widget(self.status_item)

    def open_row_popup(self, obj):
        """
        func to open popup for adding row
        """
        self.row_popup = AddRowPopup()
        self.row_popup.open()
        self.row_popup.confirm_btn.bind(
            on_release=lambda x: self.add_row(
                self.row_popup.task.text, self.row_popup.date.text
            )
        )

    def add_row(self, task_name, date):
        """
        func to add row to data table
        """
        self.data_table.add_row((self.row_counter, task_name, self.status_item, date))
        self.row_counter += ROW_COUNTER_ADDER
        self.row_popup.dismiss()

    def menu_callback(self, text_item):
        """
        set item for drop down
        """
        self.status_item.set_item(text_item)
        self.status_menu.dismiss()
