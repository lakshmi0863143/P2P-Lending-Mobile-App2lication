from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.uix.modalview import ModalView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import *
import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from datetime import datetime, timedelta, timezone
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

from borrower_wallet import WalletScreen
from lender_wallet import LenderWalletScreen


view_loan_request = """
<WindowManager>:
    ViewLoansRequest:
    ViewLoansProfileScreen:
    ViewLoansProfileScreenLR:
    ViewLoansProfileScreenRL:

<ViewLoansRequest>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:

            MDList:
                id: container

<ViewLoansProfileScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            title_align: 'center'
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
                        text: "Borrower Full Loan details"
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
                        height: dp(680)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: name
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Date Of Apply:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: date
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Tenure:" 
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
                            MDLabel:
                                text: "Phone Number:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Product Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: product_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

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
                            MDLabel:
                                text: "Loan Amount Applied:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDRaisedButton:
                                text: "Reject"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: root.rejected_click()
                                text_color: 0, 0, 0, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

                            MDRaisedButton:
                                text: "Accept"
                                md_bg_color: 5/255, 235/255, 77/255, 1
                                on_release: root.approved_click()
                                theme_text_color: 'Primary'
                                font_name: "Roboto-Bold.ttf"
                                text_color: 0, 0, 0, 1
                                size_hint: 1, None
<ViewLoansProfileScreenLR>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Borrower Loan Details"
            elevation: 3
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
            halign:"center"

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
                        text: "Borrower Full Loan details"
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

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        GridLayout:
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
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Date Of Apply:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: date
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Tenure:" 
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

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Phone Number:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)

                            MDLabel:
                                text: "Product Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: product_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"



                        GridLayout:
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

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount Applied:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        GridLayout:
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
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        GridLayout:
                            cols: 1
                            spacing: dp(10)
                            padding: dp(10)

                            MDRaisedButton:
                                text: "Loan Disbursed"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None
                                on_release: root.paynow()

<ViewLoansProfileScreenRL>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            title_align: 'center'
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
                        text: "Borrower Full Loan details"
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
                        height: dp(680)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)

                            MDLabel:
                                text: "User ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: name
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Date Of Apply:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: date
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Tenure:" 
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
                            MDLabel:
                                text: "Phone Number:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Product Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: product_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"


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
                            MDLabel:
                                text: "Loan Amount Applied:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: dp(50)
                            MDLabel:
                                text: "Your Loan request is Rejected"    
                                bold: True  
                                halign: "center"
                                size_hint_y: None
                                height: dp(50)    
"""
Builder.load_string(view_loan_request)


class ViewLoansRequest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'under process':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Borrower Name : {borrower_name[i]}",
                secondary_text=f"Borrower Number : {profile_mobile_number[number]}",
                tertiary_text=f"Product Name : {product_name[i]}",
                text_color=(0, 0, 0, 1),  # Black color
                theme_text_color='Custom',
                secondary_text_color=(0, 0, 0, 1),
                secondary_theme_text_color='Custom',
                tertiary_text_color=(0, 0, 0, 1),
                tertiary_theme_text_color='Custom'
            )
            item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        # Handle the on_release event here
        print(loan_id)
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewLoansProfileScreenLR(name='ViewLoansProfileScreenLR')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenLR'
            self.manager.get_screen('ViewLoansProfileScreenLR').initialize_with_value(loan_id, data)

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansProfileScreen(name='ViewLoansProfileScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(loan_id, data)
        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(loan_id, data)
        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'LenderDashboard'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()


class ViewLoansProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ViewLoansRequest'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        date_of_apply = []
        loan_status = []
        product_name = []

        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            product_name.append(i['product_name'])
            name.append(i['borrower_full_name'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            loan_status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            number = profile_customer_id.index(customer_id[index])
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.product_name.text = str(product_name[index])
            self.ids.name.text = str(name[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(loan_status[index])
            self.ids.number.text = str(profile_mobile_number[number])

    def email_user(self):
        return anvil.server.call('another_method')

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


    def approved_click(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.perform_approved_click(modal_view), 2)

    def perform_approved_click(self, modal_view):
        # Cancel the animation
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        profile = app_tables.fin_user_profile.search()
        email_user = self.email_user()
        profile_customer_id = []
        profile_email = []
        profile_name = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_email.append(i['email_user'])
            profile_name.append(i['full_name'])

        if email_user in profile_email:
            email_index = profile_email.index(email_user)
        else:
            print("no email found")

        approved_date = datetime.now()
        data = app_tables.fin_loan_details.search()
        loan_id = self.ids.loan_id.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'approved'
            data[index]['lender_accepted_timestamp'] = approved_date
            data[index]['lender_customer_id'] = profile_customer_id[email_index]
            data[index]['lender_full_name'] = profile_name[email_index]
            data[index]['lender_email_id'] = profile_email[email_index]
            sm = self.manager
            disbursed = ViewLoansProfileScreenLR(name='ViewLoansProfileScreenLR')
            sm.add_widget(disbursed)
            sm.current = 'ViewLoansProfileScreenLR'
            self.manager.get_screen('ViewLoansProfileScreenLR').initialize_with_value(loan_id, data)
            self.show_snackbar(f"This Loan ID {loan_id} is Approved")
            return
        else:
            pass



    def rejected_click(self):
        data = app_tables.fin_loan_details.search()
        loan_id = self.ids.loan_id.text
        print(loan_id)

        loan_idlist = []
        for i in data:
            loan_idlist.append(i['loan_id'])
        print(loan_idlist)
        if loan_id in loan_idlist:
            index = loan_idlist.index(loan_id)
            data[index]['loan_updated_status'] = 'rejected'
            sm = self.manager
            disbursed = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')
            sm.add_widget(disbursed)
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(loan_id, data)
            self.show_snackbar(f"This Loan ID {loan_id} is Rejected")
            return
        else:
            pass

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'


class ViewLoansProfileScreenLR(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()



    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        date_of_apply = []
        loan_status = []
        product_name = []

        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            product_name.append(i['product_name'])
            name.append(i['borrower_full_name'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            loan_status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            number = profile_customer_id.index(customer_id[index])
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.product_name.text = str(product_name[index])
            self.ids.name.text = str(name[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(loan_status[index])
            self.ids.number.text = str(profile_mobile_number[number])

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            #self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    '''def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'
        '''

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def paynow(self):
        data = app_tables.fin_loan_details.search()
        disbursed_time = datetime.now()
        paid_time = datetime.now()
        loan_id = self.ids.loan_id.text
        print(loan_id)
        loan_id_list = []
        disbursed = []
        credit_limit = []
        loan_amount = []
        for i in data:
            loan_id_list.append(i['loan_id'])
            disbursed.append(i['lender_accepted_timestamp'])
            credit_limit.append(i['credit_limit'])
            loan_amount.append(i['loan_amount'])

        if loan_id in loan_id_list:
            index = loan_id_list.index(loan_id)

        datetime1 = datetime.fromisoformat(str(disbursed_time)).replace(tzinfo=timezone.utc)
        datetime2 = datetime.fromisoformat(str(disbursed[index])).replace(tzinfo=timezone.utc)

        # Calculate the time difference
        time_difference = datetime1 - datetime2

        # Extract minutes from the timedelta
        minutes_difference = round(time_difference.total_seconds() / 60)

        print(f"The difference in minutes is: {minutes_difference} minutes")

        if minutes_difference < 30:
            self.show_snackbar(f"Time Out You Must Finish Before 30 Minutes {loan_amount[index]} to this Loan ID {loan_id_list[index]}")
            data[index]['loan_updated_status'] = 'disbursed'
            data[index]['loan_disbursed_timestamp'] = paid_time
            from lender_dashboard import LenderDashboard
            sm = self.manager

            # Create a new instance of the LoginScreen
            login_screen = LenderDashboard(name='LenderDashboard')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(login_screen)

            # Switch to the LoginScreen
            sm.current = 'LenderDashboard'
            return

        elif minutes_difference > 30:
            self.show_snackbar(f"Time Out You Must Finish Before 30 Minutes")
            data[index]['loan_updated_status'] = 'lost opportunities'
            self.manager.current = 'ViewLoansRequest'
            return


class ViewLoansProfileScreenRL(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ViewLoansRequest'

    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        date_of_apply = []
        loan_status = []
        product_name = []

        name = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            product_name.append(i['product_name'])
            name.append(i['borrower_full_name'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            loan_status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            number = profile_customer_id.index(customer_id[index])
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.product_name.text = str(product_name[index])
            self.ids.name.text = str(name[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.status.text = str(loan_status[index])
            self.ids.number.text = str(profile_mobile_number[number])

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
        self.manager.current = 'ViewLoansRequest'


class MyScreenManager(ScreenManager):
    pass


