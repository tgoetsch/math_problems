import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

# creating the App class
class MyApp(App):

    def build(self):

        # creating Floatlayout
        Fl = FloatLayout()

        # creating button
        # a button 30 % of the width and 50 %
        # of the height of the layout and
        # positioned at 20 % right and 20 % up
        # from bottom left, i.e x, y = 200, 200 from bottom left:
        btn = Button(text ='Hello world', size_hint =(.96, .96),
                     background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.02, 'y':.02 })

        btn.bind(on_press = self.callback)
        btn.bind(on_enter = self.wait_for_it)


        # adding widget i.e button
        Fl.add_widget(btn)

        # return the layout
        return Fl

    def callback(self, event):
        print('something')
        print(event)

    def wait_for_it(self, event):
        print('so close')

# run the App
if __name__ == "__main__":
    MyApp().run()