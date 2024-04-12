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
from datetime import datetime, timezone, timedelta

from kivymd.uix.spinner import MDSpinner
import anvil.tables.query as q

user_helpers2 = """
<WindowManager>:
    BorrowerDuesScreen:
    DuesScreen:
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
    def __init__(self, loan_details, **kwargs):
        super().__init__(**kwargs)
        self.loan_details = loan_details
        print(self.loan_details)

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


class DuesScreen(Screen):
    loan_details = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = ""
        # self.init_components(**properties)

        today_date = datetime.now(timezone.utc).date()
        self.loan_details = loan_details = []

        all_loans_disbursed = app_tables.fin_loan_details.search(
            loan_updated_status=q.any_of("disbursed loan", "extension", "foreclosure"),
            first_emi_payment_due_date=q.less_than_or_equal_to(today_date)
        )
        loan_list = list(all_loans_disbursed)
        print(loan_list)
        for loan in all_loans_disbursed:
            print(loan)
            loan_id = loan['loan_id']
            print(loan_id)
            all_loans = list(app_tables.fin_emi_table.search(
                loan_id=loan_id,
                next_payment=q.less_than_or_equal_to(today_date)
            ))
            print(all_loans)
            if all_loans:
                all_loans.sort(key=lambda x: x['next_payment'], reverse=True)
                latest_loan = all_loans[0]
                loan_detail = app_tables.fin_loan_details.get(loan_id=latest_loan['loan_id'])
                user_profile = app_tables.fin_user_profile.get(customer_id=loan_detail['lender_customer_id'])
                if loan_detail is not None and user_profile is not None:
                    loan_amount = loan_detail['loan_amount']
                    scheduled_payment = latest_loan['scheduled_payment']
                    next_payment = latest_loan['next_payment']
                    days_left = (today_date - next_payment).days

                    emi_number = latest_loan['emi_number']
                    account_number = latest_loan['account_number']
                    tenure = loan_detail['tenure']
                    interest_rate = loan_detail['interest_rate']
                    borrower_loan_created_timestamp = loan_detail['borrower_loan_created_timestamp']
                    loan_updated_status = loan_detail['loan_updated_status']
                    loan_disbursed_timestamp = loan_detail['loan_disbursed_timestamp']
                    emi_payment_type = loan_detail['emi_payment_type']
                    lender_customer_id = loan_detail['lender_customer_id']
                    borrower_customer_id = loan_detail['borrower_customer_id']
                    first_emi_payment_due_date = loan_detail['first_emi_payment_due_date']
                    total_repayment_amount = loan_detail['total_repayment_amount']
                    total_processing_fee_amount = loan_detail['total_processing_fee_amount']
                    mobile = user_profile['mobile']
                    product_name = loan_detail['product_name']
                    product_description = loan_detail['product_description']
                    lender_full_name = loan_detail['lender_full_name']
                    loan_state_status = loan_detail['loan_state_status']
                    product_id = loan_detail['product_id']
                    total_interest_amount = loan_detail['total_interest_amount']
                    Scheduled_date = latest_loan['next_payment']

                    loan_details.append({
                        'loan_id': loan_id,
                        'loan_amount': loan_amount,
                        'scheduled_payment': scheduled_payment,
                        'days_left': days_left,
                        'tenure': tenure,
                        'interest_rate': interest_rate,
                        'borrower_loan_created_timestamp': borrower_loan_created_timestamp,
                        'emi_number': emi_number,
                        'account_number': account_number,
                        'loan_updated_status': loan_updated_status,
                        'loan_disbursed_timestamp': loan_disbursed_timestamp,
                        'next_payment': next_payment,
                        'emi_payment_type': emi_payment_type,
                        'lender_customer_id': lender_customer_id,
                        'first_emi_payment_due_date': first_emi_payment_due_date,
                        'total_repayment_amount': total_repayment_amount,
                        'total_processing_fee_amount': total_processing_fee_amount,
                        'mobile': mobile,
                        'product_description': product_description,
                        'product_name': product_name,
                        'lender_full_name': lender_full_name,
                        'borrower_customer_id': borrower_customer_id,
                        'loan_state_status': loan_state_status,
                        'product_id': product_id,
                        'total_interest_amount': total_interest_amount,
                        'Scheduled_date': Scheduled_date,
                    })
            else:

                # If there are no emi records, append loan details without checking next payment date
                loan_detail = app_tables.fin_loan_details.get(loan_id=loan_id)
                user_profile = app_tables.fin_user_profile.get(customer_id=loan_detail['lender_customer_id'])
                if loan_detail is not None and user_profile is not None:
                    loan_amount = loan_detail['loan_amount']
                    first_emi_payment_due_date = loan_detail['first_emi_payment_due_date']
                    print(first_emi_payment_due_date)
                    days_left = (today_date - first_emi_payment_due_date).days
                    # Fetch account number from user profile table based on customer_id
                    user_profile = app_tables.fin_user_profile.get(customer_id=loan_detail['borrower_customer_id'])
                    if user_profile is not None:
                        account_number = user_profile['account_number']
                    else:
                        account_number = "N/A"

                    # Set emi_number to 0
                    emi_number = 0

                    tenure = loan_detail['tenure']
                    interest_rate = loan_detail['interest_rate']
                    borrower_loan_created_timestamp = loan_detail['borrower_loan_created_timestamp']
                    loan_updated_status = loan_detail['loan_updated_status']
                    loan_disbursed_timestamp = loan_detail['loan_disbursed_timestamp']
                    emi_payment_type = loan_detail['emi_payment_type']
                    lender_customer_id = loan_detail['lender_customer_id']
                    total_repayment_amount = loan_detail['total_repayment_amount']
                    total_processing_fee_amount = loan_detail['total_processing_fee_amount']
                    mobile = user_profile['mobile']
                    product_name = loan_detail['product_name']
                    product_description = loan_detail['product_description']
                    borrower_customer_id = loan_detail['borrower_customer_id']
                    lender_full_name = loan_detail['lender_full_name']
                    scheduled_payment = loan_disbursed_timestamp.date()
                    loan_state_status = loan_detail['loan_state_status']
                    product_id = loan_detail['product_id']
                    total_interest_amount = loan_detail['total_interest_amount']
                    Scheduled_date = loan_detail['first_emi_payment_due_date']

                    # Calculate next_payment based on first_payment_due_date
                    if emi_payment_type == 'One Time':
                        if tenure:
                            next_payment = loan_disbursed_timestamp.date() + timedelta(days=30 * tenure)
                    elif emi_payment_type == 'Monthly':
                        # For monthly payment, set next_payment to a month after first_payment_due_date
                        next_payment = loan_disbursed_timestamp.date() + timedelta(days=30)
                    elif emi_payment_type == 'Three Months':
                        # For three-month payment, set next_payment to three months after first_payment_due_date
                        next_payment = loan_disbursed_timestamp.date() + timedelta(days=90)
                    elif emi_payment_type == 'Six Months':
                        # For six-month payment, set next_payment  six months after first_payment_due_date
                        next_payment = loan_disbursed_timestamp.date() + timedelta(days=180)
                    else:
                        # Default to monthly calculation if emi_payment_type is not recognized
                        next_payment = loan_disbursed_timestamp.date() + timedelta(days=30)

                    loan_details.append({
                        'loan_id': loan_id,
                        'loan_amount': loan_amount,
                        'scheduled_payment': scheduled_payment,
                        # Set scheduled_payment to first_payment_due_date first_emi_payment_due_date
                        'next_payment': next_payment,
                        'days_left': days_left,
                        'tenure': tenure,
                        'interest_rate': interest_rate,
                        'borrower_loan_created_timestamp': borrower_loan_created_timestamp,
                        'loan_updated_status': loan_updated_status,
                        'loan_disbursed_timestamp': loan_disbursed_timestamp,
                        'emi_number': emi_number,
                        'account_number': account_number,
                        'emi_payment_type': emi_payment_type,
                        'lender_customer_id': lender_customer_id,
                        'total_repayment_amount': total_repayment_amount,
                        # 'first_payment_due_date': first_payment_due_date
                        'total_processing_fee_amount': total_processing_fee_amount,
                        'mobile': mobile,
                        'product_description': product_description,
                        'product_name': product_name,
                        'lender_full_name': lender_full_name,
                        'borrower_customer_id': borrower_customer_id,
                        'loan_state_status': loan_state_status,
                        'product_id': product_id,
                        'total_interest_amount': total_interest_amount,
                        'Scheduled_date': Scheduled_date,

                    })
            # self.repeating_panel_2.items = loan_details
            print(loan_details)
        for loan_details_1 in loan_details:
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower id: {loan_details_1['borrower_customer_id']}",
                secondary_text=f"Borrower loan id : {loan_details_1['loan_id']}",
                tertiary_text=f"Scheduled date : {loan_details_1['Scheduled_date']}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_details_1['loan_id'],: self.icon_button_clicked(instance,
                                                                                                              loan_id,
                                                                                                              loan_details_1))
            self.ids.container.add_widget(item)
            for loan_detail_1 in loan_details:
                print("Processing loan:", loan_detail_1)
                if loan_detail_1['days_left'] > 6 and loan_detail_1['days_left'] <= 8:
                    print("Updating status to 'lapsed loan'")
                    loan_detail_1['loan_state_status'] = 'lapsed loan'
                    loan_row = app_tables.fin_loan_details.get(loan_id=loan_detail_1['loan_id'])
                    if loan_row is not None:
                        loan_row['loan_state_status'] = 'lapsed loan'
                        loan_row.update()
                elif loan_detail_1['days_left'] > 8 and loan_detail_1['days_left'] <= 98:
                    print("Updating status to 'default loan'")
                    loan_detail_1['loan_state_status'] = 'default loan'
                    loan_row = app_tables.fin_loan_details.get(loan_id=loan_detail_1['loan_id'])
                    if loan_row is not None:
                        loan_row['loan_state_status'] = 'default loan'
                        loan_row.update()
                elif loan_detail_1['days_left'] > 98:
                    print("Updating status to 'default loan'")
                    loan_detail_1['loan_state_status'] = 'NPA'
                    loan_row = app_tables.fin_loan_details.get(loan_id=loan_detail['loan_id'])
                    if loan_row is not None:
                        loan_row['loan_updated_status'] = 'NPA'
                        loan_row.update()

    def icon_button_clicked(self, instance, loan_id, loan_details_1, ):
        # Highlight the selected item
        self.highlight_item(instance)

        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        sm = self.manager

        loan_details = loan_details_1

        # Create a new instance of the ApplicationTrackerScreen
        approved = BorrowerDuesScreen(name='BorrowerDuesScreen', loan_details=loan_details)

        # Add the ApplicationTrackerScreen to the existing ScreenManager
        sm.add_widget(approved)

        # Switch to the ApplicationTrackerScreen
        sm.current = 'BorrowerDuesScreen'
        self.manager.get_screen('BorrowerDuesScreen')

    def highlight_item(self, item):
        # Deselect all other items
        self.deselect_items()

        # Change the background color of the clicked item to indicate selection
        item.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired
        self.selected_item = item

    def deselect_items(self):
        # Deselect all items in the list
        for item in self.ids.container.children:
            if isinstance(item, ThreeLineAvatarIconListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

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
