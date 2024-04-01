import os
import anvil.server
from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
import sqlite3
from kivy import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivymd.uix.pickers import MDDatePicker
from kivy.utils import platform
from kivy.clock import mainthread
from datetime import datetime
from kivymd.uix.snackbar import Snackbar
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.spinner import MDSpinner

from borrower_dashboard import DashboardScreen

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission
    )
import anvil.server

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")
Borrower = '''
<WindowManager>:
    BorrowerScreen:
    BorrowerScreen1:
    BorrowerScreen2:
    BorrowerScreen3:
    BorrowerScreen_Edu_10th:
    BorrowerScreen_Edu_Intermediate:
    BorrowerScreen_Edu_Bachelors:
    BorrowerScreen_Edu_Masters:
    BorrowerScreen_Edu_PHD:
    BorrowerScreen4:
    BorrowerScreen5:
    BorrowerScreen6:
    BorrowerScreen7:
    BorrowerScreen8:
    BorrowerScreen9:
    BorrowerScreen10:
    BorrowerScreen11:
    BorrowerScreen12:
    BorrowerScreen13:
    BorrowerScreen14:
    BorrowerScreen15:
    BorrowerScreen16:
    BorrowerScreen17:
    BorrowerScreen18:
    BorrowerScreen19:

<BorrowerScreen>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                ize_hint_y: None
                height:dp(50)

            MDTextField:
                id: username
                hint_text: 'Enter Full Name'
                multiline: False
                helper_text: "Enter Valid Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                height:self.minimum_height

            Spinner:
                id: gender_id
                text: "Select Gender"
                values: ["Select Gender","Male", "Female", "Others"]
                multiline: False
                size_hint: 1 , None
                height:"40dp"
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                padding: dp(10)

                MDTextField:
                    id: date_textfield

                    hint_text: "Enter Date Of Birth"

                    helper_text: 'DD/MM/YYYY'
                    helper_text_mode: "on_error"
                    font_name: "Roboto-Bold"
                    hint_text_color: 0, 0, 0, 1


            MDRectangleFlatButton:
                text: 'Next'
                md_bg_color: 0.043, 0.145, 0.278, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
                on_release: root.add_data(username.text, gender_id.text, date_textfield.text)

<BorrowerScreen1>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mobile_number
                hint_text: 'Enter mobile number'
                multiline: False
                helper_text: 'Enter valid number'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0,0,0, 1
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()

            MDTextField:
                id: alternate_email
                hint_text: ' Enter Alternate Email ID'
                multiline: False
                helper_text: "Enter Valid Alternate Email ID"
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"

            Spinner:
                id: spinner_id
                text: "Please Select your References"
                values: ["Select your References" ,"Google", "Facebook", "Ads","Electronic media","Others"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(mobile_number.text, alternate_email.text, spinner_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen2>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen1')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"             

            MDTextField:
                id: aadhar_number
                hint_text: 'Enter Gov ID1 Number '
                multiline: False
                helper_text: "Enter Valid Number"
                helper_text_mode: 'on_focus'
                size_hint_y: None
                height:self.minimum_height
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    id: upload_icon1
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen2').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Govt ID1'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDTextField:
                id: pan_number
                hint_text: 'Enter Gov ID2 Number '
                multiline: False
                helper_text: "Enter Valid Gov ID2 No"
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                height:self.minimum_height
                font_name: "Roboto-Bold"

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    id: upload_icon2
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen2').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Govt ID2'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(aadhar_number.text, pan_number.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen3>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen2')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True

            Spinner:
                id: spinner_id
                text: "Please Select Education Details"
                values: ["Select Education Details", "10th class", "Intermediate", "Bachelors", "Masters", "PHD"]
                multiline: False
                size_hint: 1 , None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing: dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.next_pressed(spinner_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_10th>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: "Upload 10th class certificate"
                halign: 'center'
                bold: True
                size_hint_y: None
                height: dp(50)

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_10th').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing: dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_borrower_screen()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Intermediate>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}


            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Intermediate').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Intermediate').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_borrower_screen()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Bachelors>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title"
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True


            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Bachelors').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Bachelors').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Bachelors Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Bachelors').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_borrower_screen()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_Masters>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True
            MDLabel:
                text: "Upload 10th class Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Masters').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Masters').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Bachelors Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Masters').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_Masters').check_and_open_file_manager4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label4
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_borrower_screen()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen_Edu_PHD>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        MDCard:
            orientation: "vertical"
            size_hint: None, None
            size: "280dp", "480dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: 'Education Details'
                halign: 'center'
                bold: True

            MDLabel:
                text: "Upload 10th Class Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_PHD').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                text: "Upload Intermediate/PUC Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_PHD').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label2
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Bachelors Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_PHD').check_and_open_file_manager3()

                MDLabel:
                    id: upload_label3
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label3
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Masters Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_PHD').check_and_open_file_manager4()

                MDLabel:
                    id: upload_label4
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label4
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload PHD Certificate"
                halign: 'center'
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen_Edu_PHD').check_and_open_file_manager5()
                MDLabel:
                    id: upload_label5
                    text: 'Upload Certificate'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: image_label5
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.go_to_borrower_screen()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen4>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen3')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Address'
                halign: 'center'
                bold: True

            MDTextField:
                id: country
                hint_text: 'Enter Country Name'
                multiline: False
                helper_text_mode: 'on_focus'

            MDTextField:
                id: state
                hint_text: 'Enter State Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:
                id: city
                hint_text: 'Enter City Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  

            MDTextField:
                id: zip_code
                hint_text: 'Enter postal/zipcode '
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y: None  
                input_type: 'number'  
                on_touch_down: root.on_mobile_number_touch_down()

            MDTextField:
                id: street_address
                hint_text: 'Enter Street Name'
                multiline: False
                helper_text: 'Enter valid address'
                helper_text_mode: 'on_focus'

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(street_address.text, city.text, zip_code.text, state.text, country.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen5>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen4')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Father Information'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: father_name
                hint_text: 'Enter Father Name'
                helper_text: 'Enter valid Father Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_age
                hint_text: 'Enter Father Age'
                helper_text: 'Enter valid Father Age'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_father_age_touch_down()

            MDTextField:
                id: father_occupation
                hint_text: 'Enter Father Occupation'
                helper_text: 'Enter valid Father Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_ph_no
                hint_text: 'Enter Father Phone NO'
                multiline: False
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_father_ph_no_touch_down()

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(father_name.text, father_age.text, father_occupation.text, father_ph_no.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen6>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen5')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Mother Information'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


            MDTextField:
                id: mother_name
                hint_text: 'Enter Mother Name'
                helper_text: 'Enter Valid Mother Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True

            MDTextField:
                id: mother_age
                hint_text: 'Enter Mother Age'
                helper_text: 'Enter Valid Mother Age'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_mother_age_touch_down()

            MDTextField:
                id: mother_occupation
                hint_text: 'Enter Mother Occupation'
                helper_text: 'Enter Valid Mother Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True

            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter Mother Phone No'
                helper_text: 'Enter Valid Mother Phone No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(mother_name.text, mother_age.text, mother_occupation.text, mother_ph_no.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen7>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen6')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Profession Information'
                halign: 'center'
                bold: True


            Spinner:
                id: spinner_id
                text: "Select Profession type"
                values: ["Select Profession type", "Student", "Employee", "Business"]
                multiline: False
                size_hint: 1 , None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                MDRectangleFlatButton:
                    text: "Next"
                    on_press: root.add_data(spinner_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen8>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Student Type'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: collage_name
                hint_text: 'Enter Collage Name '
                hint_text_color:0,0,0, 1
                multiline: False
                helper_text: 'Enter Valid Collage Name'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id: collage_id
                hint_text: 'Enter Collage ID'
                hint_text_color: 0,0,0, 1
                multiline: True
                helper_text: "Enter valid Collage ID"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen8').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDTextField:
                id:  college_address
                hint_text: 'Enter College Address'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: 'Enter valid College Address'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True

            GridLayout:
                cols: 1
                spacing:dp(30)

                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(collage_name.text, college_address.text, collage_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen9>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Business Type'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Step-1'
                halign: 'center'
                bold: True

            MDTextField:
                id: business_name
                hint_text: 'Enter Business Name '
                multiline: False
                helper_text: "Enter valid Business Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id: business_location
                hint_text: 'Enter Business Location'
                multiline: False
                helper_text: "Enter valid Business Location"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id:  business_address
                hint_text: 'Enter Business Address'
                multiline: False
                helper_text: "Enter valid Business Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(business_name.text, business_location.text, business_address.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen10>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen9')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-2'
                halign: 'center'
                bold: True

            Spinner:
                id: spin
                text: "Please Select Business Type"
                values: ["Select Business Type","Partnership", "Cooperation", "Cooperative", "Solo Proprietorship", "Cash", "Cheque", "Online Transaction", "Limited Liability Company"]
                multiline:False
                background_color: (0,0,0,0)
                size_hint_y: None
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: landmark
                hint_text: 'Enter LandMark '
                multiline: False
                helper_text: "Enter Valid LandMark"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            Spinner:
                id: no_of_employees_working
                text: "No of Employees Working"
                values: ["No of Employees Working","Less Than 50", "50-100", "100-150", "150-200", "Greater Than 200"]
                multiline: False
                size_hint: 1 , None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: reg_office_address
                hint_text: 'Enter Registered Office Address '
                multiline: False
                helper_text: "Enter valid Registration Office Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id: year_of_estd
                hint_text: 'Enter Year of Estd'
                multiline: False
                helper_text: "Enter valid Year of Estd"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(landmark.text,spin.text,no_of_employees_working.text,reg_office_address.text,year_of_estd.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"

<BorrowerScreen11>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen10')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-3'
                halign: 'center'
                bold: True

            Spinner:
                id: industry_type
                text: "Select Industry Type"
                values: ["Select Industry Type","Public", "Government"]
                multiline:False
                size_hint_y: (None)
                background_color: (0,0,0,0)
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: last_six_months_turnover
                hint_text: 'Enter Last 6 Months Turnover'
                multiline: False
                helper_text: "Enter valid 6 months Turnover"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_last_six_months_turnover_touch_down()

            MDLabel:
                text: "Last 6 months Bank Statements"
                bold:True
                halign: 'center'

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen11').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(industry_type.text,last_six_months_turnover.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen12>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None

            Spinner:
                id: spinner1
                text: "Please Select Employment Type"
                values: ["Employment Type","Full-Time", "Part-Time","Contract","Freelance","Intern"]
                multiline:False
                size_hint_y: None
                background_color: 0,0,0,0
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:              
                id:company_name
                hint_text: 'Enter company name'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            Spinner:
                id: spinner2
                text: "Please Select Organisation Type"
                values: ["Select Organisation Type","Cooperation","Partnership","Sole proprietorship","Hierarchical Organization"]
                multiline:False
                size_hint_y: None
                background_color: 0,0,0,0
                background_normal: ''
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spinner1.text, company_name.text, spinner2.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen13>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen12')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: ""
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                bold: True   
                size_hint_y: None

            MDTextField:              
                id: annual_salary
                hint_text: 'Enter Annual Salary'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text:  "Enter Valid Annual Salary"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True
                input_type: 'number'  
                on_touch_down: root.on_annual_salary_touch_down()

            MDTextField:              
                id: designation
                hint_text: 'Enter Designation'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                helper_text: "Enter Valid Designation"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                bold: True

            MDLabel:
                text: "Upload Employee ID"
                font_size: dp(18)
                halign: 'center'

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  # Adjust size as needed
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1 
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen13').check_and_open_file_manager1()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

            MDLabel:
                id: image_label1
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: "Upload Last 6 months Bank Statements"
                font_size: dp(18)
                halign: 'center'

            BoxLayout:
                orientation: 'horizontal'
                padding: "10dp"
                spacing: "10dp"
                size_hint: None, None
                size: dp(200), dp(50)  
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                canvas:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDIconButton:
                    icon: 'upload'
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1  # Black text color
                    size_hint_x: None
                    width: dp(24)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.root.get_screen('BorrowerScreen13').check_and_open_file_manager2()

                MDLabel:
                    id: upload_label1
                    text: 'Upload Document'
                    halign: 'left'
                    theme_text_color: "Custom"

            MDLabel:
                id: image_label2
                text: ''
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1  # Black text color
                valign: 'middle'  # Align the label text vertically in the center
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(annual_salary.text, designation.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"

<BorrowerScreen14>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen13')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Employment Details'
                halign: 'center'
                font_size: "25dp"
                font_name: "Roboto-Bold"

            MDTextField:              
                id:company_address
                hint_text: 'Enter company address'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:company_pincode
                hint_text: 'Enter Company Pincode'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_company_pincode_touch_down()

            MDTextField:              
                id:company_country
                hint_text: 'Enter Company Country'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:landmark
                hint_text: 'Enter landmark'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None

            MDTextField:              
                id:business_number
                hint_text: 'Enter Business Phone Number'
                multiline: False                        
                helper_text_mode: 'on_focus'
                size_hint_y: None
                input_type: 'number'  
                on_touch_down: root.on_business_phone_number_touch_down()

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(company_address.text, company_pincode.text, company_country.text, landmark.text, business_number.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen15>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Borrower Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            Spinner:
                id: marital_status_id
                text: "Please Select Marital Status"
                values: ["Select Marital Status","Married", "Un-Married", "Divorced"]
                size_hint: 1 , None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(marital_status_id.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"     

<BorrowerScreen16>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-1'
                halign: 'center'
                bold:True

            MDTextField:
                id: spouse_name
                hint_text: 'Enter Spouse Name '
                multiline: False
                helper_text: "Enter Valid Spouse Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDGridLayout:
                cols: 3
                spacing: dp(10)
                padding: dp(10)
                MDTextField:
                    id: spouse_date_textfield
                    hint_text: "Enter Date Of Birth"
                    helper_text: 'DD/MM/YYYY'
                    font_name: "Roboto-Bold"
                    hint_text_color: 0, 0, 0, 1


            MDTextField:
                id: spouse_mobile
                hint_text: 'Enter Spouse Mobile No'
                multiline: False
                helper_text: "Enter valid Spouse Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_spouse_mobile_touch_down()

            MDTextField:
                id: spouse_profession
                hint_text: 'Enter Spouse Profession '
                multiline: False
                helper_text: "Enter valid Spouse Profession"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_name.text, spouse_date_textfield.text, spouse_mobile.text, spouse_profession.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen17>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen16')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Step-2'
                halign: 'center'
                bold:True

            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter Spouse Company Name '
                multiline: False
                helper_text: 'Enter Valid Spouse Company Name '
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id: spouse_company_address
                hint_text: 'Enter Spouse Company Address'
                multiline: False
                helper_text: "Enter valid Spouse Company Address"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"

            MDTextField:
                id: spouse_annual_salary
                hint_text: 'Enter Annual Salary'
                multiline: False
                helper_text: 'Enter valid Annual Salary'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'
                on_touch_down: root.on_spouse_annual_salary_touch_down()

            MDTextField:
                id: spouse_office_no
                hint_text: 'Enter Spouse Office Number'
                multiline: False
                helper_text: "Enter valid Spouse Office No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'
                on_touch_down: root.on_spouse_office_no_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(spouse_company_name.text, spouse_company_address.text, spouse_annual_salary.text, spouse_office_no.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<BorrowerScreen18>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen15')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: account_holder_name
                hint_text: 'Enter Account Holder Name '
                helper_text: 'Enter valid account holder name'
                multiline: False
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                size_hint_y:None

            Spinner:
                id: account_type_id
                text: "Select Account Type"
                values: ["Select Account Type", "Savings Account", "Salary Account", "Current Account", "NRI Account", "Re-Curing Account"]
                size_hint: 1, None
                background_color: 0,0,0, 0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: account_number
                hint_text: 'Enter Account number '
                multiline: False
                helper_text: 'Enter valid Account number'
                helper_text_mode: 'on_focus'
                size_hint_y: None
                font_name: "Roboto-Bold"

            MDTextField:
                id: bank_name
                hint_text: 'Enter Bank Name '
                helper_text: 'Enter valid Bank Name'
                multiline: False
                helper_text_mode: 'on_focus'
                size_hint_y:None
                font_name: "Roboto-Bold"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Next"
                    on_release: root.add_data(account_holder_name.text, account_type_id.text, account_number.text, bank_name.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 

<BorrowerScreen19>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'BorrowerScreen18')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Applicant Bank Details'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: ifsc_code
                hint_text: 'Enter Bank ID '
                multiline: False
                helper_text: 'Enter valid Bank ID'
                helper_text_mode: 'on_focus'
                size_hint_y:None
                font_name: "Roboto-Bold"

            MDTextField:
                id: branch_name
                hint_text: 'Enter Branch Name'
                helper_text: 'Enter valid Branch Name'
                hint_text_mode: 'on_focus'
                multiline: False
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                multiline: False
                font_name: "Roboto-Bold"

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Submit"
                    on_release: root.go_to_borrower_dashboard(ifsc_code.text, branch_name.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 
'''

conn = sqlite3.connect("fin_user_profile.db")
cursor = conn.cursor()


class BorrowerScreen(Screen):
    Builder.load_string(Borrower)

    def validate_input(self, name, gender, date_of_birth):
        errors = []

        # Validate full name
        if not name or len(name.strip()) < 3:
            errors.append("Please enter a valid full name (at least 3 characters)")

        # Validate gender (optional, depending on your requirements)
        if gender not in ['Male', 'Female', 'Other']:
            errors.append("Please select a valid gender")

        # Validate date of birth
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            errors.append("Please enter a valid date of birth in the format YYYY-MM-DD")

        return errors

    def add_data(self, name, gender, date_of_birth):
        # Show modal view with spinner
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        validation_errors = self.validate_input(name, gender, date_of_birth)

        # Delay to simulate processing time (replace with your actual logic)
        Clock.schedule_once(lambda dt: self.process_data(name, gender, date_of_birth, modal_view, validation_errors), 2)

    def process_data(self, name, gender, date_of_birth, modal_view, validation_errors):
        # Close the modal view
        modal_view.dismiss()
        validation_errors = self.validate_input(name, gender, date_of_birth)

        if validation_errors:
            for error in validation_errors:
                self.show_validation_error(error)
            return

        if date_of_birth == '':
            self.ids.date_of_birth.error = True
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET name = ?, gender = ?,  date_of_birth = ? WHERE customer_id = ?",
                (name, gender, date_of_birth, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()

        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['full_name'] = name
            data[index]['gender'] = gender
            data[index]['date_of_birth'] = date_of_birth

        else:
            print("email not there")

        sm = self.manager
        borrower_screen = BorrowerScreen1(name='BorrowerScreen1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen1'

    def show_validation_error(self, error_text):
        # Show validation errors in a snackbar
        Snackbar(text=error_text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerLanding'


class BorrowerScreen1(Screen):

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'

    def add_data(self, mobile_number, alternate_email, spinner_id):
        # Show modal view with spinner
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action1(mobile_number, alternate_email, modal_view),
                            2)

    def perform_data_addition_action1(self, mobile_number, alternate_email, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET mobile_number = ?, alternate_email = ? WHERE customer_id = ?",
                (mobile_number, alternate_email, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['mobile'] = mobile_number
            data[index]['another_email'] = alternate_email
        else:
            print('no email found')
        # self.manager.current = 'BorrowerScreen2'
        sm = self.manager
        borrower_screen = BorrowerScreen2(name='BorrowerScreen2')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen2'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen'


class BorrowerScreen2(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen2').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen2').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'

    def add_data(self, aadhar_number, pan_number):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action2(aadhar_number, pan_number, modal_view), 2)

    def perform_data_addition_action2(self, aadhar_number, pan_number, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET aadhar_number = ?, pan_number = ? WHERE customer_id = ?",
                           (aadhar_number, pan_number, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['aadhaar_no'] = aadhar_number
            data[index]['pan_number'] = pan_number
        else:
            print('no email found')
        # self.manager.current = 'BorrowerScreen3'
        sm = self.manager
        borrower_screen = BorrowerScreen3(name='BorrowerScreen3')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen3'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen1'


class BorrowerScreen3(Screen):

    def next_pressed(self, id):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action3(modal_view, id), 2)

    def perform_loan_request_action3(self, modal_view, id):
        # Close the modal view after performing the action
        modal_view.dismiss()
        if id == '10th class':
            BorrowerScreen_Edu_10th()
            sm = self.manager
            lender_screen = BorrowerScreen_Edu_10th(name='BorrowerScreen_Edu_10th')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen_Edu_10th'

        elif id == 'Intermediate':
            BorrowerScreen_Edu_Intermediate()
            sm = self.manager
            lender_screen = BorrowerScreen_Edu_Intermediate(name='BorrowerScreen_Edu_Intermediate')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen_Edu_Intermediate'

        elif id == 'Bachelors':
            # self.manager.current = 'BorrowerScreen_Edu_Bachelors'
            sm = self.manager
            lender_screen = BorrowerScreen_Edu_Bachelors(name='BorrowerScreen_Edu_Bachelors')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen_Edu_Bachelors'
        elif id == 'Masters':
            # self.manager.current = 'BorrowerScreen_Edu_Masters'
            sm = self.manager
            lender_screen = BorrowerScreen_Edu_Masters(name='BorrowerScreen_Edu_Masters')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen_Edu_Masters'
        elif id == 'PHD':
            # self.manager.current = 'BorrowerScreen_Edu_PHD'
            sm = self.manager
            lender_screen = BorrowerScreen_Edu_PHD(name='BorrowerScreen_Edu_PHD')
            sm.add_widget(lender_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'BorrowerScreen_Edu_PHD'
        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                           (id, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')
        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['qualification'] = id
        else:
            print('email not found')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen2'


class BorrowerScreen_Edu_10th(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):

        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_10th').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        else:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

    def go_to_borrower_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action10th(modal_view), 2)

    def perform_loan_request_action10th(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        borrower_screen = BorrowerScreen4(name='BorrowerScreen4')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(borrower_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerScreen4'


class BorrowerScreen_Edu_Intermediate(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Intermediate').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Intermediate').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

    def go_to_borrower_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action11th(modal_view), 2)

    def perform_loan_request_action11th(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        borrower_screen = BorrowerScreen4(name='BorrowerScreen4')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(borrower_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerScreen4'


class BorrowerScreen_Edu_Bachelors(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Bachelors').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Bachelors').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Bachelors').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

    def go_to_borrower_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action_bachelors(modal_view), 2)

    def perform_loan_request_action_bachelors(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        borrower_screen = BorrowerScreen4(name='BorrowerScreen4')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(borrower_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerScreen4'


class BorrowerScreen_Edu_Masters(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label4")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path4(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_Masters').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

    def go_to_borrower_screen(self):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_masters_action(modal_view), 2)

    def perform_masters_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        borrower_screen = BorrowerScreen4(name='BorrowerScreen4')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(borrower_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerScreen4'


class BorrowerScreen_Edu_PHD(Screen):
    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3")

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label4")

    def check_and_open_file_manager5(self):
        self.check_and_open_file_manager("upload_icon5", "upload_label5", "selected_file_label5", "selected_image5",
                                         "image_label5")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path4(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path5(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen_Edu_PHD').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label5.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')
            # Handle the case where the user is not logged in, possibly by displaying an error message to the user.

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'

    def go_to_borrower_screen(self):
        # Show modal view with spinner
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_phd_action(modal_view), 2)

    def perform_phd_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        borrower_screen = BorrowerScreen4(name='BorrowerScreen4')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(borrower_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerScreen4'


class BorrowerScreen4(Screen):
    def add_data(self, street, city, zip_code, state, country):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(street, city, zip_code, state, country, modal_view), 2)

    def perform_data_addition_action4(self, street, city, zip_code, state, country, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')

        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET street_name = ?, city_name = ?, zip_code = ?, state_name = ?, country_name = ? WHERE customer_id = ?",
                (street, city, zip_code, state, country, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['city'] = city
            data[index]['street'] = street
            data[index]['pincode'] = zip_code
            data[index]['state'] = state
            data[index]['country'] = country
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen5(name='BorrowerScreen5')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen5'

    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.zip_code.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen3'


class BorrowerScreen5(Screen):

    def on_father_age_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_age.input_type = 'number'

    def on_father_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_ph_no.input_type = 'number'

    def add_data(self, father_name, father_age, father_occupation, father_ph_no):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(father_name, father_age, father_occupation, father_ph_no,
                                                         modal_view), 2)

    def perform_data_addition_action(self, father_name, father_age, father_occupation, father_ph_no, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET father_name = ?, father_age = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
                (father_name, father_age, father_occupation, father_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['father_name'] = father_name
            data[index]['father_age'] = father_age
            data[index]['father_occupation'] = father_occupation
            data[index]['father_number'] = father_ph_no
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen6(name='BorrowerScreen6')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen6'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen4'


class BorrowerScreen6(Screen):

    def on_mother_age_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_age.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_ph_no.input_type = 'number'

    def add_data(self, mother_name, mother_age, mother_occupation, mother_ph_no):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(mother_name, mother_age, mother_occupation, mother_ph_no,
                                                         modal_view), 2)

    def perform_data_addition_action(self, mother_name, mother_age, mother_occupation, mother_ph_no, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET mother_name = ?, mother_age = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
                (mother_name, mother_age, mother_occupation, mother_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['mother_name'] = mother_name
            data[index]['mother_age'] = mother_age
            data[index]['mother_occupation'] = mother_occupation
            data[index]['mother_number'] = mother_ph_no
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen7(name='BorrowerScreen7')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen7'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen5'


class BorrowerScreen7(Screen):

    def add_data(self, spinner_id):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spinner_id, modal_view), 2)

    def perform_data_addition_action(self, spinner_id, modal_view):
        modal_view.dismiss()
        if spinner_id == 'Student':
            sm = self.manager
            borrower_screen = BorrowerScreen8(name='BorrowerScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen8'

        elif spinner_id == 'Business':
            sm = self.manager
            borrower_screen = BorrowerScreen9(name='BorrowerScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen9'

        elif spinner_id == 'Employee':
            sm = self.manager
            borrower_screen = BorrowerScreen12(name='BorrowerScreen12')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen12'
        print(spinner_id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []

        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET proficient_type = ? WHERE customer_id = ?",
                (spinner_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['profficen'] = spinner_id
        else:
            print('no email found')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen5'


class BorrowerScreen8(Screen):

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):

        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen8').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def add_data(self, collage_name, college_address, collage_id):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(collage_name, college_address, collage_id, modal_view), 2)

    def perform_data_addition_action(self, collage_name, college_address, collage_id, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            # Check if any user is logged in
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET collage_name = ?, college_address = ?, college_id = ? WHERE customer_id = ?",
                (collage_name, college_address, collage_id, row_id_list[log_index]))
            conn.commit()

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")
            print("Moving to BorrowerScreen15...")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['college_name'] = collage_name
            data[index]['college_address'] = college_address
            data[index]['college_id'] = collage_id
        else:
            print('email not found')
        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen9(Screen):
    def add_data(self, business_name, business_location, business_address):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(business_name, business_location, business_address,
                                                         modal_view), 2)

    def perform_data_addition_action(self, business_name, business_location, business_address, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET business_name = ?, business_location = ?, business_address = ? WHERE customer_id = ?",
                (business_name, business_location, business_address, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['business_name'] = business_name
            data[index]['business_add'] = business_address
            data[index]['business_location'] = business_location
        else:
            print('no email found')

        sm = self.manager
        borrower_screen = BorrowerScreen10(name='BorrowerScreen10')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen10'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen10(Screen):
    def add_data(self, landmark, business_type, no_of_employees_working, registered_office_address, year_of_estd):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(landmark, business_type, no_of_employees_working,
                                                         registered_office_address, year_of_estd, modal_view), 2)

    def perform_data_addition_action(self, landmark, business_type, no_of_employees_working, registered_office_address,
                                     year_of_estd, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET landmark = ?, business_type = ?, no_of_employees_working = ?, registered_office_address= ?, year_of_estd = ? WHERE customer_id = ?",
                (landmark, business_type, no_of_employees_working, registered_office_address, year_of_estd,
                 row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['registered_off_add'] = registered_office_address
            data[index]['business_type'] = business_type
            data[index]['employees_working'] = no_of_employees_working
            data[index]['year_estd'] = year_of_estd
            data[index]['company_landmark'] = landmark
        else:
            print('no email found')
        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen9'


class BorrowerScreen11(Screen):

    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):

        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen11').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def add_data(self, industry_type, last_six_months_turnover):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(industry_type, last_six_months_turnover, modal_view), 2)

    def perform_data_addition_action(self, industry_type, last_six_months_turnover, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET industry_type = ?, last_six_months_turnover = ? WHERE customer_id = ?",
                (industry_type, last_six_months_turnover, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['industry_type'] = industry_type
            data[index]['six_month_turnover'] = last_six_months_turnover
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen12(name='BorrowerScreen12')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen12'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen12(Screen):

    def add_data(self, employment_type, company_name, organization):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(employment_type, company_name, organization, modal_view), 2)

    def perform_data_addition_action(self, employment_type, company_name, organization, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
                (employment_type, company_name, organization, row_id_list[log_index]))
            conn.commit()

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['employment_type'] = employment_type
            data[index]['company_name'] = company_name
            data[index]['organization_type'] = organization
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen13(name='BorrowerScreen13')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen13'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen7'


class BorrowerScreen14(Screen):

    def add_data(self, company_address, company_pincode, company_country, landmark, business_number):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(company_address, company_pincode, company_country, landmark,
                                                         business_number, modal_view), 2)

    def perform_data_addition_action(self, company_address, company_pincode, company_country, landmark, business_number,
                                     modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET company_address = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
                (company_address, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['company_address'] = company_address
            data[index]['company_landmark'] = landmark
            data[index]['business_no'] = business_number
            data[index]['company_country'] = company_country
            data[index]['company_pincode'] = company_pincode
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen15(name='BorrowerScreen15')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen15'

    def on_company_pincode_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pincode.input_type = 'number'

    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_number.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen13'


class BorrowerScreen13(Screen):

    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1")

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen13').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('BorrowerScreen13').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def add_data(self, annual_salary, designation):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(annual_salary, designation, modal_view), 2)

    def perform_data_addition_action(self, annual_salary, designation, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
                (annual_salary, designation, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['annual_salary'] = annual_salary
            data[index]['designation'] = designation
        else:
            print('email not found')

        sm = self.manager
        borrower_screen = BorrowerScreen14(name='BorrowerScreen14')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'
        sm.current = 'BorrowerScreen14'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen12'


class BorrowerScreen15(Screen):

    def add_data(self, marital_status_id):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(marital_status_id, modal_view), 2)

    def perform_data_addition_action(self, marital_status_id, modal_view):
        modal_view.dismiss()
        if marital_status_id == 'Un-Married':
            sm = self.manager
            borrower_screen = BorrowerScreen18(name='BorrowerScreen18')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen18'

        elif marital_status_id == 'Married':
            sm = self.manager
            borrower_screen = BorrowerScreen16(name='BorrowerScreen16')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen16'

        elif marital_status_id == 'Divorced':
            sm = self.manager
            borrower_screen = BorrowerScreen18(name='BorrowerScreen18')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'BorrowerScreen18'

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET marital_status = ? WHERE customer_id = ?",
                (marital_status_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['marital_status'] = marital_status_id
        else:
            print('email not found')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen6'


class BorrowerScreen16(Screen):

    def on_spouse_mobile_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_mobile.input_type = 'number'

    def add_data(self, spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(spouse_name, spouse_date_textfield, spouse_mobile,
                                                         spouse_profession, modal_view), 2)

    def perform_data_addition_action(self, spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession,
                                     modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ?, spouse_profession = ? WHERE customer_id = ?",
                (spouse_name, spouse_date_textfield, spouse_mobile, spouse_profession, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()

        id_list = [i['email_user'] for i in data]

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['spouse_name'] = spouse_name
            data[index]['spouse_mobile'] = spouse_mobile
            data[index]['spouse_date'] = str(spouse_date_textfield)
            data[index]['spouse_profession'] = spouse_profession
        else:
            print("email not there")

        sm = self.manager
        borrower_screen = BorrowerScreen17(name='BorrowerScreen17')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen17'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen17(Screen):

    def on_spouse_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_annual_salary.input_type = 'number'

    def on_spouse_office_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_office_no.input_type = 'number'

    def add_data(self, spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spouse_company_name, spouse_company_address,
                                                                         spouse_annual_salary, spouse_office_no,
                                                                         modal_view), 2)

    def perform_data_addition_action(self, spouse_company_name, spouse_company_address, spouse_annual_salary,
                                     spouse_office_no, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ?, spouse_office_no = ? WHERE customer_id = ?",
                (spouse_company_name, spouse_company_address, spouse_annual_salary, spouse_office_no,
                 row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['spouse_company_name'] = spouse_company_name
            data[index]['spouse_company_address'] = spouse_company_address
            data[index]['spouse_annual_salary'] = spouse_annual_salary
            data[index]['spouse_office_no'] = spouse_office_no
        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen18(name='BorrowerScreen18')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen18'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen16'


class BorrowerScreen18(Screen):
    def add_data(self, account_holder_name, account_type, account_number, bank_name):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(account_holder_name, account_type, account_number, bank_name,
                                                         modal_view), 2)

    def perform_data_addition_action(self, account_holder_name, account_type, account_number, bank_name, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ? WHERE customer_id = ?",
                (account_holder_name, account_type, account_number, bank_name, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['account_name'] = account_holder_name
            data[index]['account_type'] = account_type
            data[index]['account_number'] = account_number
            data[index]['bank_name'] = bank_name
        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = BorrowerScreen19(name='BorrowerScreen19')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'BorrowerScreen19'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen15'


class BorrowerScreen19(Screen):

    def go_to_borrower_dashboard(self, bank_id, branch_name):
        modal_view = ModalView(size_hint=(None, None), size=(100, 100), background_color=[0, 0, 0, 0])
        spinner = MDSpinner()
        modal_view.add_widget(spinner)
        modal_view.open()

        # Perform the actual action (e.g., adding data)
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(bank_id, branch_name, modal_view), 2)

    def perform_data_addition_action(self, bank_id, branch_name, modal_view):
        modal_view.dismiss()
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        b = 'borrower'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET bank_id = ?, branch_name = ?, user_type = ?  WHERE customer_id = ?",
                (bank_id, branch_name, b, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')
        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['bank_id'] = bank_id
            data[index]['account_bank_branch'] = branch_name
            data[index]['usertype'] = b
            data[index]['registration_approve'] = True
        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = DashboardScreen(name='DashboardScreen')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'DashboardScreen'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerScreen18'


class MyScreenManager(ScreenManager):
    pass
