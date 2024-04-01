
from anvil.tables import app_tables
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from lender_lost_opportunities import LostOpportunitiesScreen
from lender_view_loans import ViewLoansScreen
from lender_view_loans_request import ViewLoansRequest
from lender_view_extension_request import NewExtension
from lender_foreclosure_request import DashboardScreenLF
from lender_today_due import TodayDuesTD
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.label import MDLabel

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

user_helpers1 = """
<WindowManager>:
    LenderDashboard:
    ViewProfileScreen:

<LenderDashboard>
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint:(1,1)# Make the size stretchable

        MDTopAppBar:
            md_bg_color:1,1,1,1
            specific_text_color:1/255, 26/255, 51/255, 1
            elevation:2
            left_action_items: [['account', lambda x: root.profile()]]
            right_action_items: [['wallet', lambda x:root.go_to_wallet()],['logout', lambda x: root.logout()]]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        Image:
            source:"LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.956}
            size_hint: None,None
            md_bg_color:0,0,0,1

            height: dp(50)
            width: dp(60)
        MDGridLayout:
            cols: 3
            spacing:dp(15)

            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None
            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.newloan_extension()

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Loan Extensions"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:0.043, 0.145, 0.278, 1 
                on_release: root.view_loan_foreclose()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Loan Foreclosure"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:0.043, 0.145, 0.278, 1 
                on_release: root.lender_today_due()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Today's Dues"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:0.043, 0.145, 0.278, 1  
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.view_loan_request()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Loan Request"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color:0.043, 0.145, 0.278, 1 
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.view_loanscreen()

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.view_lost_opportunities()
                md_bg_color: 0.043, 0.145, 0.278, 1 
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Lost Opportunities"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text:""
            MDFlatButton:
                size_hint: None, None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "View Transaction History"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDIconButton:
            icon:'help-circle'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_x': 0.92, 'center_y': 0.1}
            on_release: root.help_module()
            md_bg_color: 0.043, 0.145, 0.278, 1              
<ViewProfileScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(35)
                spacing:dp(20)
                size_hint_y: None
                height: self.minimum_height

                MDRectangleFlatButton:

                    line_color:1,1,1,1
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    canvas.before:
                        Color:
                            rgba: 174/255, 214/255, 241/255, 1
                        Ellipse:
                            size: self.size
                            pos: self.pos 

                    Image:
                        id: selected_image1
                        source: "profile.png"

                    MDFloatLayout:

                        size_hint:(None,None)
                        spacing:0
                        padding:0
                        pos_hint: {'center_x': 0, 'center_y': 0}
                        MDIconButton:
                            icon: 'camera-plus'
                            on_release: app.root.get_screen('ViewProfileScreen').check_and_open_file_manager1()
                            pos_hint: {'center_x':1.2, 'center_y':0}
                Label:
                    id: selected_file_label
                    text: 'Selected File: None'
                    size_hint_y: None
                    height: 30

                MDLabel:
                    text: ' Customer ID '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: customer_id
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        readonly: True

                MDLabel:
                    text: ' Full Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        id: edit_button
                        size_hint: None, None
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"


                    MDTextField:
                        id: username
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Mobile Number '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input1
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]



                MDLabel:
                    text: ' Date Of Birth '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: text_input2
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Gender '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True
                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: text_input3
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Alternate email '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input4
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Government ID1 '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input5
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True

                MDLabel:
                    text: ' Government ID2 '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width



                    MDTextField:
                        id: text_input6
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True

                MDLabel:
                    text: ' Highest Qualification'
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input7
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold" 


                MDLabel:
                    text: ' Street Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input8
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                MDLabel:
                    text: ' City Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input9
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                MDLabel:
                    text: ' Zipcode '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input10
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"


                MDLabel:
                    text: ' State Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input110
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Country Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input11
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Loan Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input12
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True

                MDLabel:
                    text: ' Investment '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input13
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Lending Period '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input14
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' User Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDTextField:
                        id: text_input15
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"
                        readonly: True


                MDLabel:
                    text: ' Account Holder Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input16
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Account Type '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input17
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



                MDLabel:
                    text: ' Account Number '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input18
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Bank Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input19
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Bank ID '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input20
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

                MDLabel:
                    text: ' Branch Name '
                    color: 0, 0, 0, 1
                    halign: 'left'
                    size_hint_x: 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    bold: True

                MDFloatLayout:
                    size_hint: None, None
                    size: dp(200), dp(40)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 1
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1  # Set background color to white
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [10, 10, 10, 10]

                        Color:
                            rgba: 0, 0, 0, 1  # Set border color to black

                        Line:
                            rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                            width: 1  # Border line width

                    MDFlatButton:
                        text: "EDIT"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color:6/255, 143/255, 236/255, 1
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: text_input21
                        size_hint: None, None
                        size_hint_x: 0.91
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [1, 1, 1, 1]  
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"

"""

conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()


class LenderDashboard(Screen):
    Builder.load_string(user_helpers1)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderLanding'

        # Replace with the actual name of your previous screen

    def homepage(self):
        self.manager.current = 'MainScreen'

    def logout(self):
        self.manager.current = 'MainScreen'

    def profile(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.permformance_profile(modal_view), 2)

    def permformance_profile(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewProfileScreen(name='ViewProfileScreen'))
        self.manager.current = 'ViewProfileScreen'

    def lender_today_due(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_lender_today_due(modal_view), 2)

    def view_lost_opportunities(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_lost_opportunities(modal_view), 2)

    def perform_view_lost_opportunities(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.LostOpportunitiesScreen(name='LostOpportunitiesScreen'))
        self.manager.current = 'LostOpportunitiesScreen'

    def performance_lender_today_due(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.TodayDuesTD(name='TodayDuesTD'))
        self.manager.current = 'TodayDuesTD'

    def view_loan_request(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action(modal_view), 2)

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def perform_loan_request_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewLoansRequest(name='ViewLoansRequest'))
        self.manager.current = 'ViewLoansRequest'

    def view_loanscreen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_loanscreen(modal_view), 2)

    def perform_view_loanscreen(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewLoansScreen(name='ViewLoansScreen'))
        self.manager.current = 'ViewLoansScreen'

    def newloan_extension(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_newloan_extension(modal_view), 2)

    def perform_newloan_extension(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()

        self.manager.add_widget(Factory.NewExtension(name='NewExtension'))
        self.manager.current = 'NewExtension'

    def view_loan_foreclose(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_view_loan_foreclose(modal_view), 2)

    def performance_view_loan_foreclose(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.DashboardScreenLF(name='DashboardScreenLF'))
        self.manager.current = 'DashboardScreenLF'

    def go_to_wallet(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_wallet(modal_view), 2)

    def perform_wallet(self, modal_view):
        from lender_wallet import LenderWalletScreen

        modal_view.dismiss()
        self.manager.add_widget(Factory.LenderWalletScreen(name='LenderWalletScreen'))
        self.manager.current = 'LenderWalletScreen'
        # Get the existing ScreenManager

    def help_module(self):
        from help_module import HelpScreen
        self.manager.add_widget(Factory.HelpScreen(name='HelpScreen'))
        self.manager.current = 'HelpScreen'


class ViewProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        email = self.get_email()
        data = app_tables.fin_user_profile.search()
        customer = []
        email1 = []
        name = []
        mobile = []
        date_of_birth = []
        gender = []
        alternate_email = []
        government_type1 = []
        government_type2 = []
        highest_qualification = []
        street_name = []
        city = []
        zipcode = []
        state = []
        country = []
        loan_type1 = []
        investment = []
        lending_period = []
        user_type = []
        acholder_name = []
        account_type = []
        account_number = []
        bank_name = []
        bank_id = []
        branch_name = []
        for row in data:
            customer.append(row['customer_id'])
            email1.append(row['email_user'])
            name.append(row['full_name'])
            mobile.append(row['mobile'])
            date_of_birth.append(row['date_of_birth'])
            gender.append(row['gender'])
            alternate_email.append(row['another_email'])
            government_type1.append(row['aadhaar_no'])
            government_type2.append(row['pan_number'])
            highest_qualification.append(row['qualification'])
            street_name.append(row['street'])
            city.append(row['city'])
            zipcode.append(row['pincode'])
            state.append(row['state'])
            country.append(row['country'])
            loan_type1.append(row['loan_type'])
            investment.append(row['investment'])
            lending_period.append(row['lending_period'])
            user_type.append(row['usertype'])
            acholder_name.append(row['account_name'])
            account_type.append(row['account_type'])
            account_number.append(row['account_number'])
            bank_name.append(row['bank_name'])
            bank_id.append(row['bank_id'])
            branch_name.append(row['account_bank_branch'])

        if email in email1:
            index = email1.index(email)
            self.ids.customer_id.text = str(customer[index])
            self.ids.username.text = str(name[index])
            self.ids.text_input1.text = str(mobile[index])
            self.ids.text_input2.text = str(date_of_birth[index])
            self.ids.text_input3.text = str(gender[index])
            self.ids.text_input4.text = str(alternate_email[index])
            self.ids.text_input5.text = str(government_type1[index])
            self.ids.text_input6.text = str(government_type2[index])
            self.ids.text_input7.text = str(highest_qualification[index])
            self.ids.text_input8.text = str(street_name[index])
            self.ids.text_input9.text = str(city[index])
            self.ids.text_input10.text = str(zipcode[index])
            self.ids.text_input110.text = str(state[index])
            self.ids.text_input11.text = str(country[index])
            self.ids.text_input12.text = str(loan_type1[index])
            self.ids.text_input13.text = str(investment[index])
            self.ids.text_input14.text = str(lending_period[index])
            self.ids.text_input15.text = str(user_type[index])
            self.ids.text_input16.text = str(acholder_name[index])
            self.ids.text_input17.text = str(account_type[index])
            self.ids.text_input18.text = str(account_number[index])
            self.ids.text_input19.text = str(bank_name[index])
            self.ids.text_input20.text = str(bank_id[index])
            self.ids.text_input21.text = str(branch_name[index])

        else:
            print("email not Found")

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.ids[image_id].source = path  # Set the source of the Image widget
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

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'  # Replace with the actual name of your previous screen

    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'


class MyScreenManager(ScreenManager):
    pass