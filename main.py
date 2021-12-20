import socket

from kivy.app import App
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import threading
import socket


KV = """
MyBL:
        orientation: "vertical"
        
        size_hint: (0.95, 0.95)
        
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        Label:
                font_size: "30sp"
                text: root.data_label
        
        TextInput:
                id: Inp
                multiline: False
                padding: [15, 15, 15, 15]
        
        Button:
                text: "Поиск по названию"
                bold: True
                background_color: "#00FFCE"
                size_hint: (1, 0.5)
                on_press: root.callback()
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Thr0TT1e")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        SERVER, PORT = "localhost", 9491

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"SERVER: {SERVER}, PORT: {PORT}")
        # self.client.connect((SERVER, PORT))
        # self.client.sendall(bytes("979879789", "UTF-8"))

        threading.Thread(target=self.get_data).start()

    def callback(self):
        print("sendall()")
        self.client.sendall(bytes("Поиск по названию", "UTF-8"))

    def get_data(self):
        while App.get_running_app().running:
            in_data = self.client.recv(4096)
            print(f"От сервера: {in_data.decode()}")
            kkk = in_data.decode()
            self.set_data_label(kkk)

    @mainthread
    def set_data_label(self, data):
        self.data_label += f"{str(data)}\n"


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False

MyApp().run()
