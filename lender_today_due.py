from datetime import datetime, timezone

from anvil.tables import app_tables
from bson import utc
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server
import anvil.server

lender_today_due = '''

<WindowManager>:
    TodayDuesTD:
    ViewProfileTD:

<TodayDuesTD>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Today's Dues"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container
<ViewProfileTD>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Details"
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
                        text: " Today Dues Details"
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
                        height: dp(650)
                        padding: [10, 0, 0, 0]
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
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_id
                                text: "" 
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_amount
                                text: "" 

                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 
                            MDLabel:
                                text: "Account Number" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: number
                                text: "" 
                            MDLabel:
                                text: "Emi Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: emi_amount
                                text: "" 
                            MDLabel:
                                text: "Extra Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: extra_amount
                                text: "" 
                            MDLabel:
                                text: "Total Emi Amount " 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: total_emi_amount
                                text: ""





'''
Builder.load_string(lender_today_due)
date = datetime.today().date()
print(date)


class TodayDuesTD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = app_tables.fin_emi_table.search()
        data1 = app_tables.fin_loan_details.search()
        loan_id = []
        schedule_payment = []
        scheduled_payment_date_list = []
        coustomer_id = []

        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            print(loan_id)
            schedule_payment.append(i['scheduled_payment'])
            print(schedule_payment)
            scheduled_payment_date_list.append(i['scheduled_payment_made'])
            coustomer_id.append(i['borrower_customer_id'])

        c = -1
        index_list = []

        for i in range(s):
            c += 1

            if schedule_payment[i] == date:
                index_list.append(c)

        b = 1
        k = -1

        for i in index_list:
            b += 1
            k += 1
            today_date = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=utc)

            # Access the specific date corresponding to the current iteration
            current_scheduled_payment_date = scheduled_payment_date_list[i]

            # Make sure current_scheduled_payment_date is offset-aware (e.g., using pytz)
            current_scheduled_payment_date = current_scheduled_payment_date.replace(tzinfo=utc)

            # Calculate the difference in days
            days_until_payment = (current_scheduled_payment_date - today_date).days

            if days_until_payment < 0:
                days_until_payment = 0

            print(f"Today's date: {today_date}")
            print(f"Scheduled payment date: {current_scheduled_payment_date}")
            print(f"Days until scheduled payment date: {days_until_payment} days")

        loan_id1 = []
        borrower = []
        b = 0
        for i in data1:
            loan_id1.append(i['loan_id'])
            borrower.append(i['borrower_full_name'])

        index = -1
        a = 0

        for row in index_list:
            if loan_id[row] in loan_id1:
                a = loan_id1.index(loan_id[row])

            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower Name: {borrower[a]}",
                secondary_text=f"Schedule Payment: {schedule_payment[row]}",
                tertiary_text=f"Day Passed Due Date: {days_until_payment}",
            )
            item.bind(on_release=lambda instance, loan_id=loan_id1[row]: self.icon_button_clicked(instance, loan_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, value):
        data = app_tables.fin_emi_table.search()
        data1 = app_tables.fin_loan_details.search()
        data2 = app_tables.fin_extends_loan.search()
        print(value)
        loan_status = None
        for row in data1:
            if row['loan_id'] == value:
                loan_status = row['loan_updated_status']
                break
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_today_due = ViewProfileTD(name='ViewProfileTD')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_today_due)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileTD'
        self.manager.get_screen('ViewProfileTD').initialize_with_value(value, data, data1, data2)

    '''
    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_today_data')

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def menu(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')
    '''

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
        self.manager.current = 'LenderDashboard'


class ViewProfileTD(Screen):
    def initialize_with_value(self, value, data, data1, data2):
        loan_id = []
        loan_amount = []
        tenure = []
        interest_rate1 = []

        for item in data1:
            loan_id.append(item['loan_id'])
            loan_amount.append(item['loan_amount'])
            tenure.append(item['tenure'])
            interest_rate1.append(item['interest_rate'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.interest.text = str(interest_rate1[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.loan_amount.text = str(loan_amount[index])

        acc_num = []

        for item1 in data:
            acc_num.append(item1['account_number'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.number.text = str(acc_num[index])
        extend_amount = []
        emi_amount = []
        for item2 in data2:
            extend_amount.append(item2['extension_amount'])
            emi_amount.append(item2['new_emi'])
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.number.text = str(acc_num[index])
            self.ids.emi_amount.text = str(emi_amount[index])

            if index < len(emi_amount) and index < len(extend_amount):  # Check index validity
                print("emi_amount:", emi_amount)
                print("extend_amount:", extend_amount)
                print("index:", index)
                total_amount = emi_amount[index] + extend_amount[index]
                self.ids.extra_amount.text = str(extend_amount[index])
                self.ids.total_emi_amount.text = str(total_amount)
            else:
                # Handle invalid index
                print("Invalid index:", index)
                self.ids.extra_amount.text = "N/A"
                self.ids.total_emi_amount.text = "N/A"

    def get_table_data(self):

        return anvil.server.call('get_today_data')

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def profile(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def menu(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')

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

    def on_back_button_press(self):
        self.manager.current = 'TodayDuesTD'


class MyScreenManager(ScreenManager):
    pass
