import anvil
from anvil.tables import app_tables
from kivy import properties

from kivy.core.window import Window
from kivy.properties import ListProperty, Clock
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget, TwoLineAvatarIconListItem
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime, timezone, timedelta, date

from kivymd.uix.spinner import MDSpinner
import anvil.tables.query as q
from borrower_wallet import WalletScreen

user_helpers2 = """
<WindowManager>:
    BorrowerDuesScreen:
    DuesScreen:
    LastScreenWallet:
<DuesScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:"Today's Dues"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container 


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
            size_hint:1,None
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['wallet']]
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}

        MDLabel:
            text: "" 
            size_hint_y:None
            height:dp(1) 

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Loan ID"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: loan
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1


        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Loan Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: loan_amount1
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Tenure"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: tenure
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Interest Rate"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: interest_rate
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Account Number"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:account_number
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                text: "Emi Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:emi_amount
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1 
                color: 0, 0, 0, 1

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                id: extra
                text: "Extra Payment"
                font_size:dp(16)
                bold:True

            MDLabel:
                id: extra_amount
                background_color: 1, 1, 1, 0 
                color: 0, 0, 0, 1
                line_color_normal: 0, 0, 0, 1  # Set the line color to black
                color: 0, 0, 0, 1           

        MDGridLayout:
            cols: 2
            padding: dp(20)
            MDLabel:
                id: total
                text: "Total Amount"
                font_size:dp(16)
                bold:True

            MDLabel:
                id:total_amount
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
                on_release: root.go_to_paynow()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint:0.4, None  
                font_name:"Roboto-Bold"
                font_size:dp(15)
                               
<LastScreenWallet>:
    MDTopAppBar:
        title: "Today Due Request Submitted"
        elevation: 2
        pos_hint: {'top': 1}
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        Image:
            source: "checkmark.png"
            size_hint: None, None
            size: "70dp", "70dp"
            pos_hint: {'center_x': 0.5}

        MDLabel:
            text: "Thank You"
            font_style: 'H4'
            bold: True
            halign: 'center'

        MDLabel:
            text: "Your Today Due application has been requested and you will be notified once it is approved."
            font_style: 'Body1'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        MDRaisedButton:
            text: "Go Back Home"
            on_press: root.go_back_home()
            md_bg_color: 0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {'center_x': 0.5}
            font_name: "Roboto-Bold"
        MDLabel:
            text: " "             
            
"""
Builder.load_string(user_helpers2)


class BorrowerDuesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, shechule_date):
        print(value)
        self.loan_id = value
        today_date = datetime.now(timezone.utc).date()
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])

        product = app_tables.fin_product_details.search()
        product_id = []
        lapsed_fee = []
        default_fee = []
        npa = []
        for i in product:
            product_id.append(i['product_id'])
            lapsed_fee.append(i['lapsed_fee'])
            default_fee.append(i['default_fee'])
            npa.append(i['npa'])
        data1 = app_tables.fin_loan_details.search()
        user_profile = app_tables.fin_user_profile.search()

        loan_id = []
        cos_id1 = []
        loan_amount = []
        loan_status = []
        tenure = []
        interest = []
        monthly_emi = []
        emi_pay_type = []
        total_int_amount = []
        total_pro_fee_amount = []
        total_repay = []
        shedule_payment = []
        loan_product = []
        for i in data1:
            loan_id.append(i['loan_id'])
            cos_id1.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            monthly_emi.append(i['monthly_emi'])
            emi_pay_type.append(i['emi_payment_type'])
            total_int_amount.append(i['total_interest_amount'])
            total_pro_fee_amount.append(i['total_processing_fee_amount'])
            total_repay.append(i['total_repayment_amount'])
            shedule_payment.append(i['first_emi_payment_due_date'])
            loan_product.append(i['product_id'])
        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan.text = str(loan_id[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        pro_fee = total_pro_fee_amount[index] / tenure[index]
        monthly_interest = interest[index] / 12 / 100
        total_pay = tenure[index] * 12

        cos_id = []
        account_num = []
        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])

        if cos_id1[index] in cos_id:
            index1 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

        extend_row = None
        extend_amount = 0
        foreclose_amount1 = 0
        emi_amount1 = 0
        new_emi_amount = 0

        if loan_status[index] == "disbursed":
            extra_amount = 0
            print(loan_status[index])
            print(extra_amount)
            if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 8:
                product_index = product_id.index(loan_product[index])
                lapsed = lapsed_fee[product_index]
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment (Lapsed)"
                self.ids.extra_amount.text = str(extra_amount+ lapsed)
                self.ids.total_amount.text = str(total_amount)
                data1[index]['loan_state_status'] = "lapsed"

            elif (today_date - shechule_date[value]).days >= 8 and (today_date - shechule_date[value]).days < 98:
                product_index = product_id.index(loan_product[index])
                default = default_fee[product_index]
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment(Default)"
                self.ids.extra_amount.text = str(extra_amount + default)
                self.ids.total_amount.text = str(total_amount)
                data1[index]['loan_state_status'] = 'default'
            elif (today_date - shechule_date[value]).days >= 98:
                product_index = product_id.index(loan_product[index])
                npa = npa[product_index]
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment(NPA)"
                self.ids.extra_amount.text = str(extra_amount + npa)
                self.ids.total_amount.text = str(total_amount)
                data1[index]['loan_state_status'] = 'npa'

            else:
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra_amount.text = str(extra_amount)
                self.ids.total_amount.text = str(total_amount)
                self.ids.extra.text = "Extra Payment "


        elif loan_status[index] == "extension":
            emi_num = 0
            emi_data = app_tables.fin_emi_table.search(loan_id=str(value))
            if emi_data:
                emi = emi_data[0]
                emi_number = emi['emi_number']
            print(loan_status[index])
            extend_row = app_tables.fin_extends_loan.get(
                loan_id=str(value),
                emi_number=emi_number
            )
            if extend_row is not None and extend_row['status'] == "approved":
                extend_amount += extend_row['extension_amount']
                new_emi_amount += extend_row['new_emi']
                total_amount = new_emi_amount + extend_amount
                print(new_emi_amount, extend_amount)
                print(extend_amount)
                next_emi_num = emi_number + 1
                next_emi = app_tables.fin_emi_table.get(loan_id=str(value), emi_number=next_emi_num)

                if next_emi is not None:
                    next_payment_amount = next_emi['payment_amount']
                    extend_amount += next_payment_amount
                if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 8:
                    product_index = product_id.index(loan_product[index])
                    lapsed = lapsed_fee[product_index]
                    self.ids.extra_amount.text = str(extend_amount + lapsed)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount )
                    self.ids.extra.text = "Extra Payment (Lapsed)"
                    data1[index]['loan_state_status'] = "lapsed"
                elif (today_date - shechule_date[value]).days >= 8 and (today_date - shechule_date[value]).days < 98:
                    product_index = product_id.index(loan_product[index])
                    default = default_fee[product_index]
                    self.ids.extra_amount.text = str(extend_amount + default)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount )
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = "default"
                elif (today_date - shechule_date[value]).days >= 98:
                    product_index = product_id.index(loan_product[index])
                    npa = npa[product_index]
                    self.ids.extra_amount.text = str(extend_amount + npa)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount)
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = 'npa'
                else:
                    self.ids.extra_amount.text = str(extend_amount)
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(total_amount)
                    self.ids.extra.text = "Extra Payment"
                print(extend_amount, new_emi_amount, total_amount)

        elif loan_status[index] == "foreclosure":
            print(loan_status[index])
            foreclosure_row = app_tables.fin_foreclosure.get(
                loan_id=str(value)
            )
            if foreclosure_row is not None and foreclosure_row['status'] == 'approved':
                foreclose_amount1 += foreclosure_row['foreclose_amount']
                emi_amount1 += foreclosure_row['total_due_amount']
                total_amount = foreclose_amount1 + emi_amount1
                print(foreclose_amount1, emi_amount1)
                print(emi_amount1)
                print(foreclose_amount1)
                if (today_date - shechule_date[value]).days >= 6 and (today_date - shechule_date[value]).days < 8:
                    product_index = product_id.index(loan_product[index])
                    lapsed = lapsed_fee[product_index]
                    self.ids.extra_amount.text = str(foreclose_amount1+ lapsed)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount )
                    self.ids.total.text = "Total Amount (Lapsed)"
                    data1[index]['loan_state_status'] = "lapsed"
                    data1[index]['loan_updated_status'] = "closed"
                    emi_data[index]['next_payment'] = None

                elif (today_date - shechule_date[value]).days >= 8 and (today_date - shechule_date[value]).days < 98:
                    product_index = product_id.index(loan_product[index])
                    default = default_fee[product_index]
                    self.ids.extra_amount.text = str(foreclose_amount1+ default)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount )
                    self.ids.total.text = "Total Amount (Default)"
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                elif (today_date - shechule_date[value]).days >= 98:
                    product_index = product_id.index(loan_product[index])
                    npa = npa[product_index]
                    self.ids.extra_amount.text = str(foreclose_amount1 + npa)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount )
                    self.ids.extra.text = "Extra Payment (Default)"
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"


                else:
                    self.ids.extra.text = "Extra Payment"
                    self.ids.extra_amount.text = str(foreclose_amount1)
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(total_amount)
                    data1[index]['loan_updated_status'] = "closed"

    date = datetime.today()

    def go_to_paynow(self):
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
        value = self.loan_id
        data1 = app_tables.fin_loan_details.search()
        wallet = app_tables.fin_wallet.search()
        total = self.ids.total_amount.text
        extra_amount = self.ids.extra_amount.text
        user_profile = app_tables.fin_user_profile.search()
        tenure = self.ids.tenure.text
        loan = self.ids.loan.text

        emi_number = 0

        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            emi_number = emi_num[last_index] + 1

        schedule_date = []
        loan_id = []
        cos_id1 = []
        emi_type_pay = []
        lender_customer_id = []
        borrower_email =[]
        lender_email = []
        for i in data1:
            loan_id.append(i['loan_id'])
            cos_id1.append(i['borrower_customer_id'])
            schedule_date.append(i['first_emi_payment_due_date'])
            emi_type_pay.append(i['emi_payment_type'])
            lender_customer_id.append(i['lender_customer_id'])
            borrower_email.append(i['borrower_email_id'])
            lender_email.append(i['lender_email_id'])

        cos_id = []
        account_num = []

        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index = 0
        if cos_id1[index] in cos_id:
            index1 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

        wallet_customer_id = []
        wallet_amount = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])

        lender_customer_id = []
        loan_id_list = []
        for i in data1:
            loan_id_list.append(i['loan_id'])
            lender_customer_id.append(i['lender_customer_id'])

        index = 0
        if value in loan_id:
            index = loan_id.index(value)

        next_payment_date = None
        b_index = -1
        l_index = -1

        index1 = 0
        if lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id:
            b_index = wallet_customer_id.index(int(cos_id1[index]))
            l_index = wallet_customer_id.index(lender_customer_id[index])
        print(b_index, l_index)
        print(value)
        print(wallet_amount[b_index], float(total))
        print(wallet_amount[b_index] >= float(total))
        if wallet_amount[b_index] >= float(total):
            wallet[b_index]['wallet_amount'] -= float(total)
            wallet[l_index]['wallet_amount'] += float(total)


            if emi_type_pay[index] == 'Monthly':
                next_payment_date = schedule_date[index] + timedelta(days=30)
                print(schedule_date[index])
            elif emi_type_pay[index] == 'Three Months':
                next_payment_date = schedule_date[index] + timedelta(days=90)
            elif emi_type_pay[index] == 'Six Months':
                next_payment_date = schedule_date[index] + timedelta(days=180)
            elif emi_type_pay[index] == 'One Time':
                if tenure:
                    next_payment_date = schedule_date[index] + timedelta(days=30 * int(tenure))
            app_tables.fin_emi_table.add_row(
                loan_id=str(loan),
                extra_fee=float(extra_amount),
                amount_paid=float(total),
                scheduled_payment_made=datetime.today(),
                scheduled_payment=schedule_date[index],
                next_payment=next_payment_date,
                account_number=account_num[index1],
                emi_number= emi_number,
                borrower_email=borrower_email[index],
                borrower_customer_id=cos_id1[index],
                lender_customer_id = lender_customer_id[index],
                lender_email = lender_email[index]
            )
            anvil.server.call('loan_text', None)
            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = LastScreenWallet(name='LastScreenWallet')
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'LastScreenWallet'

        elif wallet_amount[b_index] < float(total):
            self.show_success_dialog2(f"Insufficient Balance Please Deposit {float(total)}")
            anvil.server.call('loan_text', total)

            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = WalletScreen(name='WalletScreen', loan_amount_text=float(total))
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'WalletScreen'

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

    def show_success_dialog2(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen2(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()
    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def open_dashboard_screen2(self, dialog):

        dialog.dismiss()
        self.manager.current = 'WalletScreen'

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
        self.manager.current = 'DuesScreen'

    def current(self):
        self.manager.current = 'DuesScreen'

class LastScreenWallet(Screen):

    def go_back_home(self):
        self.manager.current = 'DashboardScreen'


class DuesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        today_date = datetime.now(timezone.utc).date()
        data = app_tables.fin_loan_details.search()
        emi_data = app_tables.fin_emi_table.search()
        loan_id = []
        loan_status = []
        borrower_id = []
        schedule_date = []
        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_id.append(i['borrower_customer_id'])
            schedule_date.append(i['first_emi_payment_due_date'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1
            if loan_status[i] == "disbursed" or loan_status[i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id :
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        print(index_list)
        print(shedule_date)
        today_date = datetime.now(timezone.utc).date()

        for i in index_list:
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower ID: {borrower_id[i]}",
                secondary_text=f"Borrower Loan ID : {loan_id[i]}",
                tertiary_text=f"Scheduled Date : {shedule_date[loan_id[i]]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i],: self.icon_button_clicked(instance, loan_id, shedule_date))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id, shedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = BorrowerDuesScreen(name='BorrowerDuesScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'BorrowerDuesScreen'
        self.manager.get_screen('BorrowerDuesScreen').initialize_with_value(loan_id, shedule_date)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass
