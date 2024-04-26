from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build (self):
        return Label (text= "Olá, SENAI!", font_size=100, font_name='Arial', color=get_color_from_hex("#FF5733"))
    halign= 'left' , 
    valign= 'top' ,
    size_hint=(None,None),
    size=(150,50),
    text_size=(150,None)
if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text= 'SENAI', color=[1,0,0,1],
            font_size=40, bold=True
        )

        self.lab2 = Label(
          text= 'SESI', color=[0,1,0,1],
          font_size=40, Italic=True 
        )

        self.lab3 = Label(
            text= 'ENEM', color= [0,0,1,1],
            font_size=40, font_name= 'Arial',
            underline= True
        )
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3) 
        return layout 
    
    if __name__ == '__main__': 
        App().run()
