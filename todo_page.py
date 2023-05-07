"""
Module of to do screen
"""

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    """
    Custom right check box
    """


class ListItemWithCheckbox(OneLineIconListItem):
    """
    class for list item
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = "pencil"
        self.add_widget(IconLeftWidget(icon=self.icon))
  


class ToDoScreen(MDScreen):
    """
    class for to do screen
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "todo"
        main_layout = MDFloatLayout(md_bg_color=(51 / 255, 163 / 255, 152 / 255, 1))
        self.add_widget(main_layout)

        self.todo_list = MDList(pos_hint={"center_x": 0.5, "center_y": 0.78})
        view_scroll = MDScrollView(
            self.todo_list, pos_hint={"center_x": 0.5, "top": 0.8}
        )

        save_btn = MDFillRoundFlatButton(
            text="Save",
            font_size="18sp",
            size_hint=(0.4, 0.08),
            pos_hint={"center_x": 0.72, "center_y": 0.07},
            md_bg_color=(20 / 255, 100 / 255, 105 / 255, 1),
        )

        self.task_text = MDTextField(
            hint_text="Task",
            mode="rectangle",
            size_hint=(0.75, 0.75),
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            cursor_color=(57 / 255, 66 / 255, 143 / 255, 1),
            cursor_width="2sp",
            padding=15,
            font_size="18sp",
            error_color=(66 / 255, 135 / 255, 245 / 255, 1),
            required=True,
        )
        save_btn.bind(on_release=self.add_item)

        box_layout = MDBoxLayout()
        box_layout.add_widget(view_scroll)

        main_layout_widgets_tup = (box_layout, save_btn, self.task_text)

        for widget in main_layout_widgets_tup:
            main_layout.add_widget(widget)

    def add_item(self, obj):
        """
        func to add task
        """
        task = ListItemWithCheckbox(text=self.task_text.text)
        self.todo_list.add_widget(task)
        self.task_text.text = ""
