from datetime import datetime

from anvil.tables import app_tables
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import anvil
from kivymd.uix.dialog import MDDialog

Builder.load_string(
    """
<WindowManager>:
    LenderWalletScreen:


<LenderWalletScreen>:
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
            id: box
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


class LenderWalletScreen(Screen):
    def __init__(self, loan_amount_text=None, **kwargs):
        super().__init__(**kwargs)
        self.type = None
        self.loan_amount = loan_amount_text
        print(self.loan_amount)  # Print the loan amount received during initialization
        data = app_tables.fin_wallet.search()
        email = self.email()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if email in w_email:
            index = w_email.index(email)
            self.ids.total_amount.text = str(w_amount[index])
        else:
            print("no email found")

        if loan_amount_text is not None and w_amount[index] >= loan_amount_text:
            button = MDRoundFlatButton(
                text="Loan Disbursement",
                size_hint_y=None,
                height=30,
                font_size=14,
                theme_text_color='Custom',
                text_color=(1, 1, 1, 1),
                font_name="Roboto-Bold",
                md_bg_color= (0.043, 0.145, 0.278, 1)
            )
            button.bind(on_release=self.disbrsed_loan)
            self.ids.box.add_widget(button)
        elif loan_amount_text != None and w_amount[index] < loan_amount_text:
            print("Amount Not Sufficient")

    def disbrsed_loan(self, instance):
        print("amount paid")
        self.manager.get_screen('ViewLoansProfileScreenLR').paynow()


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
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

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
        self.refresh()
        self.manager.current = 'LenderWalletScreen'

    def submit(self):
        enter_amount = self.ids.enter_amount.text
        if self.type == None:
            self.show_success_dialog('Please Select Transaction Type')
        elif self.ids.enter_amount.text == '' and not self.ids.enter_amount.text.isdigit():
            self.show_success_dialog('Enter Valid Amount')
        elif self.type == 'deposit':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()
            if email in w_email:
                index = w_email.index(email)
                data[index]['wallet_amount'] = int(enter_amount) + w_amount[index]
                self.show_success_dialog(f'Amount {enter_amount} Deposited to the this wallet ID {w_id[index]}')
                self.ids.enter_amount.text = ''
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id, customer_id=w_customer_id[index], user_email=email,
                                                           transaction_type=self.type, amount=int(enter_amount), status='success', wallet_id=w_id[index],
                                                           transaction_time_stamp=transaction_date_time)
            else:
                print("no email found")

        elif self.type == 'withdraw':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()

            if email in w_email:
                index = w_email.index(email)
                if w_amount[index] >= int(self.ids.enter_amount.text):
                    data[index]['wallet_amount'] = w_amount[index] - int(self.ids.enter_amount.text)
                    self.show_success_dialog(
                        f'Amount {self.ids.enter_amount.text} Withdraw from this wallet ID {w_id[index]}')
                    self.ids.enter_amount.text = ''
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='success', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                else:
                    self.show_success_dialog(
                        f'Insufficient Amount {self.ids.enter_amount.text} Please Deposit Required Money')
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='fail', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                    self.ids.enter_amount.text = ''
            else:
                print("no email found")

    def refresh(self):
        current_loan_amount = anvil.server.call('loan_amount_text')
        self.__init__(loan_amount_text=current_loan_amount)

    def email(self):
        return anvil.server.call('another_method')


class MyScreenManager(ScreenManager):
    pass
