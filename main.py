from kivy.uix.image import CoreImage
from kivy.uix.filechooser import string_types
from kivymd.uix.behaviors.toggle_behavior import MDFillRoundFlatButton
from kivy.uix.actionbar import Spinner
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.spinner import Spinner
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image 
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivymd.uix.spinner import MDSpinner
from kivy.uix.label import Label
import math
class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=[50, 50, 50, 50], spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # This ensures ScrollView can scroll when the content overflows

        scroll_view = ScrollView(size_hint=(1, 1))

        MDlabels = [
            'Tööliini pikkus(m)',
            'Voolikute läbimõõt',
            'Kadude konstant',
            'Vajalik rõhk(kPa)',
            'Kustutusvee hulk(l/s)'
        ]

        self.text_inputs = []

        left_side_card = MDCard(
            orientation='vertical',
            padding=dp(10),  # Slight padding for spacing
            spacing=dp(8),   # A bit less spacing between elements inside the card
            size_hint=(1, None),
            height=dp(235),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1  # Subtle shadow for a modern look
        )

        self.tööliini_pikkus_input = MDTextField(hint_text=MDlabels[0], size_hint_y=None, height=dp(40), input_filter='float', icon_right='ruler', helper_text='Meetrites', )
        self.tööliini_pikkus_input.text_color_normal = (1, 1, 1, 1)  # White color for non-focused state
        self.tööliini_pikkus_input.text_color_focus = (1, 1, 1, 1)
        self.text_inputs.append(self.tööliini_pikkus_input)
        left_side_card.add_widget(self.tööliini_pikkus_input)

        self.voolikute_läbimõõt_spinner = Spinner(text='Vali Ümbermõõt', values=('42', '51', '77', '100', '150'), size_hint_y=None, height=dp(40), color=(1, 1, 1, 1), background_color=(0, 0, 0, 1))
        left_side_card.add_widget(self.voolikute_läbimõõt_spinner)

        self.kadude_konstant_value = MDLabel(text='Kadude konstant: 0', size_hint_y=None, height=dp(40), color=(0, 0, 0, 1))
        left_side_card.add_widget(self.kadude_konstant_value)

        def update_kadude_konstant(spinner_value):
            values_dict = {'42': '16.2', '51': '6.3', '77': '0.75', '100': '0.15', '150': '0.023'}
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_value.text = f'Kadude konstant: {kadude_value}'

        self.voolikute_läbimõõt_spinner.bind(text=lambda spinner, value: update_kadude_konstant(value))

        self.kustutusvee_hulk_input = MDTextField(hint_text=MDlabels[4], size_hint_y=None, height=dp(40), input_filter='float', helper_text='Liitrit/sekundis, L/s')
        self.text_inputs.append(self.kustutusvee_hulk_input)

        left_side_card.add_widget(self.kustutusvee_hulk_input)

        right_side_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(235),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        self.tüviliini_pikkus_input_right = MDTextField(hint_text="Tüviliini pikkus(m)", size_hint_y=None, height=dp(40), input_filter='float', helper_text='Meetrites')
        self.voolikute_läbimõõt_spinner_right = Spinner(text='Vali Ümbermõõt', values=('42', '51', '77', '100', '150'), size_hint_y=None, height=dp(40), color=(1, 1, 1, 1), background_color=(0, 0, 0, 0.8))
        self.kadude_konstant_right_value = MDLabel(text='Kadude konstant: 0', size_hint_y=None, height=dp(40), color=(0, 0, 0, 1))
        self.kustutusvee_hulk_input_right = MDTextField(hint_text="Kustutusvee hulk(l/s)", size_hint_y=None, height=dp(40), input_filter='float', helper_text='Liitrit/sekundis, L/s')

        def update_kadude_konstant_right(spinner_value):
            values_dict = {'42': '16.2', '51': '6.3', '77': '0.75', '100': '0.15', '150': '0.023'}
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_right_value.text = f'Kadude konstant: {kadude_value}'

        self.voolikute_läbimõõt_spinner_right.bind(text=lambda spinner, value: update_kadude_konstant_right(value))

        right_side_card.add_widget(self.tüviliini_pikkus_input_right)
        right_side_card.add_widget(self.voolikute_läbimõõt_spinner_right)
        right_side_card.add_widget(self.kadude_konstant_right_value)
        right_side_card.add_widget(self.kustutusvee_hulk_input_right)

        third_box = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(140),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        self.vajalik_rõhk_input_third = MDTextField(hint_text="Vajalik rõhk", size_hint_y=None, height=dp(40), width=300, input_filter='float', helper_text='Joatoru 500kPa/5bar, Kinnine toiteliin 100kPa/1Bar')
        self.kõrgustest_rõhukadu_input_third = MDTextField(hint_text="Tõusumeetrid", size_hint_y=None, height=dp(40), input_filter='float', helper_text='Kui suur on kõrgustevahe pumbast - vooliku otsa?')

        third_box.add_widget(self.vajalik_rõhk_input_third)
        third_box.add_widget(self.kõrgustest_rõhukadu_input_third)

        box4 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(150),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        box5 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(100),
            style="outlined",
            line_color=(0, 0, 0, 0),
            md_bg_color=(0.5, 0.5, 0.5, 0)
        )

        self.result_MDlabel = MDLabel(text='Tööliini rõhukadu: ', size_hint_y=None, height=dp(40), color=(0, 0, 0, 1))
        self.right_result_MDlabel = MDLabel(text='Tüviliini rõhukadu: ', size_hint_y=None, height=dp(40), color=(0, 0, 0, 1))
        self.pumba_rõhk_MDlabel = MDLabel(text='Pumbarõhk: ', size_hint_y=None, height=dp(40), color=(1, 0, 0, 1))

        box4.add_widget(self.result_MDlabel)
        box4.add_widget(self.right_result_MDlabel)
        box4.add_widget(self.pumba_rõhk_MDlabel)

        # --- Add Unit Toggle Buttons ---
        self.unit_label = MDLabel(
            text="Rõhk: kPa",  # Default unit
            halign="center",
            font_style="H5",
            size_hint=(1, None),
            height=dp(50),
        )

        switch_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        self.left_button = ToggleButton(
            text="kPa",
            group="units",
            state="down",  # Default active button
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )
        self.right_button = ToggleButton(
            text="Bar",
            group="units",
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )

        # Bind ToggleButton events
        self.left_button.bind(on_press=self.update_unit)
        self.right_button.bind(on_press=self.update_unit)

        calculate_button = MDFillRoundFlatButton(
            text="Arvuta",
            size_hint=(None, None),
            width=dp(200),
            height=dp(40),
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
        )
        calculate_button.bind(on_press=self.calculate_result)

        layout.add_widget(left_side_card)
        layout.add_widget(right_side_card)
        layout.add_widget(third_box)
        layout.add_widget(box4)
        layout.add_widget(calculate_button)
        layout.add_widget(self.unit_label)
        switch_layout.add_widget(self.left_button)
        switch_layout.add_widget(self.right_button)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)
        
        layout.add_widget(switch_layout)
        layout.add_widget(box5)
    def update_unit(self, instance):
        if instance.text == "kPa":
            self.unit_label.text = "Rõhk: kPa"
        elif instance.text == "Bar":
            self.unit_label.text = "Rõhk: Bar"

    def calculate_result(self, instance):
        try:
            # Get all the values
            tööliini_pikkus = float(self.tööliini_pikkus_input.text or 0)
            kadude_konstant = float(self.kadude_konstant_value.text.split(": ")[-1] or 0)
            kustutusvee_hulk = float(self.kustutusvee_hulk_input.text or 0)
            result_left = (tööliini_pikkus * kadude_konstant * (kustutusvee_hulk ** 2)) / 100

            tüviliini_pikkus = float(self.tüviliini_pikkus_input_right.text or 0)
            kadude_konstant_right = float(self.kadude_konstant_right_value.text.split(": ")[-1] or 0)
            kustutusvee_hulk_right = float(self.kustutusvee_hulk_input_right.text or 0)
            kõrgustest_rõhukadu = float(self.kõrgustest_rõhukadu_input_third.text or 0)
            vajalik_rõhk = float(self.vajalik_rõhk_input_third.text or 0)
            result_right = (tüviliini_pikkus * kadude_konstant_right * (kustutusvee_hulk_right ** 2)) / 100

            pumba_rõhk = (1.1 * (result_left + result_right)) + (kõrgustest_rõhukadu * 10) + vajalik_rõhk

            # Check the selected unit and convert accordingly
            if self.left_button.state == "down":  # kPa selected
                self.result_MDlabel.text = f'Tööliini rõhukadu: {result_left} kPa'
                self.right_result_MDlabel.text = f'Tüviliini rõhukadu: {result_right} kPa'
                self.pumba_rõhk_MDlabel.text = f'Pumbarõhk: {pumba_rõhk} kPa'

            elif self.right_button.state == "down":  # Bar selected
                # Convert kPa to Bar (1 kPa = 0.01 Bar)
                result_left_bar = ((tööliini_pikkus * kadude_konstant * (kustutusvee_hulk ** 2)) / 100) / 100
                result_right_bar = ((tüviliini_pikkus * kadude_konstant_right * (kustutusvee_hulk_right ** 2)) / 100) / 100
                pumba_rõhk_bar = (((1.1 * (result_left + result_right)) / 100) + (kõrgustest_rõhukadu / 10) + vajalik_rõhk)

                self.result_MDlabel.text = f'Tööliini rõhukadu: {result_left_bar} Bar'
                self.right_result_MDlabel.text = f'Tüviliini rõhukadu: {result_right_bar} Bar'
                self.pumba_rõhk_MDlabel.text = f'Pumbarõhk: {pumba_rõhk_bar} Bar'

        except ValueError:
            pass
class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # Ensures ScrollView scrolls when content overflows

        scroll_view = ScrollView(size_hint=(1, 1))

        # Create container for input elements
        self.text_inputs = []

        # Left side card for the fields
        left_side_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(375),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        # Pumba rõhk (numeric only)
        self.pumba_rõhk_input = MDTextField(
            hint_text="Pumbarõhk (kPa)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="1bar = 100kPa"
        )
        self.text_inputs.append(self.pumba_rõhk_input)
        left_side_card.add_widget(self.pumba_rõhk_input)

        # Voolikute läbimõõt (spinner)
        self.voolikute_läbimõõt_spinner = Spinner(
            text='Vali Ümbermõõt',
            values=('42', '51', '77', '100', '150'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.voolikute_läbimõõt_spinner)

        # Kadude konstant
        self.kadude_konstant_value = MDLabel(
            text='Kadude konstant: 0',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.kadude_konstant_value)

        # Update Kadude konstant based on spinner value
        def update_kadude_konstant(spinner_value):
            values_dict = {'42': '16.2', '51': '6.3', '77': '0.75', '100': '0.15', '150': '0.023'}
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_value.text = f'Kadude konstant: {kadude_value}'

        self.voolikute_läbimõõt_spinner.bind(text=lambda spinner, value: update_kadude_konstant(value))

        # Tõusumeetrid input
        self.tõusumeetrid_input = MDTextField(
            hint_text="Tõusumeetrid(m)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="Kui suur on kõrgustevahe pumbast - vooliku otsa?"
        )
        self.text_inputs.append(self.tõusumeetrid_input)
        left_side_card.add_widget(self.tõusumeetrid_input)

        # Vooluhulk input
        self.vooluhulk_input = MDTextField(
            hint_text="Vooluhulk(L/s)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="L/s"
        )
        self.text_inputs.append(self.vooluhulk_input)

        # Lõpp Rõhk input
        self.lopprohk_input = MDTextField(
            hint_text="Lõpprõhk(kPa)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="Joatoru 500kPa, Kinnine toiteliin 100kPa"
        )
        self.text_inputs.append(self.lopprohk_input)
        left_side_card.add_widget(self.lopprohk_input)
        left_side_card.add_widget(self.vooluhulk_input)

        # Add the left side card to the layout
        layout.add_widget(left_side_card)

        # Button to trigger the calculation
        calculate_button = MDFillRoundFlatButton(
            text="Arvuta",
            size_hint=(None, None),
            width=dp(200),
            height=dp(40),
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
        )
        tühimik = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(100),
            style="outlined",
            line_color=(0, 0, 0, 0),
            md_bg_color=(0.5, 0.5, 0.5, 0)
        )

        result_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(80),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1   # Grey background
        )

        # Result label inside the card
        self.result_label = MDLabel(
            text="Voolikuliini maksimaalne pikkus: ",
            size_hint_y=None,
            height=dp(40),
            color=(1, 0, 0, 1),  # Red for error state initially
        )

        # Add the result label to the card
        result_card.add_widget(self.result_label)

        # Add result card and calculate button to layout
        layout.add_widget(result_card)
        layout.add_widget(calculate_button)
        

        # Add the layout to the screen
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)

        # Bind the calculate button to the calculate function
        calculate_button.bind(on_press=self.calculate_result)

        # --- Add Unit Toggle Buttons ---
        # Label to display the current unit
        self.unit_label = MDLabel(
            text="Rõhk: kPa",  # Default unit
            halign="center",
            font_style="H5",
            size_hint=(1, None),
            height=dp(50),
        )
        layout.add_widget(self.unit_label)

        # Switch layout for ToggleButtons
        switch_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        self.left_button = ToggleButton(
            text="kPa",
            group="units",
            state="down",  # Default active button
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )
        self.right_button = ToggleButton(
            text="Bar",
            group="units",
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )

        # Bind ToggleButton events
        self.left_button.bind(on_press=self.update_unit)
        self.right_button.bind(on_press=self.update_unit)

        # Add the buttons to the layout
        switch_layout.add_widget(self.left_button)
        switch_layout.add_widget(self.right_button)
        layout.add_widget(switch_layout)
        layout.add_widget(tühimik)
        # --- End of Unit Toggle Buttons ---
        
        # Default unit selected
        self.selected_unit = "kPa"  # Default is kPa
    
    def calculate_result(self, instance):
        # Validate if required fields are filled
        if not self.pumba_rõhk_input.text or not self.vooluhulk_input.text:
            self.result_label.text = "Täida kõik väljad!"
            self.result_label.color = (0, 0, 0, 1)
            return

        try:
            # Extract input values
            pumba_rõhk = float(self.pumba_rõhk_input.text)
            vooluhulk = float(self.vooluhulk_input.text)
            tõusumeetrid = float(self.tõusumeetrid_input.text) if self.tõusumeetrid_input.text else 0.0
            lopprohk = float(self.lopprohk_input.text) if self.lopprohk_input.text else 0.0
            kadude_konstant = float(self.kadude_konstant_value.text.split(": ")[-1])

            # Modify formula based on the selected unit (Bar or kPa)
            if self.selected_unit == "Bar":
                result = (((pumba_rõhk * 100) - (lopprohk * 100)- (tõusumeetrid*10)) / (kadude_konstant * vooluhulk**2) * 100) 
            else:
                result = ((pumba_rõhk - ((tõusumeetrid*10) + lopprohk)) / (kadude_konstant * vooluhulk**2)) * 100

            # Display the result
            self.result_label.text = f"Voolikuliini maksimaalne pikkus: {result:.2f} meetrit"
            self.result_label.color = (0, 0, 0, 1)

        except ValueError:
            # Handle invalid input
            self.result_label.text = "Invalid input"

    def update_unit(self, instance):
        """Update the label based on selected button."""
        if instance.text == "kPa":
            self.unit_label.text = "Rõhk: kPa"
            self.selected_unit = "kPa"  # Update selected unit to kPa
        elif instance.text == "Bar":
            self.unit_label.text = "Rõhk: Bar"
            self.selected_unit = "Bar"  # Update selected unit to Bar
   
        if instance.text == "kPa":
            self.unit_label.text = "Rõhk: kPa"
            self.selected_unit = "kPa"  # Update selected unit to kPa
            
            # Update the hint text for the pressure fields to show kPa
            self.pumba_rõhk_input.hint_text = "Pumbarõhk (kPa)"
            self.lopprohk_input.hint_text = "Lõpprõhk (kPa)"
            self.pumba_rõhk_input.helper_text = "1 bar = 100 kPa"

        elif instance.text == "Bar":
            self.unit_label.text = "Rõhk: Bar"
            self.selected_unit = "Bar"  # Update selected unit to Bar
        
        # Update the hint text for the pressure fields to show Bar
            self.pumba_rõhk_input.hint_text = "Pumbarõhk (Bar)"
            self.lopprohk_input.hint_text = "Lõpprõhk (Bar)"
            self.pumba_rõhk_input.helper_text = "1 bar = 100 kPa"
        
        if instance.text == "kPa":
            self.unit_label.text = "Rõhk: kPa"
            self.selected_unit = "kPa"  # Update selected unit to kPa
            
            # Update hint_text and helper_text for pressure fields to show kPa
            self.pumba_rõhk_input.hint_text = "Pumbarõhk (kPa)"
            self.lopprohk_input.hint_text = "Lõpprõhk (kPa)"
            self.pumba_rõhk_input.helper_text = "1 bar = 100 kPa"  # Keep this as a reference for conversion

        elif instance.text == "Bar":
            self.unit_label.text = "Rõhk: Bar"
            self.selected_unit = "Bar"  # Update selected unit to Bar
            
            # Update hint_text and helper_text for pressure fields to show Bar
            self.pumba_rõhk_input.hint_text = "Pumbarõhk (Bar)"
            self.lopprohk_input.hint_text = "Lõpprõhk (Bar)"
            self.pumba_rõhk_input.helper_text = "1 bar = 100 kPa"  # Keep this as a reference for conversion
class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # This ensures ScrollView can scroll when the content overflows
        
        scroll_view = ScrollView(size_hint=(1, 1))
        
        # Create container for input elements
        self.text_inputs = []

        # Left side card for the fields
        left_side_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(375),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        # Field 1: Pumba rõhk (numeric only)
        self.pumba_rõhk_input = MDTextField(
            hint_text="Pumbarõhk (kPa)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="10bar = 1000kPa"
        )
        self.text_inputs.append(self.pumba_rõhk_input)
        left_side_card.add_widget(self.pumba_rõhk_input)

        # Field 2: Voolikute läbimõõt (spinner with the same values)
        self.voolikute_läbimõõt_spinner = Spinner(
            text='Vali Ümbermõõt',
            values=('42', '51', '77', '100', '150'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.voolikute_läbimõõt_spinner)

        # Field 3: Kadude konstant (value updates dynamically based on spinner selection)
        self.kadude_konstant_value = MDLabel(
            text='Kadude konstant: 0',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.kadude_konstant_value)

        # Function to update Kadude konstant based on spinner value
        def update_kadude_konstant(spinner_value):
            values_dict = {'42': '16.2', '51': '6.3', '77': '0.75', '100': '0.15', '150': '0.023'}
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_value.text = f'Kadude konstant: {kadude_value}'

        self.voolikute_läbimõõt_spinner.bind(text=lambda spinner, value: update_kadude_konstant(value))

        # Field 4: Tõusumeetrid (numeric only)
        self.tõusumeetrid_input = MDTextField(
            hint_text="Kõrgustevahe",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="Kui suur on kõrgustevahe pumbast - vooliku otsa?"
        )
        self.text_inputs.append(self.tõusumeetrid_input)
        left_side_card.add_widget(self.tõusumeetrid_input)

        # Field 5: Voolikuliini pikkus (numeric only)
        self.voolikuliinipikkus_input = MDTextField(
            hint_text="Voolikuliini pikkus(m)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="meetrites"
        )
        self.text_inputs.append(self.voolikuliinipikkus_input)
        left_side_card.add_widget(self.voolikuliinipikkus_input)

        # Field 6: Lõpp Rõhk
        self.lopprohk_input = MDTextField(
            hint_text="Lõpprõhk(kPa)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="Joatoru 500kPa/5Bar, kinnine toiteliin 100kPa/1Bar"
        )
        self.text_inputs.append(self.lopprohk_input)
        left_side_card.add_widget(self.lopprohk_input)

        # Add the left side card to the layout
        layout.add_widget(left_side_card)

        result_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(80),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1   # Grey background for the card
        )

        # Add the result label inside the card
        self.result_label = MDLabel(
            text="Vooluhulk:",
            size_hint_y=None,
            height=dp(40),
            color=(1, 0, 0, 1),  # Initially red for error state
            halign="left"
        )

        # Add the result label to the card
        result_card.add_widget(self.result_label)

        # Add the result card to the layout
        layout.add_widget(result_card)

        # Button to trigger the calculation
        calculate_button = MDFillRoundFlatButton(
            text="Arvuta",
            size_hint=(None, None),
            width=dp(200),
            height=dp(40),
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
            on_release=self.calculate_result  # Link the button to the calculation function
        )
        layout.add_widget(calculate_button)
        
        box5 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(100),
            style="outlined",
            line_color=(0, 0, 0, 0),
            md_bg_color=(0.5, 0.5, 0.5, 0)
        )
        
        # --- Add Unit Toggle Buttons --- #
        # Label to display the current unit
        self.unit_label = MDLabel(
            text="Rõhk: kPa",  # Default unit
            halign="center",
            font_style="H5",
            size_hint=(1, None),
            height=dp(50),
        )
        layout.add_widget(self.unit_label)

        # Switch layout for ToggleButtons
        switch_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        self.left_button = ToggleButton(
            text="kPa",
            group="units",
            state="down",  # Default active button
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )
        self.right_button = ToggleButton(
            text="Bar",
            group="units",
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )

        # Bind ToggleButton events
        self.left_button.bind(on_press=self.update_unit)
        self.right_button.bind(on_press=self.update_unit)

        # Add the buttons to the layout
        switch_layout.add_widget(self.left_button)
        switch_layout.add_widget(self.right_button)
        layout.add_widget(switch_layout)
        # --- End of Unit Toggle Buttons --- #
        layout.add_widget(box5)
        # Add the layout to the scroll view
        scroll_view.add_widget(layout)
        
        # Add ScrollView to the screen
        self.add_widget(scroll_view)

    def update_unit(self, instance):
    # Update the unit label and hint text based on the button pressed
        if instance.text == "kPa":
                self.unit_label.text = "Rõhk: kPa"
                self.pumba_rõhk_input.hint_text = "Pumbarõhk (kPa)"  # Update hint text
                self.lopprohk_input.hint_text = "Lõpprõhk (kPa)"
        elif instance.text == "Bar":
                self.unit_label.text = "Rõhk: Bar"
                self.pumba_rõhk_input.hint_text = "Pumbarõhk (Bar)"  # Update hint text
                self.lopprohk_input.hint_text = "Lõpprõhk (Bar)"

    def calculate_result(self, instance):
            try:
        # Retrieve values from inputs
                pumba_rõhk = float(self.pumba_rõhk_input.text) if self.pumba_rõhk_input.text else 0
                lõpp_rõhk = float(self.lopprohk_input.text) if self.lopprohk_input.text else 0
                tõusumeetrid = float(self.tõusumeetrid_input.text) if self.tõusumeetrid_input.text else 0
                voolikuliinipikkus = float(self.voolikuliinipikkus_input.text) if self.voolikuliinipikkus_input.text else 0
                kadude_konstant = float(self.kadude_konstant_value.text.split(":")[1].strip()) if self.kadude_konstant_value.text != "Kadude konstant: 0" else 0

                # Check if required fields are empty
                if pumba_rõhk == 0 or voolikuliinipikkus == 0 or kadude_konstant == 0:
                    self.result_label.text = "Täida kõik vajalikud väljad!"
                    self.result_label.color = (0, 0, 0, 1)  # Red color for errors
                    return

                # Unit check: If Bar is selected, convert pumba_rõhk and lõpp_rõhk to kPa
                if self.unit_label.text == "Rõhk: Bar":
                    # Bar to kPa conversion: multiply by 100
                    pumba_rõhk = pumba_rõhk * 100  # Convert pumba_rõhk to kPa
                    lõpp_rõhk = lõpp_rõhk * 100 # Convert lõpp_rõhk to kPa

                    # Apply the formula for Bar (scaled to kPa)
                    numerator = (pumba_rõhk) - (lõpp_rõhk + (tõusumeetrid*10))
                    denominator = (voolikuliinipikkus * kadude_konstant)

                    if denominator == 0:
                        self.result_label.text = "Vältige nulli jagamist!"
                        self.result_label.color = (1, 0, 0, 1)  # Red color for errors
                        return

                    result = ((numerator / denominator) * 100) ** 0.5  # Square root of the fraction
                    self.result_label.text = f"Vooluhulk: {result:.2f}L/s"
                    self.result_label.color = (0, 0, 0, 1)  # Green color for valid result

                else:
                    # Apply the formula for kPa (standard)
                    numerator = (pumba_rõhk) - (lõpp_rõhk + (tõusumeetrid*10))
                    denominator = (voolikuliinipikkus * kadude_konstant)

                    if denominator == 0:
                        self.result_label.text = "Vältige nulli jagamist!"
                        self.result_label.color = (1, 0, 0, 1)  # Red color for errors
                        return

                    result = ((numerator / denominator) * 100) ** 0.5  # Square root of the fraction
                    self.result_label.text = f"Vooluhulk: {result:.2f}L/s"
                    self.result_label.color = (0, 0, 0, 1)  # Green color for valid result

            except ValueError:
                # Handle any invalid input
                self.result_label.text = "Sisestatud andmed ei ole õiged!"
                self.result_label.color = (1, 0, 0, 1)  # Red color for errors

class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # This ensures ScrollView can scroll when the content overflows
        
        scroll_view = ScrollView(size_hint=(1, 1))
        
        # Create container for input elements
        self.text_inputs = []

        # Left side card for the fields
        left_side_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(375),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1 
        )

        # Field 1: Pumba rõhk (numeric only)
        self.pumba_rõhk_input = MDTextField(
            hint_text="Pumbarõhk (kPa)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="10bar = 1000kPa"
        )
        self.text_inputs.append(self.pumba_rõhk_input)
        left_side_card.add_widget(self.pumba_rõhk_input)

        # Field 2: Voolikute läbimõõt (spinner with the same values)
        self.voolikute_läbimõõt_spinner = Spinner(
            text='Vali Ümbermõõt',
            values=('42', '51', '77', '100', '150'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.voolikute_läbimõõt_spinner)

        # Field 3: Kadude konstant (value updates dynamically based on spinner selection)
        self.kadude_konstant_value = MDLabel(
            text='Kadude konstant: 0',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.kadude_konstant_value)

        # Function to update Kadude konstant based on spinner value
        def update_kadude_konstant(spinner_value):
            values_dict = {'42': '16.2', '51': '6.3', '77': '0.75', '100': '0.15', '150': '0.023'}
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_value.text = f'Kadude konstant: {kadude_value}'

        self.voolikute_läbimõõt_spinner.bind(text=lambda spinner, value: update_kadude_konstant(value))

        # Field 4: Tõusumeetrid (numeric only)
        self.tõusumeetrid_input = MDTextField(
            hint_text="Kõrgustevahe",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="Kui suur on kõrgustevahe pumbast - vooliku otsa?"
        )
        self.text_inputs.append(self.tõusumeetrid_input)
        left_side_card.add_widget(self.tõusumeetrid_input)

        # Field 5: Voolikuliini pikkus (numeric only)
        self.voolikuliinipikkus_input = MDTextField(
            hint_text="Voolikuliini pikkus(m)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            helper_text="meetrites"
        )
        self.text_inputs.append(self.voolikuliinipikkus_input)
        left_side_card.add_widget(self.voolikuliinipikkus_input)

        # Field 6: Lõpp Rõhk
        self.vooluhulk_input = MDTextField(
            hint_text="Vooluhulk(l/s)",
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
        )
        self.text_inputs.append(self.vooluhulk_input)
        left_side_card.add_widget(self.vooluhulk_input)

        # Add the left side card to the layout
        layout.add_widget(left_side_card)

        result_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(80),
            style="outlined",  # Keep outlined for a cleaner look
            radius=[10],  # Rounded corners for modern style
            line_width=3,  # Thinner border for a subtle effect
            line_color=(0, 0, 0, 0.3),  # Lighter, less harsh border color
            md_bg_color=(0, 0.5, 0.5, 1),  
            elevation=1   # Grey background for the card
        )

        # Add the result label inside the card
        self.result_label = MDLabel(
            text="Lõpprõhk:",
            size_hint_y=None,
            height=dp(40),
            color=(1, 0, 0, 1),  # Initially red for error state
            halign="left"
        )

        # Add the result label to the card
        result_card.add_widget(self.result_label)

        # Add the result card to the layout
        layout.add_widget(result_card)

        # Button to trigger the calculation
        calculate_button = MDFillRoundFlatButton(
            text="Arvuta",
            size_hint=(None, None),
            width=dp(200),
            height=dp(40),
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1),
            on_release=self.calculate_result  # Link the button to the calculation function
        )
        layout.add_widget(calculate_button)
        
        box5 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(100),
            style="outlined",
            line_color=(0, 0, 0, 0),
            md_bg_color=(0.5, 0.5, 0.5, 0)
        )
        
        # --- Add Unit Toggle Buttons --- #
        # Label to display the current unit
        self.unit_label = MDLabel(
            text="Rõhk: kPa",  # Default unit
            halign="center",
            font_style="H5",
            size_hint=(1, None),
            height=dp(50),
        )
        layout.add_widget(self.unit_label)

        # Switch layout for ToggleButtons
        switch_layout = BoxLayout(size_hint=(1, None), height=dp(50), spacing=10)
        self.left_button = ToggleButton(
            text="kPa",
            group="units",
            state="down",  # Default active button
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )
        self.right_button = ToggleButton(
            text="Bar",
            group="units",
            background_color=(1, 1, 1, 1),
            color=(1, 1, 1, 1),
        )

        # Bind ToggleButton events
        self.left_button.bind(on_press=self.update_unit)
        self.right_button.bind(on_press=self.update_unit)

        # Add the buttons to the layout
        switch_layout.add_widget(self.left_button)
        switch_layout.add_widget(self.right_button)
        layout.add_widget(switch_layout)
        # --- End of Unit Toggle Buttons --- #
        layout.add_widget(box5)
        # Add the layout to the scroll view
        scroll_view.add_widget(layout)
        
        # Add ScrollView to the screen
        self.add_widget(scroll_view)

    def update_unit(self, instance):
    # Update the unit label and hint text based on the button pressed
        if instance.text == "kPa":
                self.unit_label.text = "Rõhk: kPa"
                self.pumba_rõhk_input.hint_text = "Pumbarõhk (kPa)"  # Update hint text
                
        elif instance.text == "Bar":
                self.unit_label.text = "Rõhk: Bar"
                self.pumba_rõhk_input.hint_text = "Pumbarõhk (Bar)"  # Update hint text
                

    def calculate_result(self, instance):
            try:
        # Retrieve values from inputs
                pumba_rõhk = float(self.pumba_rõhk_input.text) if self.pumba_rõhk_input.text else 0
                vooluhulk = float(self.vooluhulk_input.text) if self.vooluhulk_input.text else 0
                tõusumeetrid = float(self.tõusumeetrid_input.text) if self.tõusumeetrid_input.text else 0
                voolikuliinipikkus = float(self.voolikuliinipikkus_input.text) if self.voolikuliinipikkus_input.text else 0
                kadude_konstant = float(self.kadude_konstant_value.text.split(":")[1].strip()) if self.kadude_konstant_value.text != "Kadude konstant: 0" else 0

                # Check if required fields are empty
                if pumba_rõhk == 0 or voolikuliinipikkus == 0 or kadude_konstant == 0:
                    self.result_label.text = "Täida kõik vajalikud väljad!"
                    self.result_label.color = (0, 0, 0, 1)  # Red color for errors
                    return

                # Unit check: If Bar is selected, convert pumba_rõhk and lõpp_rõhk to kPa
                if self.unit_label.text == "Rõhk: Bar":
                    # Bar to kPa conversion: multiply by 100
                    pumba_rõhk = pumba_rõhk * 100  # Convert pumba_rõhk to kPa
                

                    # Apply the formula for Bar (scaled to kPa)
                    numerator = (pumba_rõhk - (tõusumeetrid*10))
                    denominator = (voolikuliinipikkus * kadude_konstant * (vooluhulk * vooluhulk) / 100)

                    if denominator == 0:
                        self.result_label.text = "Vältige nulli jagamist!"
                        self.result_label.color = (1, 0, 0, 1)  # Red color for errors
                        return

                    result = (numerator - denominator)  # Square root of the fraction
                    self.result_label.text = f"Lõpprõhk: {result:.2f}Bar"
                    self.result_label.color = (0, 0, 0, 1)  # Green color for valid result

                else:
                    # Apply the formula for kPa (standard)
                    numerator = (pumba_rõhk - (tõusumeetrid*10))
                    denominator = (voolikuliinipikkus * kadude_konstant * (vooluhulk * vooluhulk) / 100)

                    if denominator == 0:
                        self.result_label.text = "Vältige nulli jagamist!"
                        self.result_label.color = (1, 0, 0, 1)  # Red color for errors
                        return

                    result = (numerator - denominator) # Square root of the fraction
                    self.result_label.text = f"Lõpprõhk: {result:.2f}kPa"
                    self.result_label.color = (0, 0, 0, 1)  # Green color for valid result

            except ValueError:
                # Handle any invalid input
                self.result_label.text = "Sisestatud andmed ei ole õiged!"
                self.result_label.color = (1, 0, 0, 1)  # Red color for errors

class Screen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=[50, 50, 50, 50], spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # Ensure ScrollView can scroll when content overflows

        scroll_view = ScrollView(size_hint=(1, 1))

        MDlabels = [
            'Mahuti diameeter',
            'Mahuti Kõrgus',
            'Intensiivsus l*s/m',
            'Vabapõlmeise aeg',
            'Vooluhulk'
        ]

        self.text_inputs = []

        # Left-side card
        left_side_card = MDCard(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(8),
            size_hint=(1, None),
            height=dp(220),
            style="outlined",
            radius=[10],
            line_width=3,
            line_color=(0, 0, 0, 0.3),
            md_bg_color=(0, 0.5, 0.5, 1),
            elevation=1
        )

        self.tööliini_pikkus_input = MDTextField(
            hint_text=MDlabels[0],
            size_hint_y=None,
            height=dp(40),
            input_filter='float',
            icon_right='ruler',
            helper_text='Meetrites'
        )
        self.tööliini_pikkus_input.text_color_normal = (1, 1, 1, 1)
        self.tööliini_pikkus_input.text_color_focus = (1, 1, 1, 1)
        self.text_inputs.append(self.tööliini_pikkus_input)
        left_side_card.add_widget(self.tööliini_pikkus_input)

        self.voolikute_läbimõõt_spinner = Spinner(
            text='Vali Mahuti Kõrgus',
            values=('Põlev üle 12m', 'Kõrvalasuv üle 12m', 'Põlev Vallitus üle 12m', 'Põlev alla 12m', 'Kõrvalasuv alla 12m', 'Põlev vallitus alla 12m'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.voolikute_läbimõõt_spinner)

        self.kadude_konstant_value = MDLabel(
            text='Jahutusvee intensiivsus: 0',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.kadude_konstant_value)

        def update_kadude_konstant_left(spinner_value):
            values_dict = {
                'Põlev üle 12m': '0.75',
                'Kõrvalasuv üle 12m': '0.3',
                'Põlev Vallitus üle 12m': '1.1',
                'Põlev alla 12m': '0.5',
                'Kõrvalasuv alla 12m': '0.2',
                'Põlev vallitus alla 12m': '1'
            }
            kadude_value = values_dict.get(spinner_value, '0')
            self.kadude_konstant_value.text = f'Intensiivsus meetri kohta: {kadude_value}'

        self.voolikute_läbimõõt_spinner.bind(
            text=lambda spinner, value: update_kadude_konstant_left(value)
        )

        self.result_MDlabel = MDLabel(
            text='Vajalik jahutusvee intensiivsus: ',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        left_side_card.add_widget(self.result_MDlabel)

        # Right-side card
        right_side_card = MDCard(
            orientation="vertical",
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(280),
            style="outlined",
            radius=[10],
            line_width=3,
            line_color=(0, 0, 0, 0.3),
            md_bg_color=(0, 0.5, 0.5, 1),
            elevation=1
        )

        self.tüviliini_pikkus_input_right = MDTextField(
            hint_text="Reservuaari vabaseina kõrgus",
            size_hint_y=None,
            height=dp(40),
            input_filter="float",
            helper_text="Meetrites"
        )
        self.vabapõlemise_aeg = MDTextField(
            hint_text="Vabapõlemise aeg",
            size_hint_y=None,
            height=dp(40),
            input_filter="float",
            helper_text="Tundides"
        )

        self.voolikute_läbimõõt_spinner_right = Spinner(
            text="Vali Tume Naftasaadus",
            values=("Masuut", "Nafta", "Diisel", ),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 0.8)
        )

        self.kadude_konstant_right_value = MDLabel(
            text="Joonsoojenemiskiirus: 0",
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )

        def update_kadude_konstant_right(spinner_value):
            constants = {
                "Masuut": 0.3,
                "Nafta": 0.4,
                "Diisel": 0.08
            }
            constant = constants.get(spinner_value, 0)
            self.kadude_konstant_right_value.text = f"Joonsoojenemiskiirus: {constant}"

        self.voolikute_läbimõõt_spinner_right.bind(
            text=lambda spinner, value: update_kadude_konstant_right(value)
        )

        right_side_card.add_widget(self.tüviliini_pikkus_input_right)
        right_side_card.add_widget(self.vabapõlemise_aeg)
        right_side_card.add_widget(self.voolikute_läbimõõt_spinner_right)
        right_side_card.add_widget(self.kadude_konstant_right_value)

        self.right_result_MDlabel = MDLabel(
            text="Ohutustingimus: ",
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1),
            markup= True
        )
        right_side_card.add_widget(self.right_result_MDlabel)

        box4 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(150),
            style="outlined",
            radius=[10],
            line_width=3,
            line_color=(0, 0, 0, 0.3),
            md_bg_color=(0, 0.5, 0.5, 1),
            elevation=1
        )

        

        layout.add_widget(left_side_card)
        layout.add_widget(right_side_card)
       

        calculate_button = MDFillRoundFlatButton(
            text="Arvuta",
            size_hint=(None, None),
            width=dp(200),
            height=dp(40),
            pos_hint={'center_x': 0.5},
            md_bg_color=(0.2, 0.6, 0.2, 1)
        )
        calculate_button.bind(on_press=self.calculate_result)

############ VAHTKUSTUTAMISE PLANEERIMISE OSA###### Liiguta pärast paika!
        box5 = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(640),
            style="outlined",
            radius=[10],
            line_width=3,
            line_color=(0, 0, 0, 0.3),
            md_bg_color=(0, 0.5, 0.5, 1),
            elevation=1
        )

        self.pindala_MDTextField = MDTextField(
            hint_text="Pindala m²",
            size_hint_y=None,
            height=dp(40),
            input_filter="float",
            helper_text="Ruutmeetrites m²"
        )
        self.vahukadu_MDTextField = MDTextField(
            hint_text="Vahukadu",
            size_hint_y=None,
            height=dp(40),
            input_filter="float",
            helper_text="Mitu % ?"
        )
        
        self.Vedelikupolaarsus_spinner = Spinner(
            text='Polaarne või Mittepolaarne vedelik?',
            values=('Polaarne', 'Mittepolaarne'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )

        self.vahulahuseintensiivsus_value = MDLabel(
            text="Vahulahuse intenvsiivsus: 0",
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )

        def update_vahulahuseintensiivsus_value(spinner_value):
            constants = {
                "Polaarne": 4,
                "Mittepolaarne": 6,
            }
            constant = constants.get(spinner_value, 0)
            self.vahulahuseintensiivsus_value.text = f"Vahulahuse intensiivsus: {constant} L/min"

        self.Vedelikupolaarsus_spinner.bind(
            text=lambda spinner, value: update_vahulahuseintensiivsus_value(value)
        )

############## KUSTUTUSAEG
        self.vahurünnakuaeg_spinner = Spinner(
            text='Vahurünnaku aeg',
            values=('Mahuti 20min', 'Maapinnal olev vedelik 15min'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )

        self.vahuaeg_value = MDLabel(
            text="Vahurünnaku aeg: 0",
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )

        def update_vahurünnakuaeg_value(spinner_value):
            constants = {
                "Mahuti 20min": 20,
                "Maapinnal olev vedelik 15min": 15,
            }
            constant = constants.get(spinner_value, 0)
            self.vahuaeg_value.text = f"Vahurünnaku aeg: {constant} Min"

        self.vahurünnakuaeg_spinner.bind(
            text=lambda spinner, value: update_vahurünnakuaeg_value(value)
        )
        ###Tööriist###

        self.töövahend_spinner = Spinner(
            text='Töövahend',
            values=('Total M4S4', 'GPS600'),
            size_hint_y=None,
            height=dp(40),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1)
        )

        self.vahenditootlikus_value = MDLabel(
            text="Tööriista tootlikus:",
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )

        def update_töövahend_value(spinner_value):
            constants = {
                "Total M4S4": 400,
                "GPS600": 360,
            }
            constant = constants.get(spinner_value, 0)
            self.vahenditootlikus_value.text = f"Tööriista tootlikus: {constant} L/min"

        self.töövahend_spinner.bind(
            text=lambda spinner, value: update_töövahend_value(value)
        )

        ####VASTUSTE RIDA#####
        self.vastus1_MDlabel = MDLabel(
            text='Vahulahust : ',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        

        self.vastus2_MDlabel = MDLabel(
            text='Vajalik vahuaine kogus: ',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        self.vastus3_MDlabel = MDLabel(
            text='Vett: ',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        self.vastus4_MDlabel = MDLabel(
            text='Töövahendite arv: ',
            size_hint_y=None,
            height=dp(40),
            color=(0, 0, 0, 1)
        )
        box5.add_widget(self.töövahend_spinner)
        box5.add_widget(self.vahenditootlikus_value)
        box5.add_widget(self.Vedelikupolaarsus_spinner)
        box5.add_widget(self.vahulahuseintensiivsus_value)
        box5.add_widget(self.vahurünnakuaeg_spinner)
        box5.add_widget(self.vahuaeg_value)
        box5.add_widget(self.pindala_MDTextField)
        box5.add_widget(self.vahukadu_MDTextField)
        box5.add_widget(self.vastus1_MDlabel)
        box5.add_widget(self.vastus2_MDlabel)
        box5.add_widget(self.vastus3_MDlabel)
        box5.add_widget(self.vastus4_MDlabel)
        layout.add_widget(box5)

        layout.add_widget(calculate_button)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)

 ############################### SIIN ON TÜHIMIK
        Tühimik = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(1, None),
            height=dp(400),
            style="outlined",
            radius=[10],
            line_width=3,
            line_color=(0, 0, 0, 0),
            md_bg_color=(0, 0.5, 0.5, 0),
            elevation=1
        )
        layout.add_widget(Tühimik)
    #########################################
    def calculate_result(self, instance):
        try:
            tööliini_pikkus = float(self.tööliini_pikkus_input.text or 0)
            kadude_konstant = float(self.kadude_konstant_value.text.split(": ")[-1] or 0)
            result_left = ((tööliini_pikkus * 3.14) * kadude_konstant)
            self.result_MDlabel.text = f'Vajalik jahutusvee intensiivsus: {result_left:.2f} l/s'

            # Right calculation
            tüviliini_pikkus = float(self.tüviliini_pikkus_input_right.text or 0)
            kadude_konstant_right = float(self.kadude_konstant_right_value.text.split(": ")[-1] or 0)
            vabapõlemise_aeg = float(self.vabapõlemise_aeg.text or 0)
            ###Vahtkustutuseplaneerimisearvutus###
    # Fetch and parse inputs
            vahukadu = float(self.vahukadu_MDTextField.text.replace('%', '').strip() or 0) / 100 + 1  # Convert percentage to a decimal
            pindala = float(self.pindala_MDTextField.text or 0)
            vahenditootlikus = float(self.vahenditootlikus_value.text.split(": ")[-1].replace(" L/min", "").strip() or 0)
            vahulahuseintensiivsus = float(self.vahulahuseintensiivsus_value.text.split(": ")[-1].replace(" L/min", "") or 0)
            vahuaeg = float(self.vahuaeg_value.text.split(": ")[-1].replace(" Min", "") or 0)

            # Check if any required inputs are zero
            if vahukadu == 0 or pindala == 0 or vahulahuseintensiivsus == 0 or vahuaeg == 0:
                raise ValueError("All inputs must be provided and greater than zero.")

            # First calculation
            vastus1 = vahukadu * pindala * vahulahuseintensiivsus * vahuaeg
            self.vastus1_MDlabel.text = f"Vahulahust: {vastus1:.2f} Liitrit"

            # Second calculation
            vastus2 = vastus1 * 0.03
            self.vastus2_MDlabel.text = f"Vajalik vahuaine kogus: {vastus2:.2f} Liitrit"

            vastus3 = vastus1 - vastus2
            self.vastus3_MDlabel.text = f"Vajalik Vee kogus: {vastus3: .2f} Liitrit"

            result = (vahukadu * pindala * vahulahuseintensiivsus) / vahenditootlikus
            vastus4 = math.ceil(result)  # Round up to the nearest whole number

        # Update the label with the rounded result
            self.vastus4_MDlabel.text = f"Töövahendite arv: {vastus4}"

        except ValueError:
            # Error handling for invalid or missing inputs
            self.vastus1_MDlabel.text = "Viga: Kontrolli sisendväärtusi."
            self.vastus2_MDlabel.text = "Viga: Kontrolli sisendväärtusi."

            

            # Check condition for "result_right"
            if vabapõlemise_aeg * kadude_konstant_right < tüviliini_pikkus:
                  self.right_result_MDlabel.text = "[color=00FF00]Ohutustingimus on tagatud, ülekeemise ohtu ei ole.[/color]"
            else:
                self.right_result_MDlabel.text = "[color=FF0000]ÜLEKEEMISE OHT, kustutada vallituse tagant.[/color]"


        except ValueError:
            self.result_MDlabel.text = "Invalid input!"
            self.right_result_MDlabel.text = "Invalid input!"
            


class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Add canvas instructions for background color
        with self.canvas.before:
            Color(0.1, 0.5, 0.8, 1)  # RGBA color (light blue)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        # Bind to update rectangle size and position when layout changes
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class NavigationButtons(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        # Create a BoxLayout that will hold the buttons horizontally
        layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(10),  # Adjust spacing using dp for better scaling
            size_hint=(None, None),
            height=dp(70),  # Use dp for height
            padding=(0, 0, 0, 0)
        )
        layout.bind(minimum_width=layout.setter('width'))  # Adjust width to fit children
        layout.pos_hint = {'top': 1}  # Positioning the layout at the top of the screen

        # Buttons for navigation
        button1 = MDRaisedButton(text="Pumbarõhk", size_hint=(None, None), width=dp(200), height=dp(50), md_bg_color=(0, 0.5, 0.5, 1))
        button2 = MDRaisedButton(text="Liinipikkus", size_hint=(None, None), width=dp(200), height=dp(50), md_bg_color=(0, 0.5, 0.5, 1))
        button3 = MDRaisedButton(text="Vooluhulk", size_hint=(None, None), width=dp(200), height=dp(50), md_bg_color=(0, 0.5, 0.5, 1))
        button4 = MDRaisedButton(text="Lõpprõhk", size_hint=(None, None), width=dp(200), height=dp(50), md_bg_color=(0, 0.5, 0.5, 1))
        button5 = MDRaisedButton(text="Vahtkustutus", size_hint=(None, None), width=dp(200), height=dp(50), md_bg_color=(0, 0.5, 0.5, 1))
        # Bind buttons to the screen change functions
        button1.bind(on_release=self.change_to_screen_1)
        button2.bind(on_release=self.change_to_screen_2)
        button3.bind(on_release=self.change_to_screen_3)
        button4.bind(on_release=self.change_to_screen_4)
        button5.bind(on_release=self.change_to_screen_5)
        # Add buttons to layout
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)

        # Create a ScrollView to make the buttons scrollable horizontally
        scroll_view = ScrollView(
            do_scroll_y=False,  # Disable vertical scrolling
            do_scroll_x=True,   # Enable horizontal scrolling
            size_hint=(1, None),  # Allow full width for the scrollable area
            height=dp(130),      # Use dp for height
            pos_hint={"top": 1},  # Position at the top of the screen
        )

        # Add layout to scroll view
        scroll_view.add_widget(layout)

        # Add ScrollView to the FloatLayout
        self.add_widget(scroll_view)

    def change_to_screen_1(self, instance):
        self.screen_manager.current = "screen1"

    def change_to_screen_2(self, instance):
        self.screen_manager.current = "screen2"

    def change_to_screen_3(self, instance):
        self.screen_manager.current = "screen3"

    def change_to_screen_4(self, instance):
        self.screen_manager.current = "screen4"

    def change_to_screen_5(self, instance):
        self.screen_manager.current = "screen5"

class MyApp(MDApp):
    def build(self):
        # Set the app icon
        self.title = "Vesivarustus"
        self.icon = "kpa.png"  # Replace with the path to your icon file
        self.splash_animation = None

        sm = ScreenManager()

        # Create the Navigation Buttons and pass the ScreenManager instance
        nav_buttons = NavigationButtons(screen_manager=sm)

        # Add all screens to the screen manager
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        sm.add_widget(Screen5(name='screen5'))

        # Create a root layout
        root_layout = FloatLayout()

        # Set the theme colors
        self.theme_cls.primary_palette = "Gray"  # Set a neutral primary color (gray for a white theme look)
        self.theme_cls.primary_hue = "50"  # Lighter shade for the primary color
        
        # Add the background image (ensure your image file exists)
        background = Image(
            source="taust1.png",  # Path to your background image
            allow_stretch=True,
            keep_ratio=False,  # Make the background cover the entire app
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        root_layout.add_widget(background)

        # Add the navigation buttons at the top (fixed position)
        root_layout.add_widget(nav_buttons)

        # Add the screen manager layout and adjust the position to avoid overlap with the navigation buttons
        sm.pos_hint = {'top': 0.90}  # Adjust this to ensure content is below the nav
        root_layout.add_widget(sm)

        # Add the "Made by Oliver Tigas" footer
        footer_label = Label(
            text="Made by Oliver Tigas",
            size_hint=(1, 0.05),  # Adjust height to fit the footer
            pos_hint={'center_x': 0.5, 'y': 0},  # Position at the bottom
            halign="center",
            valign="middle",
            font_size=24 # Adjust font size as needed
        )
        footer_label.bind(size=footer_label.setter('text_size'))  # Ensure text is centered
        root_layout.add_widget(footer_label)

        return root_layout


if __name__ == "__main__":
    MyApp().run()
