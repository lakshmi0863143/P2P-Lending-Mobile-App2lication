import anvil

from kivy.core.window import Window
from kivy.properties import ListProperty, Clock
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
    BorrowerDuesScreen:

<BorrowerDuesScreen>:
    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2

        spacing: dp(20)
        orientation: 'vertical'

        MDTopAppBar:
            title:"Today's Dues"
            md_bg_color:0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 # Set color to white
            size_hint:1,dp(7)
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back(),(1,1,1,1)]]
            right_action_items: [['wallet', (0.043, 0.145, 0.278, 1)]]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}

        MDFloatLayout:
            pos_hint:{'center_x':0.5,'center_y':0.5}
            MDLabel:
                text:"#today's dues"
                id:dues
                theme_text_color: "Custom"  # Set the text color theme to custom
                text_color:1,1,1,1
                halign:"center"
                pos_hint:{'center_x':0.5,'center_y':7.5}
            MDGridLayout:
                cols: 2
                spacing:dp(10)

                size_hint_y: None
                pos_hint: {'center_x': 0.5, 'center_y':4.2}

                width: self.minimum_width
                size_hint_x: None
                MDRectangleFlatButton:
                    size_hint: None, None
                    size: "140dp", "40dp"

                    md_bg_color:0.043, 0.145, 0.278, 1
                    line_color:1,1,1,1
                    size_hint_y: None
                    height: dp(60)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Remaining Balance   "
                            font_size:dp(14)
                            bold:True
                            id:remaining_balance
                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDRectangleFlatButton:
                    size_hint: None, None
                    size: "150dp", "40dp"

                    md_bg_color: 0.043, 0.145, 0.278, 1
                    line_color:1,1,1,1
                    size_hint_y: None
                    height: dp(60)
                    size_hint_x: None
                    width: dp(130)
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing:dp(10)
                        MDLabel:
                            text: "Remaining Tenure"
                            font_size:dp(14)
                            bold:True
                            id:remaining_tenure
                            theme_text_color: 'Custom'
                            halign: "center"
                            text_color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}





        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Payment due date"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Payment due date"
                    id:payment_due_date
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1


        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Beginning balance"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"Beginning balance"
                    id: beginning_balance
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Scheduled payment"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Scheduled payment"
                    id: scheduled_payment
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Extra payment"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Extra payment"
                    id: extra_payment
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Principal"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Principal"
                    id:principal
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Interest"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Interest"
                    id:interest
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Processing fee"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Processing_fee"
                    id: processing_fee
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1


        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Ending balance"
                    font_size:dp(16)
                    bold:True

                MDLabel:
                    text:"#Ending balance"
                    id:ending_balance
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1


        MDGridLayout:
            cols: 2
            padding: dp(20)
            BoxLayout:
                orientation:"horizontal"
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                padding: dp(20)
                spacing: dp(20)

                MDLabel:
                    text: "Total payment"
                    font_size:dp(17)
                    bold:True

                MDLabel:
                    text:"#Total payment"
                    id:total
                    size_hint_x: 0.91



                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                    size_hint: None, None
                    size: "180dp", "45dp"
                    background_color: 1, 1, 1, 0 
                    color: 0, 0, 0, 1
                    line_color_normal: 0, 0, 0, 1  # Set the line color to black
                    color: 0, 0, 0, 1


        MDLabel:
            text: " "             
        MDFloatLayout:
            MDRaisedButton:
                text: "Pay Now"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release: root.go_to_newloan_screen1()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)
"""
Builder.load_string(user_helpers2)


class BorrowerDuesScreen(Screen):
    def on_pre_enter(self, *args):
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
        self.manager.current = 'DashboardScreen'

    def current(self):
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass
