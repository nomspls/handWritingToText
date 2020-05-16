from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os
import pytesseract
import cv2


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color('white')
            d = 5.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        

class WordReaderApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        ss = Button(text='Read')
        ss.bind(on_release=self.popme)
        parent.add_widget(self.painter)
        parent.add_widget(ss)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
        self.popupp.dismiss()
        
    def popme(self, obj):

        Window.screenshot(name='test.png')
        img = cv2.imread('test0001.png')
        inverted = cv2.bitwise_not(img)      
        self.textt = pytesseract.image_to_string(inverted, lang='eng')
        
        popbtn = Button(text='Retry')
        popbtn.bind(on_release=self.clear_canvas)
        
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=self.textt))
        box.add_widget(popbtn)
        
        self.popupp = Popup(title='Trying to predict what is written...:', content=box, 
        size_hint=(None, None), size=(400, 400))
        os.remove('test0001.png')
        self.popupp.open()
        
if __name__ == '__main__':
    WordReaderApp().run()
