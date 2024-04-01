
import anvil.server
from kivy.config import value
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
import anvil.users
import server
from anvil.tables import app_tables
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager

extension_loan_request = """
<WindowManager>:
    ExtensionLoansRequest:
    ExtensionLoansProfileScreen:
    ExtendLoansScreen:

<ExtensionLoansRequest> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:

            MDList:
                id: container1

<ExtensionLoansProfileScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'

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
                        text: " Borrower Extension Request"
                        halign: "center"
                        bold: True
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    width:self.minimum_width
                    padding: dp(20)
                    spacing:dp(20)
                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(800)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                width:0.7
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "User ID :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: user1
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan ID :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                halign: "left"
                                height:dp(50)
                                size_hint_y:None

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Name :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: name
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Phone Number :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Product Name :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: product_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Tenure :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: tenure
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Interest Rate :" 
                                size_hint_y:None
                                bold: True
                                height:dp(50)
                                halign: "left"
                            MDLabel:
                                id: interest
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Allowed :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_allowed
                                text:""
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Fees :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Months :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDTextField:
                                hint_text: ""
                                id: extension_months
                                height:dp(50)
                                size_hint_y:None
                                halign: "left"
                        MDFloatLayout:
                            MDRaisedButton:
                                id:extension_request
                                text: "Extension Request"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold"
                                size_hint: 0.4, None
                                height: dp(50)
                                on_release:root.on_extend()
                                text: "Next"
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                font_size:dp(15)

<ExtendLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'

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
                        text: " Borrower Extension Details"
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
                        height: dp(900)
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
                                text: "Loan ID :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                                bold: True
                            MDLabel:
                                id: loan_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Fee :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_fee
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Extension Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: extension_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Finial Repayment Amount :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: finial_repayment_amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "New EMI :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: new_emi
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 1
                            spacing: dp(5)
                            padding: dp(10)
                            MDLabel:
                                text: "Reason For Extended Loan :" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                            MDTextField:
                                hint_text: ""
                                id: reason
                                size_hint_y:None
                                height:dp(50)

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDCheckbox:
                                id: kyc_checkbox
                                size_hint_x: None
                                width: "20dp"
                            MDLabel:
                                text: "I Agree Terms and Conditions"
                                multiline: False
                                theme_text_color: 'Primary'
                                halign: 'left'
                                valign: 'center'
                                bold: True

                        MDFloatLayout:
                            MDRaisedButton:
                                text: "Submit"
                                md_bg_color: 0.043, 0.145, 0.278, 1
                                font_name: "Roboto-Bold"
                                size_hint: 0.4, None
                                on_release:root.add_data()
                                height:"50dp"
                                pos_hint: {'right': 0.5, 'y': 0.5}
                                font_size:dp(15)


"""
Builder.load_string(extension_loan_request)


class ExtensionLoansRequest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search(email_user=email)
        customer_id = []
        loan_id = []
        loan_amount = []
        borrower_name = []
        loan_status = []
        tenure = []
        product_name = []
        email1 = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])
        product = app_tables.fin_product_details.search()
        extension_allowed = []
        extension_fee = []
        for i in product:
            extension_allowed.append(i['extension_allowed'])
            extension_fee.append(i['extension_fee'])
        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
        cos_id = None
        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]
        if cos_id is not None:
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if loan_status[c] == 'disbursed' and customer_id[c] == cos_id:
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
                    secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container1.add_widget(item)

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()

    def icon_button_clicked(self, instance, loan_id):
        print(loan_id)
        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'disbursed':
            # Open the screen for approved loans
            sm = self.manager
            disbursed = ExtensionLoansProfileScreen(name='ExtensionLoansProfileScreen')
            sm.add_widget(disbursed)
            sm.current = 'ExtensionLoansProfileScreen'
            self.manager.get_screen('ExtensionLoansProfileScreen').initialize_with_value(loan_id, data)
        else:
            pass

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class ExtensionLoansProfileScreen(Screen):
    def initialize_with_value(self, value, data):
        profile = app_tables.fin_user_profile.search()
        profile_customer_id = [i['customer_id'] for i in profile]
        profile_mobile_number = [i['mobile'] for i in profile]

        product = app_tables.fin_product_details.search()
        extension_details = {i['product_name']: (i['extension_allowed'], i['extension_fee']) for i in product}

        loan_details = {i['loan_id']: (
        i['borrower_customer_id'], i['loan_amount'], i['tenure'], i['product_name'], i['interest_rate'],
        i['borrower_full_name']) for i in data}

        if value in loan_details:
            borrower_customer_id, loan_amount, tenure, product_name, interest_rate, borrower_name = loan_details[value]
            extension_allowed, extension_fee = extension_details.get(product_name, ('No', 0))
            if borrower_customer_id in profile_customer_id:
                number = profile_customer_id.index(borrower_customer_id)
                self.ids.number.text = str(profile_mobile_number[number])
            else:
                number = 0
                self.ids.number.text = "N/A"

            self.ids.loan_id.text = str(value)
            self.ids.loan_amount.text = str(loan_amount)
            self.ids.user1.text = str(borrower_customer_id)
            self.ids.interest.text = str(interest_rate)
            self.ids.tenure.text = str(tenure)
            self.ids.product_name.text = str(product_name)
            self.ids.extension_allowed.text = str(extension_allowed)
            self.ids.extension_fee.text = str(extension_fee)
            self.ids.name.text = str(borrower_name)

            # Check if the button exists in ids before accessing its attributes
            if extension_allowed == 'Yes':
                self.ids.extension_request.disabled = False
            else:
                self.show_popup("Extension Warning", "Your extension is not allowed")
                self.ids.extension_request.disabled = True
        else:
            print(f"Loan with ID '{value}' not found in loan details.")

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansRequest'

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansRequest'

    def on_extend(self):
        loan_id = self.ids.loan_id.text
        extension_fee = self.ids.extension_fee.text
        sm = self.manager
        profile = ExtendLoansScreen(name='ExtendLoansScreen')
        sm.add_widget(profile)  # Add the screen to the ScreenManager
        sm.current = 'ExtendLoansScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class ExtendLoansScreen(Screen):
    loan_id = ""
    loan_amount = ""
    extension_fee = ""

    def on_back_button_press(self):
        self.manager.current = 'ExtensionLoansProfileScreen'
        # Assuming you have these labels in your Kivy app

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)
        self.root_screen = self.manager.get_screen('ExtensionLoansProfileScreen')
        loan_id = str(self.root_screen.ids.loan_id.text)
        self.ids.loan_id.text = str(loan_id)
        loan_amount = str(self.root_screen.ids.loan_amount.text)
        self.ids.loan_amount.text = str(loan_amount)
        extension_fee = str(self.root_screen.ids.extension_fee.text)
        self.ids.extension_fee.text = str(extension_fee)
        tenure = str(self.root_screen.ids.tenure.text)
        loan_extension_months = str(self.root_screen.ids.extension_months.text)
        extension_amount = float(extension_fee) * float(loan_amount) / 100
        print(extension_amount)
        self.ids.extension_amount.text = f"{str(extension_amount)}"
        emi = app_tables.fin_product_details.search()
        if emi:
            roi = emi[0]['roi']
            roi = float(roi)
            print(roi)
        else:
            return "ROI not found for the selected category"
        monthly_interest_rate = (roi / 100) / 12
        total_tenure = app_tables.fin_emi_table.search(loan_id=loan_id)
        total_tenure = total_tenure[0]['emi_number']
        # Calculate EMI using the formula
        remaining_tenure = (float(tenure) - float(total_tenure)) + float(loan_extension_months)

        loan_extension = (float(loan_amount) * monthly_interest_rate * pow(1 + monthly_interest_rate,
                                                                           float(remaining_tenure))) / \
                         (pow(1 + monthly_interest_rate, float(remaining_tenure)) - 1)
        emi = loan_extension
        self.ids.new_emi.text = f"{float(emi):.2f}"
        print(emi)

        payment = app_tables.fin_emi_table.search()
        if payment:
            total_payment = payment[0]['emi_number']
            if total_payment is not None:
                total_payment = float(total_payment)
            else:
                return "Invalid total payment emi number"
            emi_paid = total_payment * emi
            remaining_loan_amount = (float(loan_amount) - emi_paid) + float(extension_amount)
            print(remaining_loan_amount)
            self.ids.finial_repayment_amount.text = f"{remaining_loan_amount:.2f}"

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def add_data(self):
        # self.root_screen = self.manager.get_screen('ExtensionLoansProfileScreen')
        loan_id = str(self.root_screen.ids.loan_id.text)
        extension_fee = float(self.root_screen.ids.extension_fee.text)
        loan_extension_months = float(self.root_screen.ids.extension_months.text)
        extension_amount = float(self.ids.extension_amount.text)
        finial_repayment = float(self.ids.finial_repayment_amount.text)
        new_emi = float(self.ids.new_emi.text)
        reason = str(self.ids.reason.text)
        loan_status = ''
        customer_id = ''
        data = app_tables.fin_loan_details.search(loan_id=loan_id)
        if data:
            loan_status = data[0]['loan_updated_status']
            customer_id = data[0]['borrower_customer_id']
        # loan_status=str(self.root_screen.ids.loan_status.text)
        if loan_id and customer_id and extension_fee and loan_extension_months and extension_amount and finial_repayment and loan_status and new_emi and reason:
            app_tables.fin_extends_loan.add_row(loan_id=loan_id,
                                                borrower_customer_id=customer_id,
                                                extend_fee=extension_fee,
                                                extension_amount=extension_amount,
                                                final_repayment_amount=finial_repayment,
                                                new_emi=new_emi,
                                                reason=reason,
                                                status=loan_status,
                                                total_extension_months=loan_extension_months)
            sm = self.manager
            profile = ExtendLoansScreen(name='DashboardScreen')
            sm.add_widget(profile)  # Add the screen to the ScreenManager
            sm.current = 'DashboardScreen'

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ExtensionLoansProfileScreen'


class MyScreenManager(ScreenManager):
    pass