from anvil.tables import app_tables
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.uix.snackbar import Snackbar
from kivy.factory import Factory

import anvil

Builder.load_string(
    """
<WindowManager>:
    WalletScreen:


<WalletScreen>:
    MDTopAppBar:
        title: "GP2P-Wallet"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left',lambda x: root.go_back()]]
        right_action_items: [['refresh', lambda x: root.refresh()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)
        MDLabel:
            text: ""
            size_hint_y: None
            height: dp(20)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.5  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

            MDLabel:
                text: 'Available Balance'
                halign: 'left'
                bold: True
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: None, None
                width: "190dp"
                height: "10dp"
                pos_hint: {'center_x': 0.3, 'center_y': 0.2}

                MDIcon:
                    icon: 'currency-inr'
                    halign: 'left'
                    bold: True
                MDLabel:
                    id: total_amount
                    halign: 'left'
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            points: [self.x, self.y - dp(5), self.x + self.width, self.y - dp(5)]

        MDFloatLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black in this example)
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            GridLayout:
                id: grid1
                cols: 2
                spacing: dp(20)
                padding: dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 0.95}
                size_hint: 1, None
                height: "10dp"
                MDRoundFlatButton:
                    text: "Deposit"
                    id: deposit_button_grid
                    md_bg_color: 253/255, 254/255, 254/255, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.highlight_button('deposit')
                MDRoundFlatButton:
                    text: "Withdraw"
                    id: withdraw_button_grid
                    md_bg_color: 253/255, 254/255, 254/255, 1
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.highlight_button('withdraw')

            MDBoxLayout:
                id: box1
                orientation: 'horizontal'
                size_hint: None, None
                width: "250dp"
                height: "60dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}

                MDLabel:
                    text: 'Enter Amount'
                    halign: 'left'
                    bold: True 

                MDTextField:
                    id: enter_amount      
                    helper_text_mode: "on_focus"
                    icon_left: 'currency-inr'
                    font_name: "Roboto-Bold"  

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            GridLayout:
                id: grid2
                cols: 2
                spacing: dp(5)
                padding: dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: 1, None
                height: "5dp"
                MDLabel:
                    text: 'View Transaction History'
                    halign: 'left'
                    bold: True
                MDIcon:
                    icon: 'chevron-right'
                    halign: 'right'
                    bold: True

        MDRoundFlatButton:
            text: "Submit"
            md_bg_color: 0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            font_name: "Roboto-Bold" 
            text_color: 1, 1, 1, 1
            size_hint: 0.7, None
            height: "40dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.submit()

    """
)


class WalletScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None
        data = app_tables.fin_wallet.search()
        email = self.email()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        if email in w_email:
            index = w_email.index(email)
            self.ids.total_amount.text = str(w_amount[index])
        else:
            print("no email found")

    def highlight_button(self, button_type):
        if button_type == 'deposit':
            self.ids.deposit_button_grid.md_bg_color = 0.043, 0.145, 0.278, 1
            self.ids.withdraw_button_grid.md_bg_color = 253 / 255, 254 / 255, 254 / 255, 1
            self.ids.deposit_button_grid.text_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.text_color = 0, 0, 0, 1
            self.type = 'deposit'
        elif button_type == 'withdraw':
            self.ids.deposit_button_grid.md_bg_color = 253 / 255, 254 / 255, 254 / 255, 1
            self.ids.withdraw_button_grid.md_bg_color = 0.043, 0.145, 0.278, 1
            self.ids.withdraw_button_grid.text_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 0, 0, 0, 1
            self.type = 'withdraw'

    def go_back(self):
        from borrower_dashboard import DashboardScreen  # Import the correct screen class
        dashboard_screen = DashboardScreen(name='DashboardScreen')  # Create an instance of the screen
        self.manager.add_widget(dashboard_screen)  # Add the screen to the ScreenManager
        self.manager.current = 'DashboardScreen'  # Switch to the added screen

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def submit(self):
        if self.type == 'deposit':
            data = app_tables.fin_wallet.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])

            if email in w_email:
                index = w_email.index(email)
                data[index]['wallet_amount'] = int(self.ids.enter_amount.text) + w_amount[index]
                self.show_snackbar(f'Amount {self.ids.enter_amount.text} Deposited to the this wallet ID {w_id[index]}')
                self.ids.enter_amount.text = ''
            else:
                print("no email found")

        elif self.type == 'withdraw':
            data = app_tables.fin_wallet.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])

            if email in w_email:
                index = w_email.index(email)
                if w_amount[index] > int(self.ids.enter_amount.text):
                    data[index]['wallet_amount'] = w_amount[index] - int(self.ids.enter_amount.text)
                    self.show_snackbar(
                        f'Amount {self.ids.enter_amount.text} Withdraw from this wallet ID {w_id[index]}')
                    self.ids.enter_amount.text = ''
                else:
                    self.show_snackbar(
                        f'Insufficient Amount {self.ids.enter_amount.text} Please Deposit Required Money')
                    self.ids.enter_amount.text = ''
            else:
                print("no email found")

    def refresh(self):
        self.__init__()

    def email(self):
        return anvil.server.call('another_method')

    def wallet(self):
        return anvil.server.call('wallet_data')


class MyScreenManager(ScreenManager):
    pass
