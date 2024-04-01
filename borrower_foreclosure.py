from anvil import Label
from anvil.tables import app_tables
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from datetime import datetime

from kivymd.uix.snackbar import Snackbar

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server


loan_forecloseB = '''
<WindowManager>:
    LoansDetailsB:
    ViewProfileScreenFB:
    ForecloseDetails:

<LoansDetailsB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container

<ViewProfileScreenFB>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    id: box1
                    orientation: 'vertical'
                    size_hint_y: None
                    MDLabel:
                        text: "View Loan details"
                        halign: "center"
                        bold: True
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(850)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Tenure(Months):" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: tenure
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Interest Rate:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: interest
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Credit limit:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: limit
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Total Payment Made:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: total_payment
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Foreclosure Type:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: closer_type
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: 10

                            CheckBox:
                                id: check_box
                                size_hint: (None, None)
                                width: 50
                                bold: True
                                color: 0.043, 0.145, 0.278, 1 

                            MDLabel:
                                text: "I Agree Terms and Conditions"
                                multiline: False


                        MDGridLayout:
                            cols: 2
                            spacing: 30
                            padding: 20
                            size_hint: 1, 1
                            pos_hint: {'center_x': 0.48, 'center_y': 0.5}

                            MDRaisedButton:
                                text: "BACK"
                                md_bg_color: 0.043, 0.145, 0.278, 1 
                                on_release: root.on_back()
                                text_color: 1, 1, 1, 1
                                size_hint: 1, None


                            MDRaisedButton:
                                id: foreclose_button
                                text: "FORECLOSE"
                                md_bg_color: 0.043, 0.145, 0.278, 1 
                                on_release: root.on_foreclose_press(loan.text)
                                size_hint: 1, None


<ForecloseDetails>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)  
        spacing: dp(20) 
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10) 
                spacing: dp(25)   
                size_hint_y: None
                height: self.minimum_height
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(33)  

                    MDLabel:
                        text: "Loan Foreclosure For LoanA/C:"
                        bold: True
                    MDLabel:
                        id: loan_id_label1
                        bold:True

                MDLabel:
                    text: "Foreclosure  Details"
                    bold: True

                Widget:
                    size_hint_y: None
                    height: dp(2)  
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: "Amount paid"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(33)  

                    MDLabel:
                        text: "Total amount Paid "
                        bold: True

                    MDLabel:
                        id: totalamount
                        text: ""

                    MDLabel:
                        text: "Monthly installment"

                    MDLabel:
                        id: monthly_installment
                        text: ""

                    MDLabel:
                        text: "Interest Amount"

                    MDLabel:
                        id: interest_amount
                        text: ""

                    MDLabel:
                        text: "Monthly EMI"

                    MDLabel:
                        id: monthly_emi1
                        text: ""
                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Loan Closure Amount"
                    bold: True
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(52)

                    MDLabel:
                        text: "Over all Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: overall_amount
                        text: ""
                    MDLabel:
                        text: "Over all Monthly installment"

                    MDLabel:
                        id: over_month
                        text: ""
                    MDLabel:
                        text: "Overall Interest Amount "

                    MDLabel:
                        id: overall_interest_amount
                        text: ""

                    MDLabel:
                        text: "Total Amount"

                    MDLabel:
                        id: total_amount
                        text: ""

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Amount Due"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(45)

                    MDLabel:
                        text: "Outstanding Amount"


                    MDLabel:
                        id: outstanding_amount
                        text: ""

                    MDLabel:
                        text: "Foreclosure Fee "

                    MDLabel:
                        id: foreclosure_fee
                        text: ""

                    MDLabel:
                        text: "Foreclosure Amount"

                    MDLabel:
                        id: foreclosure_amount
                        text: ""

                    MDLabel:
                        text: "Total Due Amount"
                        bold: True

                    MDLabel:
                        id: total_due_amount1
                        text: ""

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None

                    MDLabel:
                        text: 'Reason for Foreclosure '
                        valign: 'top'
                        bold: True

                    MDTextField:
                        id: reason
                        hint_text: 'Enter text here'

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    spacing: dp(10)

                    CheckBox:
                        size_hint: None, None
                        width: dp(30) 
                        color: (195/255, 110/255, 108/255, 1)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  

                MDLabel:
                    text: ""

                MDGridLayout:
                    cols: 2
                    spacing: dp(10)
                    padding: dp(5)
                    size_hint: 1, None

                    MDRaisedButton:
                        text: "CANCEL"
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        theme_text_color: 'Custom'
                        on_release: app.root.current = 'ViewProfileScreenFB'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None

                    MDRaisedButton:
                        text: "SUBMIT"
                        id : submit
                        md_bg_color: 0.043, 0.145, 0.278, 1 
                        on_release: root.add_data(loan_id_label1.text, outstanding_amount.text, foreclosure_fee.text, foreclosure_amount.text, reason.text)

                        size_hint: 1, None



'''
Builder.load_string(loan_forecloseB)
date = datetime.today()
print(date)


class LoansDetailsB(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        product_name = []
        loan_id = []
        email1 = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            product_name.append(i['product_name'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            email1.append(i['borrower_email_id'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append('email_user')

        cos_id = None
        index = -1
        if email in profile_email_id:
            index = profile_email_id.index(email)

        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        if cos_id is not None:
            print(cos_id, type(cos_id))
            print(customer_id[-1], type(customer_id[-1]))
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if customer_id[c] == cos_id and loan_status[c] == 'disbursed':
                    index_list.append(c)

            b = 1
            k = -1
            for i in index_list:
                b += 1
                k += 1
                number = profile_customer_id.index(customer_id[i])
                item = ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                # Create a lambda function with loan_id as an argument
                item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
            # Handle the on_release event here
            value = instance.text.split(':')[-1].strip()
            data = app_tables.fin_loan_details.search()
            loan_status = None
            for loan in data:
                if loan['loan_id'] == value:
                    loan_status = loan['loan_updated_status']
                    break
            print(loan_id)

            # Proceed with the action for the selected loan ID

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewProfileScreenFB(name='ViewProfileScreenFB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenFB'
            self.manager.get_screen('ViewProfileScreenFB').initialize_with_value(loan_id, data)

    def go_back(self):
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

class ViewProfileScreenFB(Screen):
    def initialize_with_value(self, value, data):
        emi1 = app_tables.fin_emi_table.search()
        pro_details = app_tables.fin_product_details.search()
        loan_id = []
        loan_amount = []
        email1 = []
        name = []
        tenure = []
        interest = []
        credit = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            email1.append(i['borrower_email_id'])
            name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            credit.append(i['credit_limit'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest.text = str(interest[index])
            self.ids.limit.text = str(credit[index])

            emi_loan = [i['emi_number'] for i in emi1 if i['loan_id'] == value]
            print(emi_loan)
            if emi_loan:
                highest_number = max(emi_loan)
                total_payment = highest_number
            else:
                total_payment = 0

            self.ids.total_payment.text = str(total_payment)

            foreclose_type = [i['foreclose_type'] for i in pro_details if
                              i['product_id'] == data[index]['product_id']]
            print(foreclose_type)
            if foreclose_type:
                foreclose_value = foreclose_type[0]
                self.ids.closer_type.text = str(foreclose_value)

                if foreclose_value == 'Eligible':
                    self.ids.foreclose_button.disabled = False
                else:
                    self.ids.foreclose_button.disabled = True
                    self.show_snackbar(f"This Foreclose Value need to be Eligible")

            minimum_months = [i['min_months'] for i in pro_details if i['product_id'] == data[index]['product_id']]
            print(minimum_months)
            if emi_loan and minimum_months:
                if emi_loan[0] >= minimum_months[0]:
                    self.ids.foreclose_button.disabled = False
                else:
                    self.ids.foreclose_button.disabled = True
            else:
                print("Either emi_loan or minimum_months is empty.")

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_back_button_press(self):
        self.manager.current = 'LoansDetailsB'

    def on_back(self):
        self.manager.current = 'LoansDetailsB'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def on_foreclose_press(self, loan_id):
        sm = self.manager

        # Create a new instance of the LoginScreen
        approved = ForecloseDetails(name='ForecloseDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(approved)

        # Switch to the LoginScreen
        sm.current = 'ForecloseDetails'
        self.manager.get_screen('ForecloseDetails').initialize_with_value(loan_id)


class ForecloseDetails(Screen):

    def initialize_with_value(self, value):
        data1 = app_tables.fin_foreclosure.search()
        data = app_tables.fin_loan_details.search()
        pro = app_tables.fin_product_details.search()
        emi1 = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        loan_id = []
        request_on = []

        index2 = -1
        for i in data1:
            loan_id.append(i['loan_id'])
            request_on.append(i['requested_on'])

        month_emi = []
        loan_id1 = []
        loan_amount = []
        tenure = []
        for i in data:
            month_emi.append(i['monthly_emi'])
            loan_id1.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])

        emi_num = []
        loan_id2 = []
        for i in emi1:
            emi_num.append(i['emi_number'])
            loan_id2.append(i['loan_id'])

        if value in loan_id1:
            index = loan_id1.index(value)
            self.ids.loan_id_label1.text = str(loan_id1[index])

        if value in loan_id1:
            index2 = loan_id1.index(value)
            self.ids.monthly_emi1.text = str(month_emi[index2])

        for i in emi1:
            if i['loan_id'] == value:
                emi_num = i['emi_number']
                break  # Break the loop once the EMI number is found

        total_amount = 0
        if emi_num is not None:  # Check if emi_num is found
            total_amount = month_emi[index2] * emi_num
            print(month_emi[index2], emi_num)

        self.ids.totalamount.text = str(total_amount)

        if value in loan_id1:
            index3 = loan_id1.index(value)
            monthly_installment = loan_amount[index3] / tenure[index3]
            print(loan_amount[index3], tenure[index3])
            self.ids.monthly_installment.text = str(monthly_installment)

        if value in loan_id1:
            index4 = loan_id1.index(value)
            interest_amount = month_emi[index4] - monthly_installment
            print(month_emi[index4], monthly_installment)
            self.ids.interest_amount.text = str(interest_amount)

        if value in loan_id1:
            index5 = loan_id1.index(value)
            overall_outstanding_amount = loan_amount[index5] - (monthly_installment * emi_num)
            print(loan_amount[index5], monthly_installment, emi_num)
            self.ids.overall_amount.text = str(overall_outstanding_amount)

        if value in loan_id1:
            index6 = loan_id1.index(value)
            outstanding_months = tenure[index6] - emi_num
            overall_monthly_installment = monthly_installment * outstanding_months
            print(monthly_installment, outstanding_months)
            self.ids.over_month.text = str(overall_monthly_installment)

        if value in loan_id1:
            index7 = loan_id1.index(value)
            interest_amount_per_month = month_emi[index7] - monthly_installment
            overall_interest_amount = interest_amount_per_month * outstanding_months
            print(interest_amount_per_month, outstanding_months)
            self.ids.overall_interest_amount.text = str(overall_interest_amount)

        if value in loan_id1:
            total_amount1 = overall_outstanding_amount + overall_interest_amount
            self.ids.total_amount.text = str(total_amount1)
            outstanding_amount1 = overall_outstanding_amount
            self.ids.outstanding_amount.text = str(outstanding_amount1)

        product_id1 = []
        for product in data:
            product_id1.append(product['product_id'])
            print(product_id1)
        product_id2 = []
        foreclose_fee = []
        for product in pro:
            product_id2.append(product['product_id'])
            foreclose_fee.append(product['foreclosure_fee'])

        if value in loan_id:
            index10 = loan_id.index(value)
            print(product_id1[index10])

        index10 = -1

        if product_id1[index10] in product_id2:
            index11 = product_id1.index(product_id1[index10])
            self.ids.foreclosure_fee.text = str(foreclose_fee[index11])
            foreclose_amount = overall_outstanding_amount * (foreclose_fee[index11] / 100)
            print(overall_outstanding_amount, foreclose_fee[index11])
            self.ids.foreclosure_amount.text = str(foreclose_amount)
            total_due_amount = overall_outstanding_amount + foreclose_amount
            self.ids.total_due_amount1.text = str(total_due_amount)

    def add_data(self, loan_id, outstanding_amount, foreclose_fee, foreclose_amount, reason):
        print(loan_id, outstanding_amount, foreclose_amount, foreclose_fee)
        app_tables.fin_foreclosure.add_row(loan_id=loan_id, outstanding_amount=float(outstanding_amount),
                                           foreclose_fee=int(foreclose_fee), foreclose_amount=float(foreclose_amount),
                                           reason=reason, status='under process')
        self.show_snackbar(f"This Loan ID {loan_id} has been submitted")
        self.manager.current = 'DashboardScreen'
    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

class MyScreenManager(ScreenManager):
    pass


