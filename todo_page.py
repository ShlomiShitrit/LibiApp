"""
Module of to do screen
"""

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen

from todo_comp import ListItemWithCheckbox, SaveBtn, TaskText


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

        self.save_btn = SaveBtn()
        self.task_text = TaskText()

        self.save_btn.bind(on_release=self.add_item)

        box_layout = MDBoxLayout()
        box_layout.add_widget(view_scroll)

        main_layout_widgets_tup = (box_layout, self.save_btn, self.task_text)

        for widget in main_layout_widgets_tup:
            main_layout.add_widget(widget)

    def add_item(self, obj):
        """
        func to add task
        """
        task = ListItemWithCheckbox(text=self.task_text.text)
        self.todo_list.add_widget(task)
        self.task_text.text = ""
