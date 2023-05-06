from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox


class SecondaryBoxLayout(MDBoxLayout):
    """
    class for ...
    """

    def __init__(self):
        super().__init__()

        self.orientation = "horizontal"

        save_btn = MDRaisedButton(
            text="Save", #on_release=(lambda x: add_task(), lambda x: close_dialog())
        )
        cancel_btn = MDFlatButton(text="Cancel"), #on_release=lambda x: close_dialog())


class LeftCheckBox(ILeftBodyTouch, MDCheckbox):
    """
    class for ...
    """

    def __init__(self):
        super().__init__()
        self.id = "check"


class ToDoLists(OneLineListItem):
    """
    class for ...
    """

    def __init__(self):
        super().__init__()
        self.id = "list_item"
        self.markup = True

        left_check_box = MDCheckbox(id='check')
        # left_check_box.bind(on_release=lambda x: self.mark(self))

        self.add_widget(left_check_box)

    def mark(self):
        print("Mark")


class DialogContent(MDBoxLayout):
    """ "
    class for ...
    """

    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        self.spacing = "10dp"
        self.size_hint = (1, None)

        text_field = MDTextField(
            id="task_text",
            hint_text="Add List",
            pos_hint={"center_y": 0.4},
            # on_text_validate=(lambda x: add_task(), lambda x: close_dialog()),
        )

        sec_box_layout = SecondaryBoxLayout()

        main_layout_widgets_tup = (text_field, sec_box_layout)

        for widget in main_layout_widgets_tup:
            self.add_widget(widget)

class ToDoScreen(MDScreen):
   """
   class for ...
   """
   def __init__(self):
       super().__init__()
       self.name = 'todo'
       dialog = DialogContent()
       todo_lists = ToDoLists()

       main_layout_widgets_tup = (dialog, todo_lists)

       for widget in main_layout_widgets_tup:
           self.add_widget(widget)
        

