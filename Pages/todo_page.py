"""
Module of to do screen
"""
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable

from Components.todo_comp import AddRowBtn, AddRowPopup
from Components.general_comp import NavLayout


from Resources.todo_resources import TOP_BAR_TITLE


class ToDoScreen(MDScreen):
    """
    class for to do screen
    """

    def __init__(self, main_app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "todo"
        self.row_counter = 1
        self.row_popup = None

        main_layout = MDFloatLayout(md_bg_color=(51 / 255, 163 / 255, 152 / 255, 1))
        self.add_widget(main_layout)

        self.data_table = MDDataTable(
            column_data=[
                ("No.", dp(20)),
                ("Task", dp(15)),
                ("Status", dp(15)),
                ("Date", dp(15)),
            ],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9, 0.7),
            use_pagination=True,
            check=True,
        )
        self.add_row_btn = AddRowBtn()

        self.add_row_btn.bind(on_release=lambda x: self.open_row_popup(self))

        self.nav_layout = NavLayout(main_app=main_app, title_txt=TOP_BAR_TITLE)
        self.add_widget(self.nav_layout)
        main_layout.add_widget(self.add_row_btn)
        main_layout.add_widget(self.data_table)

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

    def add_row(self, task_name, date, status="Pending"):
        """
        func to add row to data table
        """
        self.data_table.add_row((self.row_counter, task_name, status, date))
        self.row_counter += 1
        # self.row_popup.dismiss()
