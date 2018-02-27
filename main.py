import socket

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.core.window import Window, WindowBase

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.focus import FocusBehavior


class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.size_hint_x = 0.5
        self.bind(size=self.on_size_change)

    def on_size_change(self, *args):
        self.text_size = self.size
        self.valign = 'middle'
        self.halign = 'center'


class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.multiline = False
        self.write_tab = False
        self.data = True
        self.prefix = ""
        self.is_essential = False


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.cols = 1
        self.size_hint_y = None
        self.height = 1750

        SampleDetailsLabel = Label(text="Sample Details")
        SampleDetailsLabel.size_hint_y = 0.25
        SampleDetailsInfo = GridLayout(cols=2)
        SampleNameLabel = MyLabel(text="Sample Name")
        SampleNameTextInput = MyTextInput()
        SampleNameTextInput.prefix = "Sample Name: "
        SampleNameTextInput.is_essential = True
        SubstrateLabel = MyLabel(text="Substrate")
        SubstrateTextInput = MyTextInput()
        SubstrateTextInput.prefix = "Substrate: "
        SubstrateTextInput.is_essential = True
        SubstrateOrientationLabel = MyLabel(text="Substrate Orientation")
        SubstrateOrientationTextInput = MyTextInput()
        SubstrateOrientationTextInput.prefix = "Substrate Orientation: "
        SubstrateOrientationTextInput.is_essential = True
        FilmLabel = MyLabel(text="Film")
        FilmTextInput = MyTextInput()
        FilmTextInput.prefix = "Film: "
        FilmTextInput.is_essential = True
        SampleDetailsInfo.add_widget(SampleNameLabel)
        SampleDetailsInfo.add_widget(SampleNameTextInput)
        SampleDetailsInfo.add_widget(SubstrateLabel)
        SampleDetailsInfo.add_widget(SubstrateTextInput)
        SampleDetailsInfo.add_widget(SubstrateOrientationLabel)
        SampleDetailsInfo.add_widget(SubstrateOrientationTextInput)
        SampleDetailsInfo.add_widget(FilmLabel)
        SampleDetailsInfo.add_widget(FilmTextInput)
        self.add_widget(SampleDetailsLabel)
        self.add_widget(SampleDetailsInfo)

        CleaningLabel = Label(text="Cleaning")
        CleaningLabel.size_hint_y = 0.25
        CleaningInfo = GridLayout(cols=2)
        BoilingAcetoneLabel = MyLabel(text="Boiling Acetone")
        BoilingAcetoneTextInput = MyTextInput()
        BoilingAcetoneTextInput.prefix = "Boiling Acetone: "
        BoilingIsoLabel = MyLabel(text="Boiling Isopropanol")
        BoilingIsoTextInput = MyTextInput()
        BoilingIsoTextInput.prefix = "Boiling Isopropanol: "
        ColdIsoLabel = MyLabel(text="Cold Isopropanol")
        ColdIsoTextInput = MyTextInput()
        ColdIsoTextInput.prefix = "Cold Isopropanol: "
        BoilingMethLabel = MyLabel(text="Boiling Methanol")
        BoilingMethTextInput = MyTextInput()
        BoilingMethTextInput.prefix = "Boiling Methanol: "
        ColdMethLabel = MyLabel(text="Cold Methanol")
        ColdMethTextInput = MyTextInput()
        ColdMethTextInput.prefix = "Cold Methanol: "
        NitrogenLabel = MyLabel(text="Nitrogen Blow-dry")
        NitrogenCheckBox = CheckBox()
        NitrogenCheckBox.prefix = "Nitrogen blow-dry: "
        CleaningInfo.add_widget(BoilingAcetoneLabel)
        CleaningInfo.add_widget(BoilingAcetoneTextInput)
        CleaningInfo.add_widget(BoilingIsoLabel)
        CleaningInfo.add_widget(BoilingIsoTextInput)
        CleaningInfo.add_widget(ColdIsoLabel)
        CleaningInfo.add_widget(ColdIsoTextInput)
        CleaningInfo.add_widget(BoilingMethLabel)
        CleaningInfo.add_widget(BoilingMethTextInput)
        CleaningInfo.add_widget(ColdMethLabel)
        CleaningInfo.add_widget(ColdMethTextInput)
        CleaningInfo.add_widget(NitrogenLabel)
        CleaningInfo.add_widget(NitrogenCheckBox)
        self.add_widget(CleaningLabel)
        self.add_widget(CleaningInfo)

        PreAnnealLabel = Label(text="Pre-Anneal")
        PreAnnealLabel.size_hint_y = 0.25
        PreAnnealInfo = GridLayout(cols=2)
        # PreAnnealInfo.padding = [30, 30, 30, 30]
        MaxTempLabel = MyLabel(text="Max Pre-Anneal Temperature")
        MaxTempTextInput = MyTextInput()
        MaxTempTextInput.prefix = "Pre-Anneal Temperature: "
        MaxTempTimeLabel = MyLabel(text="Time Spent at Max Temperature")
        MaxTempTimeTextInput = MyTextInput()
        MaxTempTimeTextInput.prefix = "Time Spent at Max Temperature: "
        GrowthTempLabel = MyLabel(text="Growth Temperature")
        GrowthTempTextInput = MyTextInput()
        GrowthTempTextInput.prefix = "Growth Temperature: "
        GrowthTempTimeLabel = MyLabel(
            text="Time taken to reach growth temperature")
        GrowthTempTimeTextInput = MyTextInput()
        GrowthTempTimeTextInput.prefix = "Time Taken to reach Growth Temperature: "
        PreAnnealInfo.add_widget(MaxTempLabel)
        PreAnnealInfo.add_widget(MaxTempTextInput)
        PreAnnealInfo.add_widget(MaxTempTimeLabel)
        PreAnnealInfo.add_widget(MaxTempTimeTextInput)
        PreAnnealInfo.add_widget(GrowthTempLabel)
        PreAnnealInfo.add_widget(GrowthTempTextInput)
        PreAnnealInfo.add_widget(GrowthTempTimeLabel)
        PreAnnealInfo.add_widget(GrowthTempTimeTextInput)
        self.add_widget(PreAnnealLabel)
        self.add_widget(PreAnnealInfo)

        GrowthLabel = Label(text="Growth")
        GrowthLabel.size_hint_y = 0.25
        GrowthInfo = GridLayout(cols=2)
        BasePressureLabel = MyLabel(text="Base Pressure")
        BasePressureTextInput = MyTextInput()
        BasePressureTextInput.prefix = "Base Pressure: "
        IgniteLabel = MyLabel(text="Plasma ignition details")
        IgniteTextInput = MyTextInput()
        IgniteTextInput.prefix = "Plasma Ignition Details: "
        PreSputterLabel = MyLabel(
            text="Pre-sputter details (time, pressure etc.)")
        PreSputterTextInput = MyTextInput()
        PreSputterTextInput.prefix = "Pre-Sputter Details: "
        SputterLabel = MyLabel(text="Sputter details (time, pressure etc.)")
        SputterTextInput = MyTextInput()
        SputterTextInput.prefix = "Sputter details: "
        GrowthInfo.add_widget(BasePressureLabel)
        GrowthInfo.add_widget(BasePressureTextInput)
        GrowthInfo.add_widget(IgniteLabel)
        GrowthInfo.add_widget(IgniteTextInput)
        GrowthInfo.add_widget(PreSputterLabel)
        GrowthInfo.add_widget(PreSputterTextInput)
        GrowthInfo.add_widget(SputterLabel)
        GrowthInfo.add_widget(SputterTextInput)
        self.add_widget(GrowthLabel)
        self.add_widget(GrowthInfo)

        PostAnnealLabel = Label(text="Post-Anneal")
        PostAnnealLabel.size_hint_y = 0.25
        PostAnnealInfo = GridLayout(cols=2)
        PostAnnealTempLabel = MyLabel(text="Post anneal temperature")
        PostAnnealTempTextInput = MyTextInput()
        PostAnnealTempTextInput.prefix = "Post-Anneal Temperature: "
        PostAnnealTempTimeLabel = MyLabel(text="Time to reach max temperature")
        PostAnnealTempTimeTextInput = MyTextInput()
        PostAnnealTempTimeTextInput.prefix = "Time taken to reach Max Temperature: "
        PostAnnealTimeLabel = MyLabel(text="Time spent at max temperature")
        PostAnnealTimeTextInput = MyTextInput()
        PostAnnealTimeTextInput.prefix = "Time Spent at Max Temperature: "
        PostAnnealInfo.add_widget(PostAnnealTempLabel)
        PostAnnealInfo.add_widget(PostAnnealTempTextInput)
        PostAnnealInfo.add_widget(PostAnnealTempTimeLabel)
        PostAnnealInfo.add_widget(PostAnnealTempTimeTextInput)
        PostAnnealInfo.add_widget(PostAnnealTimeLabel)
        PostAnnealInfo.add_widget(PostAnnealTimeTextInput)
        self.add_widget(PostAnnealLabel)
        self.add_widget(PostAnnealInfo)

        NotesLabel = Label(text="Additional Notes")
        NotesLabel.size_hint_y = 0.25
        NotesInfo = TextInput()
        NotesInfo.data = True
        NotesInfo.prefix = "Additional Notes related to Growth: "
        self.add_widget(NotesLabel)
        self.add_widget(NotesInfo)

        EnterDataButton = Button(text="Enter Data")
        EnterDataButton.bind(on_press=self.on_form_completion)
        self.add_widget(EnterDataButton)

        with self.canvas.before:
            BackgroundRectangle = Rectangle(
                size=[1080, 1920], source="colour.jpeg")

    def on_form_completion(self, *args, **kwargs):
        form_string = ""
        file_name = ""
        for kids in reversed(self.children):
            for grandkids in reversed(kids.children):
                try:
                    if grandkids.is_essential == True and grandkids.text == "":
                        print "Fill out all essential fields!"
                        return 0
                    if grandkids.data and grandkids.text != "":
                        if grandkids.prefix == "Sample Name: ":
                            file_name = grandkids.text
                        form_string += grandkids.prefix
                        form_string += grandkids.text
                        form_string += '\n'
                except:
                    pass
            try:
                if kids.data and kids.text != "":
                    form_string += kids.prefix
                    form_string += kids.text
                    form_string += '\n'
            except:
                pass

        ClientSocket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM)
        ClientSocket.connect(("sprongle.com", 6950))
        ClientSocket.send("filename: " + file_name)
        ClientSocket.send(form_string)
        ClientSocket.send("3D printing isn't even that cool")

        print form_string


class SputtererApp(App):
    def build(self):
        MakeScrollable = ScrollView(size=(Window.width, Window.height))
        Screen = MainScreen(padding=[30, 30, 30, 30])
        MakeScrollable.add_widget(Screen)
        return MakeScrollable


if __name__ == "__main__":
    App = SputtererApp()
    App.run()
