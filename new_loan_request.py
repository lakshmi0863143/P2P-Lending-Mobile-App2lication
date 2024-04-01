import anvil
from anvil import tables
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivymd.uix.list import OneLineListItem
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.factory import Factory

import server
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ListProperty, Clock
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime

from kivymd.uix.spinner import MDSpinner

user_helpers2 = """

<WindowManager>:
    NewloanScreen:
    NewloanScreen1:
    NewloanScreen2:
    MenuScreen:
        name: 'menu'
    PaymentDetailsScreen:
        name: 'payment_details'


<NewloanScreen>:
    name: 'NewloanScreen' 
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "New Loan Request"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['home', lambda x:root.go_to_lender_dashboard()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(25)
                size_hint_y: None
                height: self.minimum_height


                Image:
                    source:"LOGO.png"
                    size_hint:None,None
                    size:"100dp","100dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.89}
                MDLabel:
                    text: "  Experience Hassle-Free Borrowing  " 
                    font_size:dp(15)
                    halign:"center"
                    bold:True
                    height:dp(50)
                    underline:True
                    italic:True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}

                MDGridLayout:
                    cols: 2
                    padding: dp(25)
                    spacing: dp(10)
                    MDLabel:
                        text: "Credit Limit" 
                        color:0.031, 0.463, 0.91, 1
                        bold:True
                        size_hint_y:None
                        height:dp(50)
                        halign: "left"
                        font_size:dp(23)
                    MDLabel:
                        id: credit_limit        
                        text: "" 
                        size_hint_y:None
                        height:dp(50)
                        halign: "center"
                        font_size:dp(20)
                MDLabel:
                    text:""
                MDLabel:
                    text:""

                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size: dp(16)
                        text: "Product Group"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "left"

                    Spinner:
                        id: group_id1
                        text: "Select Group"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        height:dp(40)
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_groups()
                        text_size: self.width - dp(20), None
                MDLabel:
                    text:""
                MDLabel:
                    text:""


                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size:dp(16)
                        text: "Product Categories"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "left"

                    Spinner:
                        id: group_id2
                        text: "Select Categories"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        height:dp(40)
                        halign: "center"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_categories()
                        text_size: self.width - dp(20), None
                        disabled: not group_id1.text or group_id1.text == 'Select Group'
                MDLabel:
                    text:""
                MDLabel:
                    text:""

                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size:dp(16)
                        text: "Product Name"
                        bold: True
                        size_hint_y:None
                        height:dp(50)
                        halign: "left"
                    Spinner:
                        id: group_id3
                        text: "Select product name"
                        width: dp(200)
                        multiline: False
                        size_hint: None, None
                        height:dp(40)
                        halign: "center"
                        pos_hint: {'center_x':0.5, 'center_y':0.5}
                        size: "180dp", "45dp"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                        on_press: app.fetch_product_name()
                        text_size: self.width - dp(20), None
                        disabled: not group_id2.text or group_id2.text == 'Select Categories'
                        on_text: app.fetch_product_description()
                MDLabel:
                    text: " "  
                MDLabel:
                    text:"" 
                MDLabel:
                    text:""


                MDGridLayout:
                    cols: 2

                    padding: dp(25)
                    spacing: dp(20)
                    MDLabel:
                        font_size: dp(16)
                        text: "Product Description"
                        bold: True
                    MDLabel:
                        id: product_description
                        text: " "
                        font_size: dp(11)
                        size_hint_y: None
                        halign: "center"
                        padding: [dp(5), dp(5)]
                        height: self.texture_size[1] + dp(20) if self.text else 0 # Adjust height to fit content
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1  # Background color
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                            Color:
                                rgba: 1, 1, 1, 1
                            Line:
                                width: 0.3
                                rectangle: (self.x, self.y, self.width, self.height)
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "
                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "


                MDFloatLayout:
                    MDRaisedButton:
                        text: "Next"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        on_release: root.go_to_newloan_screen1()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint:0.4, None  
                        font_name:"Roboto-Bold"

                MDLabel:
                    text: " "  
                MDLabel:
                    text: " "
<NewloanScreen1>:
    MDTopAppBar:
        title: "New Loan Request"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: root.go_back()]]
        right_action_items: [['home', lambda x:root.go_to_lender_dashboard()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.43}
        elevation: 2
        padding: dp(20)
        spacing: dp(10)
        orientation: 'vertical'
        radius: [10,]

        BoxLayout:
            orientation: "vertical"
            padding:dp(10)
            spacing:dp(10)
            size_hint_y: None
            height: self.minimum_height


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"70dp","70dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}




        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)
            MDLabel:
                text: "Loan Amount :"
                bold:True
                font_size:dp(16)
            MDTextField:
                id: text_input1
                width: dp(250)
                multiline: False
                hint_text: "Enter amount"
                size_hint: None, None
                size: "180dp", "45dp"
                on_text: root.validate_amount(text_input1,self.text)
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  # Set the line color to black
                color: 0, 0, 0, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                helper_text: ""
        MDLabel:
            text:""
        MDLabel:
            text:""


        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)   
            MDLabel:
                text: "Interest Rate(%) :"
                bold:True
                font_size:dp(16)

            MDLabel:
                id: roi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"left"
        MDLabel:
            text:""


        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)

            MDLabel:
                text: "Processing Fee(%) :"
                bold:True
                font_size:dp(16)

            MDLabel:
                id: processing_fee
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"

        MDLabel:
            text:""

        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)

            MDLabel:
                text: "Loan Period (Months):"
                font_size:dp(16)
                bold:True

            MDTextField:
                id: text_input2
                size_hint_x: 0.91
                multiline: False
                hint_text: "Enter loan period"
                on_text: root.validate_tenure(text_input2,self.text)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                helper_text: ""
                helper_text_mode: "on_error"
                size_hint: None, None
                size: "180dp", "45dp"
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  # Set the line color to black
                color: 0, 0, 0, 1
        MDLabel:
            id: max_tenure 
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            text:""
        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(10)
            MDLabel:
                font_size: dp(16)
                text: "EMI Type"
                bold: True

            Spinner:
                id: group_id4
                text: "Select EMI type"
                width: dp(200)
                multiline: False
                size_hint: None, None
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                size: "180dp", "45dp"
                height:dp(40)
                background_color: 1, 1, 1, 0
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.25
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                on_press: app.fetch_emi_type()
                text_size: self.width - dp(20), None
                disabled: not group_id4.text or group_id4.text == 'Select Categories'

        MDLabel:
            id: min_tenure 
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            text:""


        MDGridLayout:
            cols: 2
            padding: dp(25)
            spacing: dp(5)

            MDLabel:
                text: "Payment Details"
                font_size:dp(16)
                bold:True

            Button:
                text:'View Payment Details here'
                background_color: 0, 0, 0, 0
                color: 0, 0.5, 1, 1
                font_size: '15sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'center_x': 0.22, 'center_y': 0.5}
                on_release: root.go_to_menu_screen()
                halign:"left"


        MDLabel:
            id: max_amount
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)


        MDLabel:
            text:""

        MDFloatLayout:
            MDRaisedButton:
                text: "Next"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release:  root.go_to_newloan_screen2()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)
        MDLabel:
            id: min_amount
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)
        MDLabel:
            id: product_id
            color:1,1,1,1      
            text: "" 
            font_size:dp(1)


<NewloanScreen2>:
    MDTopAppBar:
        title: "View Deatils"
        elevation: 2
        pos_hint: {'top': 1}

        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        padding: dp(20)
        spacing: dp(20)
        orientation: 'vertical'

        BoxLayout:
            orientation: "vertical"


            size_hint_y: None
            height: self.minimum_height


            Image:
                source:"LOGO.png"
                size_hint:None,None
                size:"50dp","50dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDGridLayout:
            cols: 1

            MDLabel:
                text: "Loan Summary"
                halign: "center"
                font_size:dp(20)
                bold: True
                underline:"True"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Loan Amount"
                bold:True

            MDLabel:
                id: loan_amount
                text: ""
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Total Interest Amount"
                bold:True

            MDLabel:
                id: total_interest_amount
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"left"
        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: " Total Processing Fee Amount "
                bold:True

            MDLabel:
                id: total_processing_fee_amount
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Monthly EMI"
                bold:True

            MDLabel:
                id: monthly_emi
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: ""
                halign:"left"

        MDGridLayout:
            cols: 2
            spacing:dp(30)
            padding:dp(50)

            MDLabel:
                text: "Total Repayment Amount"
                bold:True

            MDLabel:
                id: total
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                text: " "
                halign:"left"

        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDFloatLayout:
            GridLayout:
                cols: 3
                spacing:dp(20)
                padding:dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size_hint: 1, None
                height: "50dp"
                MDRaisedButton:
                    text: "Back"
                    on_release: app.root.current = "NewloanScreen1"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                MDRaisedButton:
                    text: "Send request"
                    on_release: root.send_request()
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

        MDLabel:
            text: " "
<MenuScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)


        MDTopAppBar:
            title: "Payment Schedule"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            MDList:
                id: container

<PaymentDetailsScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        MDTopAppBar:
            title: "Payment Schedule"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_to_menu_screen() ]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Beginning Balance:"
                bold: True
            MDLabel:
                id: beginning_balance_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)


        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Scheduled Payment:"
                bold: True
            MDLabel:
                id: emi_label
                text: "Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)

        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Interest Amount:"
                bold: True
            MDLabel:
                id: interest_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)

        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Processing Amount:"
                bold: True
            MDLabel:
                id: processing_fee_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)

        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Principal Amount:"
                bold: True
            MDLabel:
                id: principal_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)
        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Total Payment:"
                bold: True
            MDLabel:
                id: total_payment_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)

        MDGridLayout:
            cols: 2

            padding: dp(25)
            spacing: dp(20)
            MDLabel:
                font_size: dp(16)
                text: "Ending Balance:"
                bold: True
            MDLabel:
                id: balance_label
                text: " Rs. 0.00"
                font_size: dp(11)
                size_hint_y: None
                halign: "center"
                padding: dp(5)
                height: self.texture_size[1] + dp(10) if self.text else 0  # Adjust height to fit content
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Background color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15, 15, 15, 15]  # Adjust radius for rounded corners
                    Color:
                        rgba: 0.043, 0.145, 0.278, 1
                    Line:
                        width: 0.25
                        rectangle: (self.x, self.y, self.width, self.height)



        MDRaisedButton:
            text: "Back"
            on_press: root.manager.current = 'menu'
            md_bg_color: 0.043, 0.145, 0.278, 1
            pos_hint: {'right': 1, 'y': 0.5}
            size_hint: 1, None
            height: "50dp"
            font_name: "Roboto-Bold"

"""

Builder.load_string(user_helpers2)


class NewloanScreen(Screen):
    # Add this line to check if the build method is called

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.on_back_button)
        try:
            # Get the first row from the 'fin_borrower' table
            row = app_tables.fin_borrower.search()[0]  # Fetch the first row

            # Fetch the credit limit from the row
            credit_limit = row['credit_limit']

            # Update the credit_limit MDLabel with the fetched data
            self.ids.credit_limit.text = str(credit_limit)
        except Exception as e:
            print(f"Error: {e}")

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def go_to_lender_dashboard(self):
        self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
        self.manager.current = 'DashboardScreen'

    def current(self):
        self.manager.current = 'DashboardScreen'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_newloan_screen1(self):
        # Check if all required fields are selected
        if (self.ids.group_id1.text == 'Select Group' or
                self.ids.group_id2.text == 'Select Categories' or
                self.ids.group_id3.text == 'Select product name'):
            # If any field is not selected, display a popup
            self.show_popup("Please select all fields.")
        else:
            # Show modal view with loading label
            modal_view = ModalView(size_hint=(None, None), size=(300, 100),
                                   background_color=(0, 0, 0, 0))  # Set background color to transparent

            # Create a loading label
            loading_label = Label(text="Loading...", font_size=25)
            modal_view.add_widget(loading_label)
            modal_view.open()

            # Animate the loading label
            Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

            # Perform the actual action (e.g., fetching loan requests)
            # You can replace the sleep with your actual logic
            Clock.schedule_once(lambda dt: self.performance_go_to_newloan_screen1(modal_view), 2)

    def performance_go_to_newloan_screen1(self, modal_view):

        # selected_group = self.ids.group_id1.text
        # selected_category = self.ids.group_id2.text
        # self.selected_category = selected_category
        # self.selected_group = selected_group
        # Get the existing ScreenManager
        # product_name = self.ids.product_id1.text

        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.NewloanScreen1(name='NewloanScreen1'))
        self.manager.current = 'NewloanScreen1'
        # print(self.selected_category)
        # print(product_name)

    def show_popup(self, text):
        content = MDLabel(text=text)
        popup = Popup(title="Warning", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()


class NewloanScreen1(Screen):
    product_name = ""
    product_group = ""
    product_categories = ""
    credit_limit = ""
    product_description = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen')
        product_name = self.root_screen.ids.group_id3.text
        product_group = self.root_screen.ids.group_id1.text
        product_categories = self.root_screen.ids.group_id2.text
        prodcut_description = self.root_screen.ids.product_description.text
        credit_limit = self.root_screen.ids.credit_limit.text

        try:
            # Call the Anvil server function to get the latest credit limit for the specified customer_id
            tenure = app_tables.fin_product_details.search(product_name=product_name)
            max_tenure = tenure[0]['max_tenure']
            min_tenure = tenure[0]['min_tenure']
            max_amount = tenure[0]['max_amount']
            min_amount = tenure[0]['min_amount']
            processing_fee = tenure[0]['processing_fee']
            roi = tenure[0]['roi']
            self.ids.roi.text = str(roi)
            self.ids.processing_fee.text = str(processing_fee)
            # Update the credit_limit MDLabel with the fetched data
            self.ids.max_tenure.text = str(max_tenure)
            self.ids.min_tenure.text = str(min_tenure)
            self.ids.max_amount.text = str(max_amount)
            self.ids.min_amount.text = str(min_amount)
        except anvil._server.AnvilWrappedError as e:
            print(f"Anvil error: {e}")

    def validate_amount(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            amount = float(text)
            text_input.helper_text = ""
            if amount < float(self.ids.min_amount.text):
                text_input.helper_text = f"enter amount more than {self.ids.min_amount.text} "
                text_input.error = True
            elif amount > float(self.ids.max_amount.text):
                text_input.helper_text = f"enter amount less than {self.ids.max_amount.text}"
                text_input.error = True

            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def go_to_lender_dashboard(self):
        self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
        self.manager.current = 'DashboardScreen'

    def reset_fields(self):
        self.ids.text_input1.text = ""
        self.ids.text_input2.text = ""
        self.ids.group_id3.text = "Select EMI Type"

    def validate_tenure(self, text_input, text):
        try:
            if not text:
                text_input.helper_text = ""
                text_input.error = False
                return

            tenure = float(text)
            text_input.helper_text = ""

            if tenure < float(self.ids.min_tenure.text):
                text_input.helper_text = f"enter tenure more than {self.ids.min_tenure.text} "
                text_input.error = True
            elif tenure > float(self.ids.max_tenure.text):
                text_input.helper_text = f"enter tenure less than {self.ids.max_tenure.text}"
                text_input.error = True
            else:
                text_input.error = False

        except ValueError:
            text_input.helper_text = " Please enter a valid number "
            text_input.error = True

        def reset_helper_text(instance_textfield, value):
            instance_textfield.helper_text = ""
            instance_textfield.error = False

        text_input.bind(on_focus=reset_helper_text)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen'

    def current(self):
        self.manager.current = 'NewloanScreen'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_newloan_screen2(self):
        loan_amount = self.ids.text_input1.text.strip()
        loan_tenure = self.ids.text_input2.text.strip()
        emi_type = self.ids.group_id4.text.strip()

        if not loan_amount or not loan_tenure or emi_type == 'Select EMI type':
            # Show a popup indicating that the user needs to provide all necessary information
            self.show_popup("Please enter all fields.")
        else:
            # Show modal view with loading label
            modal_view = ModalView(size_hint=(None, None), size=(300, 100),
                                   background_color=(0, 0, 0, 0))  # Set background color to transparent

            # Create a loading label
            loading_label = Label(text="Loading...", font_size=25)
            modal_view.add_widget(loading_label)
            modal_view.open()

            # Animate the loading label
            Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

            # Perform the actual action (e.g., fetching loan requests)
            # You can replace the sleep with your actual logic
            Clock.schedule_once(lambda dt: self.performance_go_to_newloan_screen2(modal_view), 2)

    def performance_go_to_newloan_screen2(self, modal_view):

        loan_amount = self.ids.text_input1.text
        loan_tenure = self.ids.text_input2.text
        # Get the existing ScreenManager

        self.product_name = self.root_screen.ids.group_id3.text
        self.product_group = self.root_screen.ids.group_id1.text
        self.product_categories = self.root_screen.ids.group_id2.text
        self.product_description = self.root_screen.ids.product_description.text
        self.credit_limit = self.root_screen.ids.credit_limit.text

        # Create a new instance of the LoginScreen
        self.manager.add_widget(Factory.NewloanScreen2(name='NewloanScreen2'))
        self.manager.current = 'NewloanScreen2'

        modal_view.dismiss()

    def show_popup(self, text):
        content = MDLabel(text=text)
        popup = Popup(title="Warning", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def go_to_menu_screen(self):
        loan_amount = self.ids.text_input1.text.strip()
        loan_tenure = self.ids.text_input2.text.strip()
        emi_type = self.ids.group_id4.text.strip()

        if not loan_amount or not loan_tenure or emi_type == 'Select EMI type':
            self.show_popup("Please enter all fields.")
        else:
            interest_rate = float(self.ids.roi.text)  # Accessing IDs directly from NewloanScreen2
            processing_fee = float(self.ids.processing_fee.text)  # Accessing IDs directly from NewloanScreen2

            # Check if MenuScreen already exists in the ScreenManager
            if 'menu' in self.manager.screen_names:
                # If it exists, get a reference to the existing MenuScreen
                menu_screen = self.manager.get_screen('menu')

                # Update the existing MenuScreen with new values
                menu_screen.update_values(loan_amount, loan_tenure, interest_rate, processing_fee, emi_type)
                self.manager.current = 'menu'  # Switch to the existing MenuScreen
            else:
                # If it doesn't exist, create a new MenuScreen and switch to it
                menu_screen = MenuScreen(name='menu', loan_amount=loan_amount, loan_tenure=loan_tenure,
                                         interest_rate=interest_rate, processing_fee=processing_fee,
                                         emi_type=emi_type)
                self.manager.add_widget(menu_screen)
                self.manager.current = 'menu'
class NewloanScreen2(Screen):
    loan_amount = ""
    loan_tenure = ""
    emi_type = ""
    interest_rate = ""
    Processing_fee = ""

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('NewloanScreen1')

        if self.root_screen and self.root_screen.ids:
            loan_amount = float(self.root_screen.ids.text_input1.text)
            self.loan_tenure = float(self.root_screen.ids.text_input2.text)  # Define loan_tenure here
            self.ids.loan_amount.text = "₹" + " " + str(loan_amount)
            interest_rate = float(self.root_screen.ids.roi.text)
            processing_fee = float(self.root_screen.ids.processing_fee.text)
            product_name = self.root_screen.product_name
            product_group = self.root_screen.product_group
            product_categories = self.root_screen.product_categories
            product_description = self.root_screen.product_description
            credit_limit = self.root_screen.credit_limit

            p = loan_amount
            t = self.loan_tenure
            monthly_interest_rate = float(int(interest_rate) / 100) / 12
            emi_denominator = ((1 + monthly_interest_rate) ** t) - 1
            emi_numerator = p * monthly_interest_rate * ((1 + monthly_interest_rate) ** t)
            Monthly_EMI = emi_numerator / emi_denominator

            self.emi_type = self.root_screen.ids.group_id4.text.strip()
            print("Selected emi_type:", self.emi_type)  # Debug print
            # Adjust calculation based on emi_type
            if self.emi_type == 'One Time':
                print("Selected one Month")
                emi = Monthly_EMI * t
            elif self.emi_type == 'Three Months':
                print("Selected Three Months")
                emi = Monthly_EMI * 3
            elif self.emi_type == 'Six Months':
                print("Selected six Months")
                emi = Monthly_EMI * 6
            elif self.emi_type == 'Monthly':
                print("Selected Monthly")
                emi = Monthly_EMI
            else:
                emi = 0  # Default value if emi_type is not recognized
            print("Calculated emi:", emi)  # Debug print
            self.ids.monthly_emi.text = "₹" + " " + str(round(emi, 2))
            interest_amount = Monthly_EMI * t - p
            self.ids.total_interest_amount.text = "₹" + " " + str(round(interest_amount, 2))
            processing_fee_amount = (processing_fee / 100) * p
            self.ids.total_processing_fee_amount.text = "₹" + " " + str(round(processing_fee_amount, 2))
            total_repayment_amount = Monthly_EMI * t + interest_amount + processing_fee_amount
            self.ids.total.text = "₹" + " " + str(round(total_repayment_amount, 2))

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen1'

    def current(self):
        self.manager.current = 'NewloanScreen1'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def send_request(self):
        # Show modal view with loading label
        modal_view = ModalView(size_hint=(None, None), size=(300, 150),
                               background_color=(0, 0, 0, 0))  # Set background color to transparent

        # Create a loading label
        loading_label = Label(text="Loading...", font_size=25)
        modal_view.add_widget(loading_label)
        modal_view.open()

        # Animate the loading label
        Clock.schedule_once(lambda dt: self.animate_loading_text(loading_label, modal_view.height), 0.1)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_send_request(modal_view), 2)

    def generate_loan_id(self):
        # Query the latest loan ID from the data table
        latest_loan = app_tables.fin_loan_details.search(tables.order_by("loan_id", ascending=False))

        if latest_loan and len(latest_loan) > 0:
            # If there are existing loans, increment the last loan ID
            last_loan_id = latest_loan[0]['loan_id']
            counter = int(last_loan_id[2:]) + 1
        else:
            # If there are no existing loans, start the counter at 100001
            counter = 1000001

        # Return the new loan ID
        return f"LA{counter}"

    def performance_send_request(self, modal_view):
        loan_amount_text = self.ids.loan_amount.text
        roi_text = self.root_screen.ids.roi.text
        total_text = self.ids.total.text

        if loan_amount_text and roi_text and total_text:
            # Remove currency symbols and convert to float
            try:
                loan_amount = float(loan_amount_text.replace('₹', '').strip())
                loan_tenure = float(self.root_screen.ids.text_input2.text)
                product_name = self.root_screen.product_name
                product_group = self.root_screen.product_group
                product_categories = self.root_screen.product_categories
                product_description = self.root_screen.product_description
                credit_limit = self.root_screen.credit_limit

                roi = float(roi_text.replace('₹', '').strip())
                processing_fee = float(self.root_screen.ids.processing_fee.text.replace('₹', '').strip())
                total_interest_amount = float(self.ids.total_interest_amount.text.replace('₹', '').strip())
                total_processing_fee_amount = float(self.ids.total_processing_fee_amount.text.replace('₹', '').strip())
                monthly_EMI = float(self.ids.monthly_emi.text.replace('₹', '').strip())
                emi_type = self.root_screen.ids.group_id4.text
                total_repayment = float(total_text.replace('₹', '').strip())
                date_of_apply = datetime.now().date()

                # Call the generate_loan_id function to get the loan ID
                loan_id = self.generate_loan_id()
                email = anvil.server.call('another_method')
                customer = app_tables.fin_user_profile.search(email_user=email)
                customer_id = customer[0]['customer_id']
                borrower_name = customer[0]['full_name']
                print(borrower_name)
                print(customer_id)
                print(email)
                product_id = app_tables.fin_product_details.search(product_name=product_name)
                product_id = product_id[0]['product_id']
                app_tables.fin_loan_details.add_row(
                    loan_id=str(loan_id),
                    borrower_full_name=borrower_name,
                    borrower_email_id=email,
                    borrower_customer_id=customer_id,
                    product_id=str(product_id),
                    loan_amount=float(loan_amount),
                    tenure=float(loan_tenure),
                    loan_updated_status="under process",
                    borrower_loan_created_timestamp=date_of_apply,
                    interest_rate=float(roi),
                    product_name=str(product_name),
                    total_repayment_amount=float(total_repayment),
                    product_description=str(product_description),
                    credit_limit=int(credit_limit),
                    total_processing_fee_amount=float(total_processing_fee_amount),
                    total_interest_amount=float(total_interest_amount),
                    monthly_emi=float(monthly_EMI),
                    emi_payment_type=str(emi_type)
                )
                modal_view.dismiss()
                self.show_success_dialog(f"Request submitted successfully!")
            except ValueError as e:
                modal_view.dismiss()
                print(f"An error occurred: {e}")
        else:
            # Handle the case where some fields are empty
            self.show_popup("Please fill in all fields before submitting.")

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    # Assuming you are in NewloanScreen2 class


class PaymentDetailsScreen(Screen):
    def go_to_menu_screen(self):
        self.manager.add_widget(Factory.MenuScreen(name='menu'))
        self.manager.current = 'menu'


# Register the PaymentDetailsScreen class with the Factory
Factory.register('PaymentDetailsScreen', cls=PaymentDetailsScreen)


class MenuScreen(Screen):

    def __init__(self, loan_amount=0, loan_tenure=0, interest_rate=0, processing_fee=0, emi_type="", **kwargs):
        super().__init__(**kwargs)

        self.loan_amount = float(loan_amount)
        self.loan_tenure = float(loan_tenure)
        self.interest_rate = float(interest_rate)
        self.processing_fee = float(processing_fee)
        self.emi_type = emi_type  # Assign selected EMI type

        if self.emi_type == 'Monthly':
            self.calculate_schedule()
        elif self.emi_type == 'One Time':
            self.calculate_one_time_payment()
        elif self.emi_type == 'Three Months':
            self.calculate_three_months_payment()
        elif self.emi_type == 'Six Months':
            self.calculate_six_months_payment()
        print(self.loan_amount)
        print(self.loan_tenure)
        print(interest_rate)
        print(processing_fee)
        print(self.emi_type)

    def update_values(self, loan_amount, loan_tenure, interest_rate, processing_fee, emi_type):
        self.loan_amount = float(loan_amount)
        self.loan_tenure = float(loan_tenure)
        self.interest_rate = float(interest_rate)
        self.processing_fee = float(processing_fee)
        self.emi_type = emi_type

        if self.emi_type == 'Monthly':
            self.calculate_schedule()
        elif self.emi_type == 'One Time':
            self.calculate_one_time_payment()
        elif self.emi_type == 'Three Months':
            self.calculate_three_months_payment()
        elif self.emi_type == 'Six Months':
            self.calculate_six_months_payment()
    def calculate_schedule(self):
        print("Calculating payment schedule...")
        container = self.ids.container
        container.clear_widgets()

        # Calculate total interest and processing fee based on provided rates and loan tenure
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee_amount = (self.processing_fee / 100) * self.loan_amount

        print("Monthly Interest Rate:", monthly_interest_rate)
        print("Total Processing Fee Amount:", total_processing_fee_amount)

        # Check if loan tenure is zero or monthly interest rate is zero
        if self.loan_tenure == 0 or monthly_interest_rate == 0:
            print("Error: Loan tenure or monthly interest rate is zero.")
            # Handle error condition here (e.g., display an error message)
            return

        # Calculate EMI
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            print("Error: Denominator for EMI calculation is zero.")
            # Handle error condition here (e.g., display an error message)
            return

        monthly_emi = emi_numerator / emi_denominator
        total_interest_amount = monthly_emi * self.loan_tenure - self.loan_amount

        print("Monthly EMI:", monthly_emi)
        print("Total Interest Amount:", total_interest_amount)

        # Initialize beginning balance
        loan_amount_beginning_balance = self.loan_amount
        beginning_balance = monthly_emi * self.loan_tenure + total_interest_amount + total_processing_fee_amount

        # Create and add payment items to the schedule
        for month in range(1, int(self.loan_tenure) + 1):
            # Calculate total payment for the month
            monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
            monthly_processing_fee = (self.processing_fee / 100) * self.loan_amount / self.loan_tenure
            total_payment = monthly_emi + monthly_interest + monthly_processing_fee

            # Calculate principal for the month
            principal = monthly_emi - monthly_interest

            # Calculate ending balance for subsequent months
            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal)

            # Print statements for each month
            print(f"Month: {month}")
            print("Monthly Interest:", monthly_interest)
            print("Monthly Processing Fee:", monthly_processing_fee)
            print("Principal:", principal)
            print("Total Payment:", total_payment)
            print("Ending Balance:", ending_balance)
            print("loan amount Ending Balance:", loan_amount_ending_balance)
            print("Beginning Balance:", beginning_balance)
            print("loan amountBeginning Balance:", loan_amount_beginning_balance)

            # Create and add payment item
            payment_str = f"Payment Schedule {month}"
            print("Adding payment item:", payment_str)
            item = PaymentItem(payment_str=payment_str, loan_amount=self.loan_amount, emi_amount=monthly_emi,
                               interest_amount=monthly_interest, processing_fee_amount=monthly_processing_fee,
                               total_payment=total_payment, balance_amount=ending_balance, principal=principal,
                               beginning_balance=beginning_balance)
            container.add_widget(item)

            # Update beginning balance for the next month
            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

        print("Payment schedule calculation complete.")

    def calculate_one_time_payment(self):
        print("Calculating one-time payment...")
        container = self.ids.container
        container.clear_widgets()

        # Calculate total interest and processing fee based on provided rates and loan tenure
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee_amount = (self.processing_fee / 100) * self.loan_amount

        # Calculate EMI
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            print("Error: Denominator for EMI calculation is zero.")
            # Handle error condition here (e.g., display an error message)
            return

        monthly_emi = emi_numerator / emi_denominator

        total_interest_amount = monthly_emi * self.loan_tenure - self.loan_amount
        total_payment = monthly_emi + total_interest_amount + total_processing_fee_amount
        beginning_balance = monthly_emi * self.loan_tenure + total_interest_amount + total_processing_fee_amount

        # Print one-time payment details
        print("One-Time Payment:")
        print("Monthly EMI:", monthly_emi)
        print("Total Interest Amount:", total_interest_amount)
        print("Total payment:", total_payment)
        print("Total processing Amount:", total_processing_fee_amount)

        # Create and add one-time payment item
        item = PaymentItem(payment_str="Payment Schedule 1", loan_amount=self.loan_amount, emi_amount=beginning_balance,
                           interest_amount=total_interest_amount, processing_fee_amount=total_processing_fee_amount,
                           total_payment=beginning_balance,
                           balance_amount=0, principal=self.loan_amount,
                           beginning_balance=beginning_balance)
        container.add_widget(item)
        print("One-time payment added.")

    def calculate_three_months_payment(self):
        print("Calculating payment for every three months...")
        container = self.ids.container
        container.clear_widgets()

        # Calculate total interest and processing fee based on provided rates and loan tenure
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee_amount = (self.processing_fee / 100) * self.loan_amount

        # Calculate EMI
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            print("Error: Denominator for EMI calculation is zero.")
            # Handle error condition here (e.g., display an error message)
            return

        monthly_emi = emi_numerator / emi_denominator

        total_interest_amount = monthly_emi * self.loan_tenure - self.loan_amount

        # Calculate number of three-month periods
        num_periods = int(self.loan_tenure / 3)

        # Initialize loan amount beginning balance
        loan_amount_beginning_balance = self.loan_amount
        beginning_balance = monthly_emi * self.loan_tenure + total_interest_amount + total_processing_fee_amount
        for period in range(1, num_periods + 1):
            # Calculate payments for this three-month period
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(1, 4):  # Calculate for each month in the three-month period
                # Calculate total payment for the month
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                monthly_processing_fee = (self.processing_fee / 100) * self.loan_amount / self.loan_tenure

                # Calculate principal for the month
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += monthly_processing_fee
                total_payment = monthly_emi * 3 + interest_sum + processing_fee_sum
            # Calculate ending balance for this three-month period
            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            # Create and add payment item for the three-month period
            payment_str = f"Payment Schedule {period}"
            item = PaymentItem(payment_str=payment_str, loan_amount=self.loan_amount,
                               emi_amount=monthly_emi * 3, interest_amount=interest_sum,
                               processing_fee_amount=processing_fee_sum, total_payment=total_payment,
                               balance_amount=ending_balance, principal=principal_sum,
                               beginning_balance=beginning_balance)
            container.add_widget(item)

            # Update loan amount beginning balance for the next three-month period
            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

        # Calculate remaining months
        remaining_months = int(self.loan_tenure - (num_periods * 3))
        if remaining_months > 0:
            # Calculate payments for remaining months
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(1, remaining_months + 1):
                # Calculate total payment for the month
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                monthly_processing_fee = (self.processing_fee / 100) * self.loan_amount / self.loan_tenure
                # total_payment = monthly_emi + monthly_interest + monthly_processing_fee

                # Calculate principal for the month
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += monthly_processing_fee
                total_payment = monthly_emi * remaining_months + interest_sum + processing_fee_sum

            # Calculate ending balance for the remaining months
            ending_balance = max(0, beginning_balance - total_payment)

            # Create and add payment item for the remaining months
            payment_str = f"Payment Schedule {num_periods + 1}"
            item = PaymentItem(payment_str=payment_str, loan_amount=self.loan_amount,
                               emi_amount=monthly_emi * remaining_months, interest_amount=interest_sum,
                               processing_fee_amount=processing_fee_sum, total_payment=total_payment,
                               balance_amount=ending_balance, principal=principal_sum,
                               beginning_balance=beginning_balance)
            container.add_widget(item)

        print("Payment calculation complete.")

    def calculate_six_months_payment(self):
        print("Calculating payment for every three months...")
        container = self.ids.container
        container.clear_widgets()

        # Calculate total interest and processing fee based on provided rates and loan tenure
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_processing_fee_amount = (self.processing_fee / 100) * self.loan_amount

        # Calculate EMI
        emi_numerator = self.loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** self.loan_tenure)
        emi_denominator = ((1 + monthly_interest_rate) ** self.loan_tenure) - 1

        if emi_denominator == 0:
            print("Error: Denominator for EMI calculation is zero.")
            # Handle error condition here (e.g., display an error message)
            return

        monthly_emi = emi_numerator / emi_denominator

        total_interest_amount = monthly_emi * self.loan_tenure - self.loan_amount

        # Calculate number of three-month periods
        num_periods = int(self.loan_tenure / 6)

        # Initialize loan amount beginning balance
        loan_amount_beginning_balance = self.loan_amount
        beginning_balance = monthly_emi * self.loan_tenure + total_interest_amount + total_processing_fee_amount
        for period in range(1, num_periods + 1):
            # Calculate payments for this three-month period
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(1, 7):  # Calculate for each month in the three-month period
                # Calculate total payment for the month
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                monthly_processing_fee = (self.processing_fee / 100) * self.loan_amount / self.loan_tenure

                # Calculate principal for the month
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += monthly_processing_fee
                total_payment = monthly_emi * 6 + interest_sum + processing_fee_sum
            # Calculate ending balance for this three-month period
            ending_balance = max(0, beginning_balance - total_payment)
            loan_amount_ending_balance = max(0, loan_amount_beginning_balance - principal_sum)

            # Create and add payment item for the three-month period
            payment_str = f"Payment Schedule {period}"
            item = PaymentItem(payment_str=payment_str, loan_amount=self.loan_amount,
                               emi_amount=monthly_emi * 6, interest_amount=interest_sum,
                               processing_fee_amount=processing_fee_sum, total_payment=total_payment,
                               balance_amount=ending_balance, principal=principal_sum,
                               beginning_balance=beginning_balance)
            container.add_widget(item)

            # Update loan amount beginning balance for the next three-month period
            beginning_balance = ending_balance
            loan_amount_beginning_balance = loan_amount_ending_balance

        # Calculate remaining months
        remaining_months = int(self.loan_tenure - (num_periods * 3))
        if remaining_months > 0:
            # Calculate payments for remaining months
            principal_sum = 0
            interest_sum = 0
            processing_fee_sum = 0

            for month in range(1, remaining_months + 1):
                # Calculate total payment for the month
                monthly_interest = loan_amount_beginning_balance * monthly_interest_rate
                monthly_processing_fee = (self.processing_fee / 100) * self.loan_amount / self.loan_tenure
                # total_payment = monthly_emi + monthly_interest + monthly_processing_fee

                # Calculate principal for the month
                principal = monthly_emi - monthly_interest

                principal_sum += principal
                interest_sum += monthly_interest
                processing_fee_sum += monthly_processing_fee
                total_payment = monthly_emi * remaining_months + interest_sum + processing_fee_sum

            # Calculate ending balance for the remaining months
            ending_balance = max(0, beginning_balance - total_payment)

            # Create and add payment item for the remaining months
            payment_str = f"Payment Schedule {num_periods + 1}"
            item = PaymentItem(payment_str=payment_str, loan_amount=self.loan_amount,
                               emi_amount=monthly_emi * remaining_months, interest_amount=interest_sum,
                               processing_fee_amount=processing_fee_sum, total_payment=total_payment,
                               balance_amount=ending_balance, principal=principal_sum,
                               beginning_balance=beginning_balance)
            container.add_widget(item)

        print("Payment calculation complete.")

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'NewloanScreen1'


# Define the PaymentItem class
class PaymentItem(OneLineListItem):
    def __init__(self, payment_str='', loan_amount=0, emi_amount=0, interest_amount=0,
                 processing_fee_amount=0, total_payment=0, balance_amount=0, principal=0, beginning_balance=0,
                 **kwargs):
        super().__init__(**kwargs)
        self.text = payment_str
        self.loan_amount = loan_amount
        self.emi_amount = emi_amount
        self.interest_amount = interest_amount
        self.processing_fee_amount = processing_fee_amount
        self.total_payment = total_payment
        self.balance_amount = balance_amount
        self.principal = principal
        self.beginning_balance = beginning_balance
        self.bind(on_release=self.on_item_click)

    def on_item_click(self, *args):
        app = App.get_running_app()
        screen_manager = app.root

        # Check if the PaymentDetailsScreen already exists in the ScreenManager
        if 'payment_details' in screen_manager.screen_names:
            # If it exists, get the reference to the existing screen
            payment_details_screen = screen_manager.get_screen('payment_details')
        else:
            # If it doesn't exist, create a new PaymentDetailsScreen
            payment_details_screen = PaymentDetailsScreen(name='payment_details')
            # Add the PaymentDetailsScreen to the ScreenManager
            screen_manager.add_widget(payment_details_screen)

        # Update the labels with the corresponding values
        # payment_details_screen.ids.loan_label.text = f" Rs. {self.loan_amount:.2f}"
        payment_details_screen.ids.emi_label.text = f"Rs. {self.emi_amount:.2f}"
        payment_details_screen.ids.interest_label.text = f" Rs. {self.interest_amount:.2f}"
        payment_details_screen.ids.processing_fee_label.text = f" Rs. {self.processing_fee_amount:.2f}"
        payment_details_screen.ids.total_payment_label.text = f" Rs. {self.total_payment:.2f}"
        payment_details_screen.ids.balance_label.text = f" Rs. {self.balance_amount:.2f}"
        payment_details_screen.ids.principal_label.text = f" Rs. {self.principal:.2f}"
        payment_details_screen.ids.beginning_balance_label.text = f" Rs. {self.beginning_balance:.2f}"

        # Switch to the PaymentDetailsScreen
        screen_manager.current = 'payment_details'


class MyScreenManager(ScreenManager):
    pass
