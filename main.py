import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class Interface(GridLayout):
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="Present Value Calculator"))

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Number of Payments: "))
        self.n = TextInput(multiline=False)
        self.inside.add_widget(self.n)

        self.inside.add_widget(Label(text="Amount per Payment: "))
        self.p = TextInput(multiline=False)
        self.inside.add_widget(self.p)

        self.inside.add_widget(
            Label(text="Interest Rate for the Corresponding Period: "))
        self.i = TextInput(multiline=False)
        self.inside.add_widget(self.i)

        self.PV_submit = Button(text="Calculate the Present Value")
        self.PV_submit.bind(on_press=self.PV_calculate)
        self.inside.add_widget(self.PV_submit)

        self.add_widget(self.inside)

    def PV_calculate(self, instance):
        str_i = self.i.text
        str_n = self.n.text
        str_p = self.p.text
        try:
            i = float(str_i)
            n = float(str_n)
            p = float(str_p)
        except ValueError:
            dismiss = Button(text="Close")
            popup = Popup(title="Wrong Type of Input", content=Label(
                text="Please re-enter the Values"), auto_dismiss=False)
            dismiss.bind(on_press=popup.dismiss)
            popup.open()
            return
        v = 1/(1+i)
        pv = p*(1-v ** n)/(i)
        self.txt_pv = Label(text=str(pv))
        self.inside.add_widget(self.txt_pv)
        return

    def is_num(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False
        else:
            return False


class Financial_Calculator(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    Financial_Calculator().run()
