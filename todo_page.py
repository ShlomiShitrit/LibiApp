from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineListItem, MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    """
    Custom right check box
    """


class ToDoList(MDList):
    """
    class for to do list
    """

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.pos_hint={"center_x": 0.5, "center_y": 0.78}


class ToDoScreen(MDScreen):
    """
    class for to do screen
    """

    def __init__(self):
        super().__init__()
        self.name = 'todo'
        main_layout = MDFloatLayout(md_bg_color=(51 / 255, 163 / 255, 152 / 255, 1))
        self.add_widget(main_layout)
        view_scroll = MDScrollView()
        self.todo_list = ToDoList(id="scroll")
        view_scroll.add_widget(self.todo_list)
        save_btn = MDFillRoundFlatButton(
            text="Save",
            font_size="18sp",
            size_hint=(0.4, 0.08),
            pos_hint={"center_x": 0.72, "center_y": 0.07},
            md_bg_color=(20 / 255, 100 / 255, 105 / 255, 1),
            on_release=lambda x: self.add_item(self)
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


        main_layout_widgets_tup = (view_scroll, save_btn, self.task_text)

        for widget in main_layout_widgets_tup:
            main_layout.add_widget(widget)
    
    def add_item(self, obj):
        """
        func to add task
        """
        task = OneLineListItem(text=self.task_text.text)
        self.todo_list.add_widget(task)
        self.task_text.text = ''
        
        


